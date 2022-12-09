from rest_framework import serializers

class FileDownloadValidate(serializers.Serializer):
    id = serializers.CharField()
    type = serializers.CharField(required=False, allow_null=True)

    def validate(self, value):
        name = str(value['id']).split('.')
        if not name[0].isdigit():
            raise serializers.ValidationError({'File name':'not_exists'})
        value['id'] = name[0]
        value['type'] = name[-1]
        return value
        
    