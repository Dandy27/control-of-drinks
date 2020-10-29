from django.db import models

class WeightConfig(models.Model):
    name_product = models.CharField(max_length=100)
    weight_liquid = models.DecimalField(max_digits=6, decimal_places=1, help_text='GRS')
    quantity_of_doses = models.DecimalField(max_digits=6, decimal_places=1, help_text='QUANT')
    gross_bottle_weight = models.DecimalField(max_digits=6, decimal_places=1, help_text='GRS')
    tare = models.DecimalField(max_digits=6, decimal_places=1, help_text='GRS')
    weigh_bottle_and_liquid = models.DecimalField(max_digits=6, decimal_places=1, help_text='Barman')
    

    def calculo_doses(self):

        calc = (self.weigh_bottle_and_liquid - self.tare) * self.quantity_of_doses / (self.gross_bottle_weight - self.tare )
        if  self.weigh_bottle_and_liquid < (self.gross_bottle_weight - self.weight_liquid):
            return ('"ERROR" value less than tare')
        else:
            return calc 
    

    def __str__(self):
        return self.name_product
