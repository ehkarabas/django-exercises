from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
# ------------------------------------------------
# Function Based Views
# ------------------------------------------------

# env\Lib\site-packages\django\contrib\auth\decorators.py
# function based view'larda bir sayfaya erisim icin login gerektirme => login_required decorator
# istenilen url'e yonlendirmek icin login_url agumani kullanilmalidir.

# from django.contrib.auth.decorators import login_required

# @login_required(login_url='user_login') # default login_url = accounts/login/
def home(request):
    from .models import Pizza

    pizzas = Pizza.objects.all()
    context = {
        'pizzas' : pizzas
    }

    return render(request, 'home.html', context)

# ------------------------------------------------
# Class Based Views
# ------------------------------------------------

from django.views.generic import (
    # generic display
    ListView,
    DetailView,
    # generic editing
    CreateView,
    UpdateView,
    DeleteView,
)

# env\Lib\site-packages\django\contrib\auth\mixins.py
# class based view'larda bir sayfaya erisim icin login gerektirme => LoginRequiredMixin
# istenilen url'e yonlendirmek icin LoginRequiredMixin > AccessMixin login_url override edilmelidir.

from django.contrib.auth.mixins import LoginRequiredMixin

class FixView(LoginRequiredMixin):
    from .forms import OrderForm
    from .models import Order
    from django.urls import reverse_lazy

    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order_list')

    # LoginRequiredMixin > AccessMixin login_url override ediliyor
    login_url = 'user_login'

    # env\Lib\site-packages\django\views\generic\list.py
    # MultipleObjectMixin get_queryset override ediliyor, yalnizca o an login olmus user'a ait instance'larin dondurulmesi icin

    def get_queryset(self):
        from .models import Order

        return Order.objects.filter(user=self.request.user).order_by('-id')

# List:
class OrderListView(FixView, ListView):
    template_name = 'pizza/order_list.html'
    context_object_name = 'orders' # default => object_list
    # ordering = ['-id'] # FixView'de queryset get_queryset ile override edildigi icin, ordering get_queryset'te handle edildi.

# Detail:
class OrderDetailView(FixView, DetailView):
    template_name = 'pizza/order_detail.html'
    context_object_name = 'order'
    
# Create:
class OrderCreateView(FixView, CreateView):
    template_name = 'pizza/order_form.html'
    context_object_name = 'form'

    # Yeni kayıt sayfası için pizza bilgisi:
    # env\Lib\site-packages\django\views\generic\detail.py
    # CreateView > BaseCreateView > ModelFormMixin > SingleObjectMixin get_context_data override ediliyor
    def get_context_data(self, **kwargs):
        from .models import Pizza

        # Context dictionary'sini al:
        kwargs = super().get_context_data(**kwargs)
        # Url query'den pizza id bilgisini cek ve pizza_id'ye ata:
        pizza_id = self.request.GET.get('pizza', 0)
        # Context'e pizza key'i ile ilgili pizza instance'ini value olarak ekle
        # kwargs['pizza'] = Pizza.objects.get(id=pizza_id)
        kwargs['pizza'] = Pizza.objects.filter(id=pizza_id).first()
        return kwargs

    # Order olusturulurken request'ten user_id ve pizza_id'yi alip object'e kaydetme, field verileri otomatiklestiriliyor, boylece form'dan user ve pizza exclude edilebilir ve user'dan hataya yol acabilecek gereksiz bir input beklentisi olusmaz.
    # env\Lib\site-packages\django\views\generic\edit.py
    # CreateView > BaseCreateView > ModelFormMixin form_valid override ediliyor
    def form_valid(self, form):
        self.object = form.save(commit=False) # commit False ile veritabanina kayit yapmadan model instance'i olusturur. Modelde olup formda exclude edilen field'lar varsa, formda olan tum field'lar cekilmis olur, ilave islemlerle de modele kiyasla eksik olan veriler tamamlanip database'e kayit yapilir.
        # Objeye user_id ekle(kayitli kullanici):
        self.object.user_id = self.request.user.id
        # Objeye pizza_id ekle(kayitli kullanici):
        self.object.pizza_id = self.request.GET.get('pizza')
        self.object.save()
        return super().form_valid(form)

    # Mesaj gostermek icin post override ediliyor
    def post(self, request, *args, **kwargs):
        from django.contrib import messages

        # Mesaj göster:
        messages.success(request, 'Kaydedildi.')
        return super().post(request, *args, **kwargs)

# Update:
class OrderUpdateView(FixView, UpdateView):
    template_name = 'pizza/order_form.html'
    context_object_name = 'form'

    # Mesaj gostermek icin post override ediliyor
    def post(self, request, *args, **kwargs):
        from django.contrib import messages

        # Mesaj göster:
        messages.success(request, 'Güncellendi.')
        return super().post(request, *args, **kwargs)

# Delete:
class OrderDeleteView(FixView, DeleteView):
    # template_name = 'pizza/order_confirm_delete.html'
    # context_object_name = 'form'
    
    # NO TEMPLATE => SHOW MESSAGE THEN DELETE AND FINALLY REDIRECT ORDER LIST VIA FIXVIEW'S SUCCESS_URL
    # template dosyasina gitmeden direkt sil:
    def get(self, request, *args, **kwargs):
        from django.contrib import messages

        # Mesaj goster:
        messages.success(request, 'Silindi.')

        # Tekrar get yaparak template aramasina yol acmak yerine DeleteView > BaseDeleteView > DeletionMixin delete method'u kullaniliyor.
        return super().delete(request, *args, **kwargs)