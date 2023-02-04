from django.contrib import admin

from app.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'image')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
    list_max_show_all = 100
    save_on_top = True
    save_as = True
    save_as_continue = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'price', 'image', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'slug', 'category__name')
    prepopulated_fields = {'slug': ('name',)}
    autocomplete_fields = ('category',)
    list_per_page = 20
    list_max_show_all = 100
    list_editable = ('price',)
    save_on_top = True
    save_as = True
    save_as_continue = True
    list_select_related = ('category',)
    list_display_links = ('id', 'name')
