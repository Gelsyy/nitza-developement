from django.contrib import admin

from .models import (
    Product,
    Stock,
    Unit,
    ProductTransaction,
    InventoryLocations,
    ProductCategory,
    PriceReference,
    ProductKit,
    KitElement,
    DocumentCategory
)




admin.site.register(Product)
admin.site.register(Unit)
admin.site.register(ProductTransaction)
admin.site.register(InventoryLocations)
admin.site.register(ProductCategory)
admin.site.register(Stock)
admin.site.register(PriceReference)
admin.site.register(ProductKit)
admin.site.register(KitElement)

class DocumentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

    def has_change_permission(self, request, obj=None):
        return request.user.has_perm('yourapp.change_documentcategory')

    def has_delete_permission(self, request, obj=None):
        return request.user.has_perm('yourapp.delete_documentcategory')

admin.site.register(DocumentCategory, DocumentCategoryAdmin)