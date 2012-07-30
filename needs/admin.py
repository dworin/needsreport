from django.contrib import admin
from needs.models import Need, Category

class NeedAdmin(admin.ModelAdmin):
	list_display = ('sourcetype', 'source', 'category', 'countrycode', 'needtext')


admin.site.register(Need, NeedAdmin)
admin.site.register(Category)

