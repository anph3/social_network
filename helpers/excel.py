import pandas
import os
from django.conf import settings
import json

def read_excel(request):
    file = os.path.join(settings.MEDIA_ROOT, '615122022101422.xlsx')
    excel_data_df = pandas.read_excel(file)
    json_str = excel_data_df.to_json(orient='records')
    return json.loads(json_str)