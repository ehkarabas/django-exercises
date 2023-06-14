from rest_framework.viewsets import ModelViewSet
from .serializers import (
    Car, CarSerializer,
    Reservation, ReservationSerializer,
)

# ------------------------------------
# Fix View
# ------------------------------------

class FixView(ModelViewSet):
    pass

# ------------------------------------
# Car View
# ------------------------------------

from .permissions import IsStaffOrReadOnly

class CarView(FixView):
    queryset = Car.objects.filter(availability=True)
    serializer_class = CarSerializer
    # custom permission
    permission_classes = [IsStaffOrReadOnly]

    # field'a gore custom permission'i da ozellestiriyoruz, GenericApiView get_queryset'i override ederek.
    # env\Lib\site-packages\rest_framework\generics.py
    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = Car.objects.all()
        else:
            queryset = super().get_queryset()

        # url query parametreleri gelmisse bunlari yakalamak    
        # Tarihe gore filtreleme:
        # http://127.0.0.1:8000/api/car?from=2023-06-14&to=2023-06-18
        start = self.request.query_params.get('from', None)
        end = self.request.query_params.get('to', None)

        # django object filter keywords
        # https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups
        # gte => Greater than or equal to
        # lte => Less than or equal to
        if start and end:
            '''
            not_available_car_ids =  Reservation.objects.filter(
                start_date__gte = start, 
                start_date__lte = end
            ).values_list('car_id', flat=True)

            # If flat is True, this will mean the returned results are single values, rather than one-tuples.
            
            # >>> Entry.objects.values_list("id").order_by("id")
            # <QuerySet[(1,), (2,), (3,), ...]>

            # >>> Entry.objects.values_list("id", flat=True).order_by("id")
            # <QuerySet [1, 2, 3, ...]>
            '''

            # AND ve OR kullanmak için Q parametresini kullabiliriz:
            from django.db.models import  Q
            not_available_car_ids = Reservation.objects.filter(
                (Q(start_date__gte=start) & Q(start_date__lte=end))
                |
                (Q(end_date__gte=start) & Q(end_date__lte=end))
            ).values_list('car_id', flat=True)

            queryset = queryset.exclude(id__in=not_available_car_ids)

        return queryset



# ------------------------------------
# Reservation View
# ------------------------------------

from .permissions import IsStaffOrOnlySelfObjects

class ReservationView(FixView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    # custom permission
    permission_classes = [IsStaffOrOnlySelfObjects]

    # field'a gore custom permission'i da ozellestiriyoruz, GenericApiView get_queryset'i override ederek.
    # env\Lib\site-packages\rest_framework\generics.py
    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset() # Eğer user.is_staff ise default veriyi göster. 
        else:
            return Reservation.objects.filter(user=self.request.user) # Sadece kendi objelerini görsün.
    
    # def get_serializer_context(self):
    #     return {'request': self.request}

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)