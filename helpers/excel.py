import pandas
import os
from django.conf import settings
import excel2json
import json

def read_excel(request):
    # xls = pandas.ExcelFile('/home/an/Desktop/python/social_network/media/609122022160802.xlsx')
    file = os.path.join(settings.MEDIA_ROOT, '609122022162155.xlsx')
    xls = excel2json.convert_from_file(file)
    # print(xls)
    excel_data_df = pandas.read_excel(file)
    json_str = excel_data_df.to_json(orient='records')
    return json.loads(json_str)