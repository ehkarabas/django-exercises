from rest_framework import serializers

# ------------------------------------
# User Serializer
# ------------------------------------

from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
        required = True, # EmailField required default'u False
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
  
  password = serializers.CharField(
        # password required default'u True
        required = True,
        write_only = True,
    )
  
  class Meta:
    model = User
    # fields = "__all__"
    exclude = [
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
        ]
    
  # password alanının her zaman doğru bir şekilde hashlendiğinden emin olmak için hem create hem de update method'larini override etmek best-practice'tir ve set_password ile hash'lenir.

  '''
  # env\Lib\site-packages\rest_framework\serializers.py
  # Model Serializer'larindaki create method'u override edilerek, password'un hashlenip saklanmasi saglanir. Bu ornek icin buna gerek yoktur, cunku POST'ta password required True olacagi icin password'un girilmis olmasi gerekecektir ve validate override'inda da password alani zaten hash'lenmektedir.
  def create(self, validated_data):
    # password = validated_data.pop('password', None)
    password = validated_data.pop('password')
    # if password is None:
    #     raise serializers.ValidationError("Password field is required")
    instance = self.Meta.model(**validated_data)
    instance.set_password(password)
    instance.save()
    return instance
  '''
  
  # env\Lib\site-packages\rest_framework\serializers.py
  # Model Serializer'larindaki get_fields method'u override edilerek, model field'larinin hangi kosullara gore required olacagi kontrol edilebilir.
  def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        if request and getattr(request, 'method', None) == "PUT":
            fields['password'].required = False
        return fields
  
  # env\Lib\site-packages\rest_framework\serializers.py
  # Model Serializer'larindaki update method'u override edilerek, password'un hashlenip saklanmasi saglanir. Bu ornekte get_fields override'inda PUT request'lerde password required false olarak ayarlanmis olsa bile, password girilerek de PUT yapilabilecegi icin bu durumda hashlenmemis olacaktir, bu da bir guvenlik acigi olusturacagi icin update bu ornekte override edilmelidir.
  # Django Rest Framework'te update metodu hem PUT hem de PATCH isteklerinde çağrılır.
  def update(self, instance, validated_data):
      for attr, value in validated_data.items():
          if attr == 'password':
              instance.set_password(value)
          else:
              setattr(instance, attr, value)
      instance.save()
      return instance
  
  '''
  # Bir patch isleminde hangi field'larin guncellenebilecegi update override'inda belirlenebilir, izin verilmeyen alanlarda guncelleme yapilamaz. Bu nedenle boyle durumlarda update override'lari validate override'i yapilsa bile onem kazanmaktadir.
  class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
  # Bu ornekte, bir PATCH isteği sırasında password alanı gönderilse bile, bu değer update metodunda belirtilmediği için kullanılmayacak ve password güncellenmeyecektir.
  '''
  
  # env\Lib\site-packages\rest_framework\serializers.py
  # Base Serializer'indaki validate method'u override edilerek, password'un hashlenip saklanmasi saglanir. validate metodu, her türlü istekte (POST, PUT, PATCH vb.) çağrılır ve verileri işlemeden önce doğrulama yapar.
  def validate(self, attrs):
        if attrs.get('password', False):
            from django.contrib.auth.password_validation import validate_password
            from django.contrib.auth.hashers import make_password
            password = attrs['password']
            validate_password(password)
            attrs.update({'password': make_password(password)})
        return super().validate(attrs)

# ------------------------------------
# User Token Serializer
# ------------------------------------

from dj_rest_auth.serializers import TokenSerializer

class UserTokenSerializer(TokenSerializer):
    # Token model'inde user icin gecerli olan field name user oldugundan burada da user kullanilmalidir. somethingAnother = UserSerializer() AttributeError verecektir.
    user = UserSerializer()
    # dj_rest_auth\serializers.py TokenSerializer meta'si override ediliyor.
    class Meta(TokenSerializer.Meta):
        fields = ("key","user")