from rest_framework import serializers
from .models import (
    Car,
    Reservation,
)

# ------------------------------------
# Fix Serializer
# ------------------------------------

class FixSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(required=False, read_only=True)

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        return super().create(validated_data)


# ------------------------------------
# Car Serializer
# ------------------------------------

class CarSerializer(FixSerializer):
    class Meta:
        model = Car
        fields = "__all__"

    
    # env\Lib\site-packages\rest_framework\serializers.py
    # Model Serializer'larindaki get_fields method'u override edilerek, model field'larinin hangi kosullara gore gosterilecegi kontrol edilebilir.
    def get_fields(self):
        fields = super().get_fields() # Model field'larini collection type'ta toplar.
        user = self.context.get('request').user # Serializer'larda o an giris yapmis user verisi daima bu sekilde alinir.

        # Staff degilse gosterilmeyecek olan field'lar
        if not user.is_staff:
            fields.pop('created')
            fields.pop('updated')
            fields.pop('plate')
            fields.pop('availability')
        
        return fields

# ------------------------------------
# Reservation Serializer
# ------------------------------------

class ReservationSerializer(FixSerializer):
    car = serializers.StringRelatedField()
    # car_id = serializers.IntegerField(required=False, read_only=True)
    # POST, UPDATE, PATCH icin iliskili ID'ye erismek gerekli, bunun icin de PrimaryKeyRelatedField kullanilir.
    car_id = serializers.PrimaryKeyRelatedField(source='car', queryset=Car.objects.all())

    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = "__all__"
    
    def get_total_price(self, obj):
        return obj.car.rent_per_day * (obj.end_date - obj.start_date).days

    # Django'daki UniqueConstraintlar genellikle veritabanı seviyesinde bir kısıtlamadır ve bu, bir save() işlemi sırasında yürütülür. Ancak, bu tür bir kısıtlama, DRF serializer'ı tarafından kontrol edilmez. Dolayısıyla, verilerinizi serialize etmek ve deserialize etmek için kullandığınız serializer'da bu tür bir kısıtlamanın kontrolünü sağlamak istiyorsanız, bu kontrolü manuel olarak eklemelisiniz.

    # ReservationSerializer'da bu kısıtlamayı kontrol etmek için bir validate metodunu override etmek gerekiyor. Bu metod, serializer'a gelen verileri kontrol eder ve belirttiğiniz kısıtlamalara uyup uymadığını kontrol eder.

    # env\Lib\site-packages\rest_framework\serializers.py
    # Base Serializer'indaki validate method'u override ediliyor
    def validate(self, data):
        user = self.context['request'].user
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if self.Meta.model.objects.filter(user=user, start_date=start_date, end_date=end_date).exists():
            raise serializers.ValidationError("Reservation with this User, Start date and End date already exists.")
        return data
    
    '''
    #get_serializer_context: Bu metod, serializer'a verilecek context'i oluşturur. Eğer bu metod override edilmezse, default olarak bir context oluşturulur fakat bu context'te request objesi bulunmayabilir. Bu durumda, serializerınızın validate metodunda self.context['request'].user ifadesi çalışmayabilir çünkü context'te request objesi bulunmamaktadır. Bu durum bir KeyError hatası verir.
    def get_serializer_context(self):
        return {'request': self.request}

    #perform_create ve perform_update: Bu metodlar, bir objenin oluşturulması ve güncellenmesi sırasında çağrılır. Bu metodlar override edilmezse, objeler normal şekilde oluşturulur ve güncellenir. Ancak, perform_create ve perform_update metodlarını override ederek serializer.save(user=self.request.user) ifadesini eklerseniz, her oluşturma ve güncelleme işlemi sırasında user alanı otomatik olarak oturum açmış olan kullanıcı olur. Bu durumda, user alanını her POST ve PUT/PATCH request'te göndermenize gerek kalmaz. Eğer bu metodları override etmezseniz, user alanını her request'te manuel olarak göndermeniz gerekir.
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    '''