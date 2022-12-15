from rest_framework import serializers


class MailValidate(serializers.Serializer):
    subject = serializers.CharField()
    body = serializers.CharField()
    to = serializers.ListField()
    cc = serializers.ListField(
        required=False,
        allow_null=True,
        default=['']
    )
    bcc = serializers.ListField(
        required=False, 
        allow_null=True,
        default=['']
    )