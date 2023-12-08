from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from .forms import LoginForm, RegisterForm, PwChangeForm

# Gecis template'i yonlendirmeleri icin function tanimlama
def redirect_gate(request, path_name, is_next=False):
    print(f"==>> path_name: {path_name}")
    print(f"==>> is_next: {is_next}")
    print(f"==>> path_name if is_next else 'undefined': {path_name if is_next else "undefined"}")
    context = {
        "redirect_to": "undefined" if is_next else reverse(path_name),
        "redirect_to_next": path_name if is_next else "undefined",
    }
    return render(request, "redirect_message.html", context)


# Create your views here.
def login_request(request):
    if request.method == "POST":
        print(f"==>> request.POST: {request.POST}")
        # class AuthenticationForm(
        #     request: Any = ...,
        #     *args: Any,
        #     **kwargs: Any
        # )
        # The 'request' parameter is set for custom auth use by subclasses. The form data comes in via the standard 'data' kwarg.

        # form = AuthenticationForm(request, data=request.POST)
        # AuthenticationForm customize edilerek field'lara widgets.attrs ile class eklenmistir.
        form = LoginForm(request, data=request.POST)
        username = request.POST.get("username","") # yalnizca django message'lari icin

        if form.is_valid():
            username = form.cleaned_data.get("username") # yalnizca django message'lari icin, yoksa authenticate kullanilmadigindan gereksiz
            user = form.get_user()
            print(f"==>> user: {user}")

            login(request, user)

            next_url = request.POST.get("next", "")
            print(f"==>> next_url: {next_url}")
            if next_url == "":
                messages.success(request, f"{username} basariyla giris yapti.")
                return redirect_gate(request, "product_index")
            else:
                messages.success(request, f"{next_url} adresine artik erisebilirsiniz.")
                return redirect_gate(request, next_url, is_next=True)
        else:
            print(f"==>> form.errors: {form.errors}")
            messages.error(request, f"{username} icin girilen bilgiler hatali, eksik veya gecersiz formatta.")
            return render(request, "account/login.html", {"form": form})
    else:
        print(f"==>> request.GET: {request.GET}")
        form = LoginForm(request)
        return render(request, "account/login.html",{"form":form})


def register_request(request):
    if request.method == "POST":
        print(f"==>> request.POST: {request.POST}")
        # class UserCreationForm(
        #     *args: Any,
        #     **kwargs: Any
        # )
        # form = UserCreationForm(request.POST)
        form = RegisterForm(request.POST)
        username = request.POST.get("username", "") # django messages icin saklandi

        if form.is_valid():
            form.save() # django.contrib.auth.forms.BaseUserCreationForm save'de commit default True oldugu icin User instance'i olusturulacaktir.
            # register'dan sonra User instance'ini otomatik login etmek
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"] # custom UserCreationForm ile eklendi
            password = form.cleaned_data["password1"]
            
            user = authenticate(request,username=username,password=password,email=email)
            login(request,user)
            messages.success(request, f"{username} basariyla olusturuldu ve giris yapildi.")
            return redirect_gate(request,"product_index")
        else:
            print(f"==>> form.errors: {form.errors}")
            messages.error(request, f"{username} icin girilen bilgiler hatali, eksik veya gecersiz formatta.")
            return render(request,"account/register.html",{"form": form})
    else:
        form = RegisterForm()
        return render(request, "account/register.html",{"form":form})


def logout_request(request):
    messages.success(
        request,
        f"Hesaptan basariyla cikis yapildi.",
    )
    logout(request)
    return redirect("account_login")  

def change_password(request):
    # class PasswordChangeForm(
    #   user: AbstractBaseUser | None,
    #   *args: Any,
    #   **kwargs: Any
    # )
    # A form that lets a user change their password by entering their old password.
    if request.method == "POST":
        form = PwChangeForm(request.user, data=request.POST) # form element(field) bootstrap class'lari eklenmis custom PasswordChangeForm
        if form.is_valid():
            # PasswordChangeForm'un inherit edildigi SetPasswordForm'un save methodu:
            # def save(self, commit=True):
            #   password = self.cleaned_data["new_password1"]
            #   self.user.set_password(password)
            #   if commit:
            #       self.user.save()
            #   return self.user
            # form.save()
            user = form.save() 

            # (function) def update_session_auth_hash(
            #     request: HttpRequest,
            #     user: AbstractBaseUser
            # ) -> None
            # Updating a user's password logs out all sessions for the user.

            # Take the current request and the updated user object from which the new session hash will be derived and update the session hash appropriately to prevent a password change from logging out the session from which the password was changed.

            # update_session_auth_hash(request,request.user)
            update_session_auth_hash(request,user)
            messages.success(request,f"{request.user.username} sifresi basariyla degistirildi.")
            return redirect_gate(request,"product_index")
        else:
            print(f"==>> form.errors: {form.errors}")
            messages.error(request, f"{request.user.username} icin girilen parolalar hatali, eksik veya gecersiz formatta.")
            return render(request,"account/change_password.html",{"form": form})
    else:
        form = PwChangeForm(request.user)
        return render(request,"account/change_password.html",{"form":form})

