from api_app import urls

def get_list_url(value):
    list_url = []
    for item in urls.all_url[value]:
        list_url.append('/'+str(item.pattern))
    return list_url