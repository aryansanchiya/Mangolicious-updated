from django.contrib import admin

# Register your models here.
from .models import BuyNow,Details,Cod,RipeMangoes

# admin.site.register(Details)
admin.site.register(BuyNow)
admin.site.register(RipeMangoes)



@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ('email','name','Mo_No','quant','city','address','typeofmangoes')
    list_filter = ('name','city')
    search_fields = ('name','city')

@admin.register(Cod)
class CodAdmin(admin.ModelAdmin):
    list_display = ('email','name','Mo_No','quant','city','address','typeofmangoes')
    list_filter = ('name','city')
    search_fields = ('name','city')
