from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("slug",)
        # model field'larina ait formdaki label'larin ozellestirilmesi
        labels = {
            "name": "Urun Adi",
            "price": "Urun Fiyati",
            "description": "Urun Bilgisi",
            "image": "Image Dosyasi",
            "isActive": "Aktif mi?",
            "categories": "Kategoriler",
            "supplier": "Tedarikci",
        }
        # model field'larina ait form elementlerinin class'larinin belirlenmesi(ozellikle bootstrap gibi kutuphaneler icin)
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "isActive": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "categories": forms.SelectMultiple(
                attrs={
                    "class": "form-select",
                    "multiple": "True",  # SelectMultiple aslinda default olarak multiple eklenmis halde HTML ciktisi uretir.
                }
            ),
            "supplier": forms.Select(attrs={"class": "form-select"}),
        }
        # model field'larina ait formdaki hata mesajlarini tanimlama, fieldName dict'lerindeki her key, model field'indaki kisitlama saglayan option'lardir.
        error_messages = {
            "name": {
                "required": "Urun Adi gerekli bir alandir.",
                "min_length": "Min 3 karakter giriniz",
                "max_length": "Max 20 karakter giriniz",
            },
            "price": {
                "required": "Urun Fiyati gerekli bir alandir.",
                "min_value": "Urun Fiyati 0'dan buyuk olmalidir.",
                "max_value": "Urun Fiyati 100.000'den kucuk olmalidir.",
            },
            "description": {
                "required": "Urun Bilgisi gerekli bir alandir.",
                "min_length": "Min 10 karakter giriniz",
                "max_length": "Max 200 karakter giriniz",
            },
            "image": {
                "required": "Image Dosyasi yuklenmelidir.",
            },
            "isActive": {
                "required": "Aktif mi? gerekli bir alandir.",
            },
            "categories": {
                "required": "Kategoriler gerekli bir alandir.",
            },
            "supplier": {
                "required": "Tedarikci gerekli bir alandir.",
            },
        }


class UploadForm(forms.Form):
    image = forms.FileField(
        label="Image:",
        widget=forms.ClearableFileInput(attrs={"class": "form-control"}),
    )  # herhangi bir dosya turunu kabul eder, buna resimler de dahil. Ancak ImageField yalnizca resim dosyalarini kabul eder.

    def clean_image(self):
        # self.files Django form sınıflarında özel bir anlama sahip bir yapıdır. Bu, request.FILES'tan gelen dosya verilerine bir referanstır ve Django'nun form işleme mekanizması tarafından sağlanır.
        file = self.files.get("image")
        print(f"==>> file: {file}")
        MAX_FILE_SIZE = 100 * 1024 * 1024  # 100 MB
        print(f"==>> file.size > MAX_FILE_SIZE: {file.size > MAX_FILE_SIZE}")
        if file.size > MAX_FILE_SIZE:
            raise forms.ValidationError(
                f"{file.name} - Dosya boyutu 100MB'dan buyuk olamaz"
            )
        return file


# class(pylance tanimi, aslinda instance) FormsFormVeyaFormsModelForm(
#         #     data: Mapping[str, Any] | None = ...,
#         #     files: Mapping[str, Any] | None = ...,
#         ...
#         # )
