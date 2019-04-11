from django.db import models

class Solution(models.Model):
    rank=models.CharField(max_length=254)
    solution=models.CharField(max_length=254)
    sector=models.CharField(max_length=254)
    co2_reduction=models.CharField(help_text="TOTAL ATMOSPHERIC CO2-EQ REDUCTION (GT)", max_length=254)

    # eleventh hour making of models to put an actual chart in the talk
    net_cost=models.CharField(max_length=254, help_text="Net Cost (BILLIONS US $)")
    # net_cost=models.DecimalField(help_text="Net Cost (BILLIONS US $)", max_digits=1024, decimal_places=2)
    savings=models.CharField(max_length=254, help_text="BILLIONS US $")
    # savings=models.DecimalField(help_text='BILLIONS US $', max_digits=1024, decimal_places=2)