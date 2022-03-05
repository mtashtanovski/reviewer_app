from django.contrib import admin

# Register your models here.
from webapp.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'description']
    list_filter = ['title']
    search_fields = ['title']
    fields = ['title', 'category', 'description', 'picture']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'review_text', 'grade', 'moderated', 'created' ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
