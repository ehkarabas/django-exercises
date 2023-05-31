from django.urls import path
from rest_framework.routers import DefaultRouter # DefaultRouter ViewSet'lerle birlikte calisir, Generic Api View'ler icin siradan path yapisi kullanilmalidir.
from .views import DepartmentListCreateView, DepartmentRUDView, PersonnelListCreateView, PersonnelRUDView, DepartmentPersonnelView

urlpatterns = [
    path('departments/', DepartmentListCreateView.as_view()),
    path('departments/<int:pk>', DepartmentRUDView.as_view()),
    path('personnels/', PersonnelListCreateView.as_view()),
    path('personnels/<int:pk>', PersonnelRUDView.as_view()),
    # path('department-personnels/', DepartmentPersonnelView.as_view()),
    path('department/<str:department>', DepartmentPersonnelView.as_view()),
]

# router = DefaultRouter()
# # hepsini kaplayan url'ler altta yer almali, aksi halde diger url'ler calismaz.
# # ./ url'si ./someOtherUrlPart url'sini kapsayacagindan altinda yer almalidir.
# router.register('departments', DepartmentListCreateView) # DefaultRouter ViewSet'lerle birlikte calisir, Generic Api View'ler icin siradan path yapisi kullanilmalidir.

# urlpatterns += router.urls