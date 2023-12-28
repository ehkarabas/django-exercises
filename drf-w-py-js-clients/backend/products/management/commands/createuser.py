from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Yeni bir kullanıcı oluşturur"

    def add_arguments(self, parser):
        parser.add_argument("username", type=str, help="Kullanıcı adı")
        parser.add_argument(
            "--email", type=str, help="E-posta adresi (opsiyonel)", default=None
        )
        parser.add_argument("password", type=str, help="Şifre")

    def handle(self, *args, **kwargs):
        username = kwargs["username"]
        email = kwargs.get("email")
        password = kwargs["password"]

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'"{username}" adında bir kullanıcı zaten var')
            )
            return

        if email and User.objects.filter(email=email).exists():
            self.stdout.write(
                self.style.WARNING(
                    f'"{email}" e-posta adresi başka bir kullanıcı tarafından kullanılıyor'
                )
            )
            return

        User.objects.create_user(username, email, password)
        self.stdout.write(
            self.style.SUCCESS(f'"{username}" adında kullanıcı başarıyla oluşturuldu')
        )
