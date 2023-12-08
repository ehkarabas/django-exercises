from django.http import (
    Http404,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Product, UploadModel
from .forms import ProductForm, UploadForm

# import logging
# from django.template import loader, TemplateDoesNotExist

# logger = logging.getLogger(__name__)

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from account.views import redirect_gate


def index(request):
    products = Product.objects.filter(isActive=True).order_by("-price")

    context = {
        "products": products,
    }

    return render(request, "app1/index.html", context)


# (function) def render(
#     request: HttpRequest,
#     template_name: str | Sequence[str],
#     context: Mapping[str, Any] | None = ...,
#     content_type: str | None = ...,
#     status: int | None = ...,
#     using: str | None = ...
# ) -> HttpResponse


@login_required(login_url="/account/login")
def list_products_by_query(request):
    # print(request.GET)
    # print(request.GET["q"])

    # GET isteginde q query'si var mi, Django form ile tanimlandiysa bos gonderildiginde None olacagi icin ek olarak q'nun None olmamasi da gerekecektir.
    # if "q" in request.GET and request.GET["q"] is not None: # square bracket access kullanilirsa key yoksa MultiValueDictKeyError verir. bunun icin get kullanilarak erisim saglanirsa hata vermek yerine None dondurur.
    print(f"==>> request.GET.get('q'): {request.GET.get("q")}")
    print(f"==>> request.GET: {request.GET}")
    if  "q" in request.GET and request.GET.get("q") is not None:
        q = request.GET["q"]
        products = Product.objects.filter(name__contains=q).order_by("-price")
        print(products)
    else:
        # url = reverse("index")
        # return HttpResponseRedirect(url)
        # return redirect("index")
        products = Product.objects.all().order_by("-price")
        print(f"==>> products: {products}")

    context = {
        "products": products,
    }

    return render(request, "app1/list.html", context)

@login_required(login_url="/account/login")
def create(request):
    create_template_static_path = "app1/create.html"
    # try:
    #     template = loader.get_template('form_snippet.html')
    #     template_path = template.origin.name
    #     logger.debug('Şablonun tam yolu: %s', template_path)
    #     print('Şablonun tam yolu:', template_path)
    # except TemplateDoesNotExist:
    #     logger.error('Şablon bulunamadı')
    #     print('Şablon bulunamadı')
    if request.method == "POST":
        print(f"==>> request.POST: {request.POST}")
        print(f"==>> request.FILES: {request.FILES}")
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            product_name = form.cleaned_data['name']
            messages.success(request, f"{product_name} basariyla olusturuldu.")
            return render(request, "redirect_message.html", {"redirect_to": "list_products_by_query"})
    else: 
        form = ProductForm()
    return render(request,create_template_static_path,{"product_create_form":form})

def edit(request, id):
    product = get_object_or_404(Product, pk=id)
    print(reverse('edit_product',kwargs={"id":id})) 

    if request.method == "POST": 
        form = ProductForm(request.POST, request.FILES, instance=product)
        
        if form.is_valid():
            print(f"==>> request.POST: {request.POST}")
            print(f"==>> request.FILES: {request.FILES}")
            form.save()
            messages.success(request, f"{product.name} basariyla guncellendi.")
            return render(request, "redirect_message.html", {"redirect_to": "list_products_by_query"})
    else:
        form = ProductForm(instance=product)

    return render(request,"app1/edit.html",{"form":form})

def delete(request,id):
    product = get_object_or_404(Product,pk=id)

    if request.method == "POST":
        product_name = product.name
        product.delete()
        messages.success(request, f"{product_name} basariyla silindi.")
        return render(request, "redirect_message.html", {"redirect_to": "list_products_by_query"})

    return render(request, "app1/delete_confirm.html", {"product":product})

def upload(request):
    if request.method == "POST":
        print(f"==>> request.FILES: {request.FILES}")
        print(f"==>> request.POST: {request.POST}") 

        form = UploadForm(request.POST, request.FILES)
        error_occurred = False
        image = request.FILES.get("image")

        if form.is_valid():
            print(f"==>> image: {image}")
            
            image_file_name = image.name
            print(f"==>> image_file_name: {image_file_name}")

            file_size_in_mb = image.size / (1024 * 1024)  # Bayttan MB'ye çevirme
            file_size_in_mb = round(file_size_in_mb, 2)  # İki ondalık basamağa yuvarlama
            print(f"==>> file_size_in_mb: {file_size_in_mb}")

            messages.success(request, f"{image_file_name} dosyasi basariyla yuklendi.({file_size_in_mb} MB)")
        else:
            for field, errors in form.errors.items():
              for error in errors:
                  print(f"==>> error: {error}")
                  messages.error(request, f"{field}: {error}")
        
        for message in messages.get_messages(request):
            if message.level == messages.ERROR:
                error_occurred = True
                break

        if error_occurred:
            return render(request, "redirect_message.html", {"redirect_to": "upload_image"})
        else:
            model = UploadModel(image=image)
            model.save()
            return render(request, "redirect_message.html", {"redirect_to": "product_index"})
    
    else:
        form = UploadForm()
    return render(request, "app1/upload.html", {'form': form})

# def handle_uploaded_file(file):
#     number = random.randint(10000,99999)
#     file_name, file_extension = os.path.splitext(file.name)
#     # os.path.splitext() => pathlike string'in uzantisini ayirir, (pathlikeStringWithoutExtension,extensionDotDahil)
#     name = file_name + f"_{number}" + f"{file_extension}"
#     with open("temp/" + name, "wb+") as destination:
#         for chunk in file.chunks(): # Django'da yüklenen dosyaları işlerken kullanılan chunks() metodu, dosyayı tek tek byte olarak değil, birden fazla byte'lık gruplar (chunks) halinde işler.
#             destination.write(chunk)

def getProductsByProductNameSlug(request, product_name_slug):
    product = get_object_or_404(Product, slug=product_name_slug)
    context = {"product": product}
    return render(request, "app1/product.html", context)


# def details(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     context = {"product": product}
#     return render(request, "app1/details.html", context)


