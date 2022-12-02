def get_urls(list_url):
    new_list = []
    for item in list_url:
        new_list.append('/' + str(item.pattern))
    return new_list