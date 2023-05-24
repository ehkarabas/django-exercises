from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    PassengerView,
    FlightView,
    ReservationView
)

urlpatterns = [
]

# ---------- Router ----------

router = DefaultRouter()
# hepsini kaplayan url'ler altta yer almali, aksi halde diger url'ler calismaz.
# ./ url'si ./someOtherUrlPart url'sini kapsayacagindan altinda yer almalidir.
router.register('passenger', PassengerView)
router.register('flight', FlightView)
router.register('reservation', ReservationView)

urlpatterns += router.urls
