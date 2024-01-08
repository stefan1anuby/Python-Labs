import pika, sys, os , json , time
from pywebcopy import save_webpage

rabbitmq_host = os.environ.get('RABBITMQ_HOST','localhost')
rabbitmq_queue = os.environ.get('RABBITMQ_QUEUE','workerpool')

def checkDirIsEmpty(dir_path):
    if os.path.exists(dir_path):
        if len(os.listdir(dir_path)) != 0:
            return False
    return True

def handle_download_page(message):

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