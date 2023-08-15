from django.contrib import admin
from ders.models import Tanit, Card


# Register your models here.
class TanitAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    list_filter = ['title', 'image']
    list_display_links = ['title', 'image']

    class Meta:
        model = Tanit


admin.site.register(Tanit, TanitAdmin)


class CardAdmin(admin.ModelAdmin):
    list_display = ["title", "image"]
    list_display_links = ["title", "image"]

    class Meta:
        model = Card


admin.site.register(Card, CardAdmin)
