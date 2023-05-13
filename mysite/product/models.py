from django.db import models
from django.conf import settings

class Element(models.Model):
    element_title = models.TextField("Наименование", max_length=500)
    element_dimension = models.CharField(max_length=500, blank=True, null=True)
    element_note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.element_title

class Product_type(models.Model):
    title = models.TextField(max_length=500)

class Product(models.Model):
    product_title = models.CharField(max_length=500)
    product_type = models.ForeignKey(Product_type, on_delete = models.CASCADE)
    product_fabrication = models.IntegerField()
    product_standard = models.IntegerField()
    product_note = models.TextField()
    elements = models.ManyToManyField(Element, through='Product_Element')

def __str__(self):
    return self.product_title

    def get_absolute_url(self):
            return reverse('product_list_url', kwargs={'id':self.id})

class Product_Element(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    quantity = models.FloatField(max_length=200)
