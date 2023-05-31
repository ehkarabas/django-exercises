from rest_framework import serializers
from .models import Department, Personnel

class FixSerializer(serializers.ModelSerializer):

    created_by_user = serializers.StringRelatedField(read_only=True)
    created_by_uid = serializers.SerializerMethodField()

    def create(self, validated_data):
        validated_data['created_by_user'] = self.context['request'].user
        return super().create(validated_data)
    
    def get_created_by_uid(self, obj):
        return obj.created_by_user.id

class DepartmentSerializer(FixSerializer):
    
    class Meta:
        model = Department
        # fields = "__all__"
        exclude = []

# class TitleField(serializers.ChoiceField): # ise yaramadi, post yaparken NOT NULL constraint failed: personnel_personnel.title hatasi alindi.
#     def __init__(self, **kwargs):
#         super().__init__(choices=Personnel.TITLES, **kwargs)

#     def to_representation(self, value):
#         return dict(Personnel.TITLES).get(value)

#     def to_internal_value(self, data):
#         titles_dict = {v: k for k, v in Personnel.TITLES}
#         return titles_dict.get(data)
    

class PersonnelSerializer(FixSerializer):
    
    # title = serializers.SerializerMethodField() # SerializerMethodField read only'dir, write icin to_representation ve to_internalValue kullanilmasi onerilmektedir.
    # title = TitleField() # ise yaramadi, post yaparken NOT NULL constraint failed: personnel_personnel.title hatasi alindi.
    department_name = serializers.SerializerMethodField()
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), write_only=True)
    
    class Meta:
        model = Personnel
        # fields = "__all__"
        # exclude = []
        fields = (
            'first_name',
            'last_name',
            'department', # write-only -> int(id)
            'department_name', # read-only -> str(name)
            'title',
            'gender',
            'salary',
            )
        
    def get_department_name(self,obj):
        department = obj.department
        if department is not None:
            return department.name
        return None
    
    # def get_title(self, obj): SerializerMethodField read only'dir, write icin to_representation ve to_internalValue kullanilmasi onerilmektedir.
        # return obj.get_title_display()


class DepartmentPersonnelSerializer(serializers.ModelSerializer):
    
    personnels = PersonnelSerializer(many=True,read_only=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'personnels')