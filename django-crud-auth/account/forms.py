from django.contrib.auth.forms import (
    AuthenticationForm,
    BaseUserCreationForm,
    UserCreationForm,
    SetPasswordForm,
    PasswordChangeForm,
    ValidationError,
)
from django.forms import widgets
from django.contrib import messages
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User


# customizing AuthenticationForm
class LoginForm(AuthenticationForm):
    next = forms.CharField(required=False, widget=forms.HiddenInput())

    # inherit edilen AuthenticationForm __init__ override'i
    def __init__(self, request=None, *args, **kwargs):
        # super(LoginForm, self).__init__(request=request, *args, **kwargs) # Python 2
        super().__init__(request=request, *args, **kwargs)  # Python 3
        self.fields["next"].initial = request.GET.get("next", "")
        print(f"==>> self.fields['next'].initial: {self.fields['next'].initial}")
        self.fields["username"].widget = widgets.TextInput(
            attrs={"class": "form-control"}
        )
        self.fields["password"].widget = widgets.PasswordInput(
            attrs={"class": "form-control"}
        )

    # form seviyesinde dogrulama icin inherit edilen AuthenticationForm clean override'i(nasil override edilecegini gostermek icin, bir islem yapilmayacak)
    def clean(self):
        super().clean()
        # islemler
        return self.cleaned_data

    # username field'i icin ekstra dogrulama ekleme
    def clean_username(self):
        username = self.cleaned_data.get("username")
        print(f"==>> username from LoginForm clean_username: {username}")

        if username == "admin":
            messages.success(self.request, "Hosgeldin Admin!")
        return username

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if user.username.startswith("banned"):
            # django.forms.ValidationError ile django.core.exceptions.ValidationError ayni method'tur. env\Lib\site-packages\django\core\exceptions.py
            raise forms.ValidationError("bu kullanici adiyla login olunamaz.")
            # raise ValidationError("bu kullanici adiyla login olunamaz.")


# customizing UserCreationForm
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(
            attrs={"class": "form-control"}
        )
        self.fields["email"].widget = widgets.EmailInput(
            attrs={"class": "form-control"}
        )
        self.fields["email"].required = True
        self.fields["first_name"].widget = widgets.TextInput(
            attrs={"class": "form-control"}
        )
        self.fields["first_name"].required = True
        self.fields["last_name"].widget = widgets.TextInput(
            attrs={"class": "form-control"}
        )
        self.fields["last_name"].required = True
        self.fields["password1"].widget = widgets.PasswordInput(
            attrs={"class": "form-control"}
        )
        self.fields["password2"].widget = widgets.PasswordInput(
            attrs={"class": "form-control"}
        )

    # email'in clean_<field_name> ile unique olmasini saglama
    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            self.add_error(
                "email", f"{email} baska bir kullanici tarafindan kullanimdadir."
            )

        return email


# customizing PasswordChangeForm
class PwChangeForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.fields["old_password"].widget = widgets.PasswordInput(
            attrs={"class": "form-control"}
        )
        self.fields["new_password1"].widget = widgets.PasswordInput(
            attrs={"class": "form-control"}
        )
        self.fields["new_password2"].widget = widgets.PasswordInput(
            attrs={"class": "form-control"}
        )
