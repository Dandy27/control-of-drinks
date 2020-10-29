from django.contrib import admin
from .models import WeightConfig

admin.site.site_header = "Inventory control "

@admin.register(WeightConfig)
class WeightConfig(admin.ModelAdmin):
    list_display = ('name_product',
                 'weight_liquid',
                 'quantity_of_doses', 
                 'gross_bottle_weight', 
                 'tare', 
                 'weigh_bottle_and_liquid', 'calculo_doses')


