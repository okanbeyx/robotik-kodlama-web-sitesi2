from django.contrib import admin
from ders.models import Tanit, Card, Yazi


# Register your models here.
class TanitAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    list_filter = ['title', 'image']
    list_display_links = ['title', 'image']

    class Meta:
        model = Tanit


admin.site.register(Tanit, TanitAdmin)


class CardAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    list_display_links = ['title', 'image']

    class Meta:
        model = Card


admin.site.register(Card, CardAdmin)


class YaziAdmin(admin.ModelAdmin):
    list_display = ['text']
    list_display_links = ['text']

    class Meta:
        model = Yazi


admin.site.register(Yazi, YaziAdmin)
