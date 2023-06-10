from django.contrib import admin
from .models import Product, Review, Category
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from import_export import resources
from import_export.admin import ImportExportModelAdmin

admin.site.site_title = 'CoolDev Title'
admin.site.site_header = 'CoolDev Header'
admin.site.index_title = 'CoolDev Index Page'

# ------------------------------------------------
# Product Admin Panel Customization

# Foreign key table instance'inda iliski kurulan table row'larina ait goruntuleme formati tanimlama
# admin.TabularInline inherit edilerek class tanimlamasi yapilir
class ReviewInline(admin.TabularInline):  # Alternatif: StackedInline (farklı görünüm aynı iş)
    model = Review # Model
    extra = 1 # Yeni ekleme için ekstra boş alan
    classes = ['collapse'] # Görüntüleme tipi (default: tanımsız)

# Import-Export ModelResource:
class ProductModelResource(resources.ModelResource): # Import-Export ModelResource:
    class Meta:
        model = Product


# ImportExportModelAdmin => admin.ModelAdmin inherit edilerek olusturulmus bir class'tir
class ProductModelAdmin(ImportExportModelAdmin):
    # site'a click(sites.py) > def register > ModelAdmin click(django.contrib.admin.options.ModelAdmin) field'lari override ediliyor
    # ? list_display'deki ilk öğe (sütun), list_editable içinde belirtilirse bir hata alırsınız. Bu, Django'nun list_display_links için varsayılan değeri list_display'deki ilk öğe olduğu için kaynaklanır.
    # Tablo sutunları:
    list_display = ["id", "name","is_in_stock","create_date","update_date",]
    # Tablo üzerinde güncelleyebilme:
    list_editable = ["is_in_stock"]
    # Kayda gitmek icin linkleme:
    list_display_links = ["id",'name']
    # Filtreleme (arama değil):
    list_filter = [('name', DropdownFilter), "is_in_stock",('create_date', DateRangeFilter), ('update_date', DateTimeRangeFilter)]
    # Arama:
    search_fields = ['id', 'name']
    # Default siralama()
    # site'a click(sites.py) > def register > ModelAdmin'in inherit edildigi BaseModelAdmin field'i ordering override ediliyor
    ordering = ['-create_date','-id']
    # Sayfa basina kayit sayisi:
    list_per_page = 20
    # Arama bilgilendirme yazısı: 
    search_help_text = 'Arama yapmak için burayı kullanabilirsiniz.'
    # SEO uyumlu URL yapisinda(kucuk harf ve bosluklar dash(-)) otomatik kayıt oluştur:
    # site'a click(sites.py) > def register > ModelAdmin'in inherit edildigi BaseModelAdmin field'i prepopulated_fields override ediliyor
    prepopulated_fields = {'slug' : ['name']}
    # Tarihe göre filtreleme başlığı(bar'i):
    date_hierarchy = 'create_date'
    # Form layout degisikligi(basic seviye):
    # site'a click(sites.py) > def register > ModelAdmin'in inherit edildigi BaseModelAdmin field'i fields override ediliyor
    # fields = (
    #     ('name', 'is_in_stock'),
    #     ('slug'),
    #     ('description')
    # )
    # Instance'lar icin form layout degisikligi(ileri seviye):
    # site'a click(sites.py) > def register > ModelAdmin'in inherit edildigi BaseModelAdmin field'i fieldsets override ediliyor

    # site'a click(sites.py) > def register > ModelAdmin'in inherit edildigi BaseModelAdmin field'i readonly_fields override ediliyor
    # Instance'ta resim gosterme(read_only olarak cagir):
    readonly_fields = ["view_image"] 

    fieldsets = ( 
        (
            'General Settings', {
                "classes": ("wide",),
                "fields": (
                    ('name', 'slug'),
                    ("image", "view_image"),
                    "is_in_stock",
                    "categories",
                ),
            }
        ),
        (
            'Optionals Settings', {
                "classes": ("collapse",),
                "fields": (
                    "description",
                    ),
                'description': "You can use this section for optionals settings"
            }
        ),
    )

    # İlişkili tablo (many2many) nasıl görünsün:
    # site'a click(sites.py) > def register > ModelAdmin'in inherit edildigi BaseModelAdmin field'lari filter_horizontal ve filter_vertical override ediliyor
    filter_horizontal = ["categories"] # Yatay Görünüm
    # filter_vertical = ["categories"] # Dikey Görünüm

    # Iliskili table'daki row'lari goruntuleme:
    inlines = [ReviewInline]

    # Import Export:
    resource_class = ProductModelResource

    # Action tanimlama:
    def set_stock_in(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f'{count} adet "Stokta Var" olarak işaretlendi.')
    

    def set_stock_out(self, request, queryset):
        count = queryset.update(is_in_stock=False)
        self.message_user(request, f'{count} adet "Stokta Yok" olarak işaretlendi.')

    # ModelAdmin actions override ediliyor
    actions = ('set_stock_in', 'set_stock_out')
    # action select'inin option'lari degistiriliyor
    set_stock_in.short_description = 'İşaretli ürünleri stoğa ekle'
    set_stock_out.short_description = 'İşaretli ürünleri stoktan çıkar'

    # model'de olmayan bir field'i eklemek(serializer'larda oldugu gibi basina get_ eklemek zorunlu degildir) => serializer'lardaki karsiligi serializerMethodField get_serializerMethodFieldVariableName return'u
    def added_days_ago(self, object):
        from django.utils import timezone
        different = timezone.now() - object.create_date
        return different.days
    
    # Tablo sutunları:
    list_display += ["added_days_ago"]

    # Kaçtane yorum var:
    def how_many_reviews(self, object):
        count = object.reviews.count()
        return count

    list_display += ['how_many_reviews']
    
    # Listede küçük resim göster:
    def view_image_in_list(self, obj):
        from django.utils.safestring import mark_safe
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} style="height:30px; width:30px;"></img>')
        return '-*-'
    
    list_display = ['view_image_in_list'] + list_display
    view_image_in_list.short_description = 'IMAGE' # listedeki sutun adi'nin kisaltilmasi
    


# Register your models here.
# site'a click(sites.py) > def register :
admin.site.register(Product, ProductModelAdmin) # def register(self, model_or_iterable, admin_class=None, **options):
# ------------------------------------------------


# ------------------------------------------------
# Review Admin Panel Customization

class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_filter = [('product', RelatedDropdownFilter)]
    list_per_page = 50
    # raw_id_fields = ('product',) 

# Register your models here.
# site'a click(sites.py) > def register :
admin.site.register(Review, ReviewModelAdmin) # def register(self, model_or_iterable, admin_class=None, **options):

# ------------------------------------------------
# Catehgory Admin Panel 

admin.site.register(Category)

# ------------------------------------------------



