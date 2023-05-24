from rest_framework import serializers
from .models import (
    Passenger,
    Flight,
    Reservation
)

# -----------------------------------------------------------
# -------------------- FixSerializer ------------------------
# -----------------------------------------------------------


class FixSerializer(serializers.ModelSerializer):
    created = serializers.StringRelatedField()  # model field'i
    created_id = serializers.IntegerField(required=False)  # database column'i

    # ModelSerializer create override edildi
    # created_id girmeden o anki user'in id'sini alip created_id olarak isleme
    def create(self, validated_data):
        validated_data['created_id'] = self.context['request'].user.id
        return super().create(validated_data)


# -----------------------------------------------------------
# ----------------- PassengerSerializer ---------------------
# -----------------------------------------------------------


class PassengerSerializer(FixSerializer):

    gender_text = serializers.SerializerMethodField()

    class Meta:
        model = Passenger
        exclude = []
        # fields = '__all__' + [
        #     'get_gender_display'
        # ] # denendi calismadi - TypeError: can only concatenate str (not "list") to str

    def get_gender_text(self, obj):
        return obj.get_gender_display()


# -----------------------------------------------------------
# ------------------- FlightSerializer ----------------------
# -----------------------------------------------------------

class FlightSerializer(FixSerializer):
    departure_text = serializers.SerializerMethodField()  # return from get_fieldName()
    # arrival = serializers.SerializerMethodField() # mevcut field da override edilebilir
    arrival_text = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        # exclude = []
        fields = (
            "id",
            "created",
            "created_id",
            "departure_text",
            "arrival_text",
            "created_time",
            "updated_time",
            "flight_number",
            "airline",
            "departure",
            "departure_date",
            "arrival",
            "arrival_date",
            "get_airline_display"  # dont need SerializationMethodField, directly returns fieldName
        )

    def get_departure_text(self, obj):
        return obj.get_departure_display()  # obj.get_fieldName

    def get_arrival_text(self, obj):
        return obj.get_arrival_display()


# -----------------------------------------------------------
# ----------------- ReservationSerializer -------------------
# -----------------------------------------------------------

# class ReservationSerializer(FixSerializer):
#     flight = serializers.StringRelatedField()  # only __str__()
#     flight_id = serializers.IntegerField(write_only=True)

#     reservation_flight = FlightSerializer(
#         read_only=True)  # complete data, ForeignKey()

#     reservation_passenger = PassengerSerializer(
#         read_only=True, many=True)  # ManyToMany()

#     passenger_count = serializers.SerializerMethodField()

#     class Meta:
#         model = Reservation
#         exclude = []

#     def get_passenger_count(self, obj):
#         return obj.passenger.count()  # obj.fieldName.method

#     # def create(self, validated_data):
#     #     passenger_data = validated_data.pop("passenger")
#     #     validated_data["user_id"] = self.context["request"].user.id
#     #     reservation = Reservation.objects.create(**validated_data)
#     #     for passenger in passenger_data:
#     #         pas = Passenger.objects.create(**passenger)
#     #         reservation.passenger.add(pas)
#     #     reservation.save()
#     #     return reservation


class ReservationSerializer(FixSerializer):

    flight_id = serializers.IntegerField(write_only=True)
    passenger_ids = serializers.ListField(write_only=True)

    flight = FlightSerializer(read_only=True)  # ForeingKey()
    passenger = PassengerSerializer(read_only=True, many=True)  # ManyToMany()

    class Meta:
        model = Reservation
        exclude = []

    def create(self, validated_data):
        # model'deki passenger(iliskili field oldugu icin database'de passenger_id'leri arar)
        validated_data["passenger"] = validated_data.pop('passenger_ids')
        return super().create(validated_data)

    # def create(self, validated_data):
    #     from django.shortcuts import get_object_or_404

    #     flight_id = validated_data.pop('flight_id')
    #     passenger_ids = validated_data.pop('passenger_ids')

    #     # Fetch the Flight instance.
    #     flight = get_object_or_404(Flight, id=flight_id)

    #     # Fetch the Passenger instances.
    #     passengers = [get_object_or_404(Passenger, id=id)
    #                   for id in passenger_ids]

    # List comprehension : [expression for item in iterable]
    # passenger_ids listesindeki her bir id değeri için bir Passenger nesnesi getirir

    #     # Create a new Reservation instance.
    #     reservation = Reservation.objects.create(flight=flight)

    #     # Associate the passengers to the reservation.
    #     reservation.passenger.set(passengers)

    #     return reservation
