from django.contrib import admin
from unfold.admin import ModelAdmin
from pos import models


# Register your models here.
class OrderLineinLine(admin.TabularInline):
    model = models.OrderLine
    extra = 1
    readonly_fields = ('subtotal','price',)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        field = super().formfield_for_foreignkey(db_field, request, **kwargs)
        print(db_field.name)
        if db_field.name == 'product':
            print(field.widget)
            field.widget.can_add_related = False
            field.widget.can_change_related = False
            field.widget.can_delete_related = False
            field.widget.can_view_related = False
        return field

@admin.register(models.Order)
class OrderAdmin(ModelAdmin):
    inlines = [OrderLineinLine]
    readonly_fields = ('total','invoice_number')

@admin.register(models.Product)
class ProductAdmin(ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)

@admin.register(models.Customer)
class CustomerAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(models.StockIn)
class StockInAdmin(ModelAdmin):
    list_display = ('product','quantity','status')
    pass

@admin.register(models.StockOut)
class StockOutAdmin(ModelAdmin):
    pass