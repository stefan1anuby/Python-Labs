import pika , os ,json , requests , re

rabbitmq_host = os.environ.get('RABBITMQ_HOST','localhost')
rabbitmq_queue = os.environ.get('RABBITMQ_QUEUE','workerpool')
data_to_store_path = os.environ.get('STORAGE_PATH','/data')

def get_top_pages_for_country(country):
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
    result = {}
    countries = ['argentina', 'australia', 'austria', 'belgium', 'brazil', 'bulgaria', 'canada', 'chile', 'colombia', 'croatia', 'czech-republic', 'denmark', 'egypt', 'finland', 'france', 'germany', 'greece', 'hong-kong', 'hungary', 'india', 'indonesia', 'iraq', 'ireland', 'israel', 'italy', 'japan', 'korea-republic-of', 'kuwait', 'malaysia', 'mexico', 'morocco', 'netherlands', 'new-zealand', 'norway', 'pakistan', 'peru', 'philippines', 'poland', 'portugal', 'qatar', 'romania', 'russia', 'saudi-arabia', 'serbia', 'singapore', 'slovakia', 'south-africa', 'spain', 'sweden', 'switzerland', 'taiwan', 'thailand', 'turkey', 'ukraine', 'united-arab-emirates', 'united-kingdom', 'united-states', 'venezuela', 'vietnam']
    for country in countries:
        list = get_top_pages_for_country(country)
        if list is not None:
            result[country] = list
   
    return result if len(result) != 0 else None

def map_top_pages_dict_to_message_list(top_pages_dict):
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
    