from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioAdmin(admin.ModelAdmin):
    fields = ['nombre']
    list_display = ('id','nombre')
    list_display_links = ['nombre']

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    ordering = ('nombre',)
    list_display_links = ['nombre','laboratorio']
    list_per_page = 2

class ProductoAdmin(admin.ModelAdmin):
    fields = ['nombre', 'laboratorio', 'f_fabricacion', 'p_costo','p_venta']
    list_display = ('id','nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    list_display_links = ['nombre', 'laboratorio']
    ordering = ('nombre','laboratorio')
    list_filter = ('nombre', 'laboratorio')

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)