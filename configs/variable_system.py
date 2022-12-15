import os
from django.conf import settings as st
from enum import Enum

KEY_RSA = 'duanfpro'

U = 'username'
P = 'password'

EXCEL_TYPE = "xl"

JSON_TYPE = "json"

OPEN_TYPE = {
    'action': {
        'read':'r',
        'append':'a',
        'write':'w',
        'create':'x'
    },
    'type': {
        'text':'t',
        'binary': 'b'
    }
}

FILES = {
    'download_file':'download-file'
}

TOKEN = {
    'private_key':'anphMNcZkh',
    'public_key':'fnEcdMHkm',
    'type':'Bearer ',
    'hash':'HS256',
    'tls_access_token':3600,
    'tls_refresh_token':10800
}

GROUP_URL = {
    'url_swagger',
    'url_auth',
    'url_test',
    'url_in_media',
}

MEDIA_ROOT = st.MEDIA_ROOT

STR_MEDIA_PATH = '{}{}.{}'

STR_CURRENT_HOST = '{}://{}'