from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class SavedRecommendation(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        # related_name='owner_recommendations'
        )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        # related_name='product_recommendations'
    )
    