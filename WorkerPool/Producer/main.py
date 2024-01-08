import pika , os ,json , requests , re

"""
Environment Variables:
    RABBITMQ_HOST: The host of the RabbitMQ server. Defaults to 'localhost'.
    RABBITMQ_QUEUE: The RabbitMQ queue name to consume messages from. Defaults to 'workerpool'.
    STORAGE_PATH: Location to store the downloaded pages.
"""

rabbitmq_host = os.environ.get('RABBITMQ_HOST','localhost')
rabbitmq_queue = os.environ.get('RABBITMQ_QUEUE','workerpool')
data_to_store_path = os.environ.get('STORAGE_PATH','/data')

def get_top_pages_for_country(country):
    """
    Retrieves the top web pages for a specified country from similarweb.com.

    Args:
        country (str): The name of the country for which to retrieve the top web pages.

    Returns:
        list: A list of top web pages for the specified country. Returns None if no pages are found or if an HTTP request error occurs.
    """
    url = "https://www.similarweb.com/top-websites/" + country + "/"
    agent = {"User-Agent":"Mozilla/5.0"}
    response = requests.get(url,headers=agent)
    
    if response.status_code == 200:
        html_content = response.text
    else:
        print(f"Failed to retrieve the HTML content for country \"{country}\". Status code: {response.status_code}")
        return None
    
    pattern = r"https://www\.similarweb\.com/website/([^/]+(?:\.[^/]+)+)/"

    matches = re.findall(pattern, html_content)

    return matches if len(matches) != 0 else None

def get_top_pages_every_country():
    """
    Retrieves the top web pages for a predefined list of countries.

    Iterates over a predefined list of countries and uses `get_top_pages_for_country` to fetch the top web pages for each. 

    Args:
        None

    Returns:
        dict: A dictionary with country names as keys and lists of top web pages as values. Returns None if no data is retrieved.
    """
    result = {}
    countries = ['argentina', 'australia', 'austria', 'belgium', 'brazil', 'bulgaria', 'canada', 'chile', 'colombia', 'croatia', 'czech-republic', 'denmark', 'egypt', 'finland', 'france', 'germany', 'greece', 'hong-kong', 'hungary', 'india', 'indonesia', 'iraq', 'ireland', 'israel', 'italy', 'japan', 'korea-republic-of', 'kuwait', 'malaysia', 'mexico', 'morocco', 'netherlands', 'new-zealand', 'norway', 'pakistan', 'peru', 'philippines', 'poland', 'portugal', 'qatar', 'romania', 'russia', 'saudi-arabia', 'serbia', 'singapore', 'slovakia', 'south-africa', 'spain', 'sweden', 'switzerland', 'taiwan', 'thailand', 'turkey', 'ukraine', 'united-arab-emirates', 'united-kingdom', 'united-states', 'venezuela', 'vietnam']
    for country in countries:
        list = get_top_pages_for_country(country)
        if list is not None:
            result[country] = list
   
    return result if len(result) != 0 else None

def map_top_pages_dict_to_message_list(top_pages_dict):
    """
    Maps a dictionary of top web pages to a list of messages suitable for RabbitMQ publishing.

    Args:
        top_pages_dict (dict): A dictionary with country names as keys and lists of web pages as values.

    Returns:
        list: A list of messages, where each message is a dictionary containing 'domain' and 'location' keys. Returns None if the input dictionary is empty.
    """
    messages = []
    for country,country_top_pages_list in top_pages_dict.items():
        for page in country_top_pages_list:
            message = {"domain" : page ,  "location" : data_to_store_path + "/" + country + "/"}
            messages.append(message)
    
    return messages if len(messages) != 0 else None


def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection.channel()

    channel.queue_declare(queue=rabbitmq_queue)

    top_pages_dict = get_top_pages_every_country()
    if top_pages_dict is None:
        print("ERROR!! Coudn't get pages!")
        exit()

    message_list = map_top_pages_dict_to_message_list(top_pages_dict)
    if message_list is None:
        print("ERROR!! Coudn't map pages to message list!")
        exit()

    for message in message_list:
        print(message)
        channel.basic_publish(exchange='', routing_key=rabbitmq_queue, body=json.dumps(message))
        print(f" [x] Sent : {message}")

    connection.close()
    print("Connection closed !")

if __name__ == '__main__':
    main()
    