from rest_framework.serializers import ModelSerializer
from .models import Todo

class TodoSerializer(ModelSerializer):
    class Meta: # yapisal ozelliklerin(default ozelliklerin) degistirildigi yer
        model = Todo
        # fields = "__all__"
        exclude = ["created_date","updated_date"]