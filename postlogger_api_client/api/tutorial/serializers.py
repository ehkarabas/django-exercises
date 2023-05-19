from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Tutorial


class TutorialSerializer(ModelSerializer):
    class Meta:
        model = Tutorial
        fields = '__all__'

    def validate(self, attrs):
        if attrs['title'] == attrs['description']:
            raise ValidationError(
                {'message': 'Title and description must be different'})
        return attrs
