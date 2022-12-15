from .views import *

class MailView(ViewSet):
    def send_mail(self, request):
        data = request.data.copy()
        validate = MailValidate(data=data)
        if not validate.is_valid():
            return validate_error(validate.errors)
        
        result = validate.data
        if hp.send_mail(
            subject = result['subject'],
            body = result['body'],
            to = result['to'],
            cc = result['cc'],
            bcc = result['bcc']
        ):
            return response_data(
                message=SUCCESS['send_mail']
            )
        return response_data(
            status=STATUS['FAIL_REQUEST'], 
            message=ERROR['send_mail']
        )