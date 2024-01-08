

import pika, sys, os , json , time
from pywebcopy import save_webpage

"""
Environment Variables:
    RABBITMQ_HOST: The host of the RabbitMQ server. Defaults to 'localhost'.
    RABBITMQ_QUEUE: The RabbitMQ queue name to consume messages from. Defaults to 'workerpool'.
"""

rabbitmq_host = os.environ.get('RABBITMQ_HOST','localhost')
rabbitmq_queue = os.environ.get('RABBITMQ_QUEUE','workerpool')

def checkDirIsEmpty(dir_path):
    """
    Check if a given directory is empty.

    Args:
        dir_path (str): Path of the directory to check.

    Returns:
        bool: True if the directory is empty or does not exist, False otherwise.
    """
    if os.path.exists(dir_path):
        if len(os.listdir(dir_path)) != 0:
            return False
    return True

def handle_download_page(message):
    """
    Handles the downloading of a webpage.

    Extracts 'domain' and 'location' from the message, and downloads the webpage using `pywebcopy`.
    The function first checks if the target directory is empty before downloading.

    Args:
        message (dict): A dictionary containing 'domain' and 'location' keys.

    Returns:
        bool: True if the download is successful, False otherwise.
    """

    if "domain" not in message.keys():
        print("The message doesn't contain domain key")
        return False
    
    if "location" not in message.keys():
        print("The message doesn't contain location key")
        return False
    
    domain = message["domain"]
    location = message["location"]
    target_path = location + domain 

    if checkDirIsEmpty(target_path) is False:
        print(f"{target_path} already exists !")
        return False
    
    delay = 0.5
    save_webpage("https://www." + domain, location ,bypass_robots=True , open_in_browser=False ,project_name=domain , delay=delay)
    if checkDirIsEmpty(target_path):
        save_webpage("https://" + domain, location ,bypass_robots=True , open_in_browser=False , project_name=domain , delay=delay)
    
    if checkDirIsEmpty(target_path):
        print(f"Downloading {domain} failed !")
        return False
    
    print(f"Downloading {domain} succeded !")
    return True

def rabbitmq_callback(ch, method, properties, body):
    """
    Processes and acknowledges messages from a RabbitMQ queue.

    Attempts to download webpages based on message content, with up to three retries. Acknowledges the message 
    upon successful download. The message is expected to be a JSON object containing 'domain' and 'location' keys.

    Args:
        ch (BlockingChannel): The channel associated with the RabbitMQ connection.
        method (spec.Basic.Deliver): Delivery information of the message.
        properties (spec.BasicProperties): Message properties.
        body (bytes): The message body in byte format.

    Returns:
        None: This function does not return a value.
    """
    message = json.loads(body)
    print(f" [x] Received {message}")

    max_tries = 3
    tries = 0
    result = None
    delay = 1
    while result is None and tries < max_tries :
        try:
            result = handle_download_page(message)
        except Exception as e:
            print(e)
            time.sleep(delay)
        tries += 1
    if result is True:
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print("Message handled with success !")
    else:
        print("Message failed to be handled !")

def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection.channel()

    channel.queue_declare(queue=rabbitmq_queue)
    channel.basic_consume(queue=rabbitmq_queue, on_message_callback=rabbitmq_callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    main()