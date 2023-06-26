from django.shortcuts import render

# Create your views here.

# --------------------------------------------------------
# USER LOGIN/LOGOUT
# --------------------------------------------------------

"""
# env\Lib\site-packages\django\contrib\auth\views.py
Overriding next_page to redirect after success
def get_default_redirect_url(self):
        if self.next_page:
            return resolve_url(self.next_page)
        else:
            return resolve_url(settings.LOGIN_REDIRECT_URL)
"""

"""
# env\Lib\site-packages\django\contrib\auth\views.py
from django.contrib.auth.views import LoginView
class UserLoginView(LoginView):
    template_name = 'user/user_form.html'
    next_page = 'user_login'

from django.contrib.auth.views import LogoutView

class UserLogoutView(LogoutView):
    template_name = 'user/user_form.html'
    next_page = 'user_login'
"""

# REDIRECT_URL_PATHNAME = 'user_login'
REDIRECT_URL_PATHNAME = 'home'

class FixView:
    template_name = 'user/user_form.html'
    # next_page = 'user_login'
    next_page = REDIRECT_URL_PATHNAME

# USING DJANGO BUILT-IN AUTH

# env\Lib\site-packages\django\contrib\auth\views.py
from django.contrib.auth.views import LoginView

class UserLoginView(FixView, LoginView):
    extra_context = {'title': 'Login'} # Sayfa Başlık

from django.contrib.auth.views import LogoutView

class UserLogoutView(FixView, LogoutView):
    pass

"""
Django Rest Auth ile Django'nun dahili auth sistemi farkli calisir, bu iki sistemin farklı çalışma şekli, oturum (session) yönetimi ve oturum (session) süresi gibi konularda farklı yaklaşımlar sergilemelerinden kaynaklanıyor.

Django rest auth, RESTful API tasarım prensiplerini benimser ve genellikle durumsuz (stateless) olma prensibini izler. Bu, her bir isteğin (request) bağımsız olduğu ve önceki veya sonraki isteklerden bilgi taşımadığı anlamına gelir. Bu nedenle, bir kullanıcı oturum bilgilerini her istekte tekrar göndermek zorunda kalır.

Öte yandan, Django'nun dahili kimlik doğrulama sistemini (django.contrib.auth.views) kullandığınızda, oturum bilgileri sunucuda saklanır ve oturum süresince kullanıcının kimliği hatırlanır. Bu, bir kullanıcının oturumu açtıktan sonra başka bir sayfaya gitse bile kimlik bilgilerini korumasını sağlar.

Admin panel hakkında bahsettiğiniz durum, oturum yönetiminin nasıl çalıştığının bir örneği. Bir kullanıcı giriş yaptığında, kimlik bilgileri oturumda saklanır ve daha sonraki isteklerde kullanılır. Bu, kullanıcının admin paneline erişmeye çalıştığında, oturum bilgileri hala geçerli olduğu için "yetkisiz bu kullanıcı" uyarısını almasına neden olur. Çünkü Django, kullanıcının kim olduğunu hatırlar, ancak bu kullanıcının admin paneline erişim yetkisi olmadığını bilir. Bu durumda, kullanıcının logout olması ve gerektiğinde yetkili bir kullanıcı ile yeniden giriş yapması gerekmektedir.

Her iki sistem de farklı durumlar ve ihtiyaçlar için uygun olabilir. Birisi durumsuz bir API istiyorsa, Django rest auth kullanabilir. Ancak bir web sitesinde kullanıcıların giriş yaptıktan sonra kimliklerini korumasını istiyorsa, Django'nun dahili kimlik doğrulama sistemini kullanabilir.
"""

# --------------------------------------------------------
# USER REGISTRATION
# --------------------------------------------------------

from django.views.generic import CreateView # built-in class view
# env\Lib\site-packages\django\contrib\auth\forms.py
from django.contrib.auth.forms import UserCreationForm # built-in user creation form(admin panel de kullanir)
from django.urls import reverse_lazy

REDIRECT_URL_PATHNAME = 'user_login'

class UserCreateView(FixView, CreateView):
    extra_context = {'title': 'Register'} # Sayfa Başlık
    form_class = UserCreationForm
    # success_url = reverse_lazy('user_login')
    # success_url = reverse_lazy(FixView.next_page)
    success_url = reverse_lazy(REDIRECT_URL_PATHNAME)

    """
    # env\Lib\site-packages\django\views\generic\edit.py
    def get_success_url(self):
        if not self.success_url:
            raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
        return str(self.success_url)  # success_url may be lazy
    """

    # Overriding get_success_url in FormMixin (CreateView > BaseCreateView > ModelFormMixin > FormMixin get_success_url) to login after successful request
    # Login after registration:
    def get_success_url(self):
        from django.contrib.auth import login

        login(self.request, self.object)
        return super().get_success_url()
    
"""
Email adresi eklenmis user creation form customization'i 1. alternatif:

forms.py:

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreateFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateFormWithEmail, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
"""

"""
Email adresi ve extra field'lar eklenmis user creation form customization'i 2. alternatif:

forms.py:

from django import forms

from django.contrib.auth.forms import UserCreationForm
class CustomUserCreationForm(UserCreationForm):

    extra_field = forms.CharField(max_length=128, required=False)

    class Meta(UserCreationForm.Meta):
        fields = (
            'email',
            'username',
            'password',
            'password2',
            'first_name',
            'last_name',
            'extra_field',
        )
"""