from django.contrib import admin
from krypton_products.models import KryptonProduct
# Register your models here.


@admin.register(KryptonProduct)
class KryptonProductAdmin(admin.ModelAdmin):
    exclude = ('creation_date',)


# admin.site.register(KryptonProduct)
