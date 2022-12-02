STATUS = { 
    'SUCCESS': 1,
    'NOT_LOGIN': 2,
    'NOT_PERMISSION': 3,
    'INPUT_INVALID': 4,
    'TOKEN_EXPIRED': 5,
    'NO_DATA': 6,
    'FAIL_REQUEST': 7
}

ERROR = {
    'wrong_password': 'Wrong password.',
    'not_exists': ' is not exists.',
    'refresh_token':'refresh_token is not exists.',
    'not_login':'Not logged in, token is null.',
    'token_not_exists':'Token is not exists.',
    'access_token':'Token fails, you can refresh token.',
    'user_exists': {
        'Username or email':'tai khoan da ton tai'
    },
    'user_exists_deleted': {
        'Username or email':'Tai khoan da ton tai, hay doi trang thai tai khoan'
    },
}

SUCCESS = {
    'login':'Login success.',
    'refresh_token':'Refresh success.',
}