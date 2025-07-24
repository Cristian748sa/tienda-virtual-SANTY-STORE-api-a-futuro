import uuid
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)  
    has_discount = models.BooleanField(default=False)  # checkbox
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # porcentaje
    slug = models.SlugField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/', null=False, blank=False)

    def __str__(self):
        return self.title

    def final_price(self):  #  calcular precio final
        if self.has_discount:
            return self.price * (1 - self.discount / 100)
        return self.price


def set_slug(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        slug = slugify(instance.title)
        while Product.objects.filter(slug=slug).exists():
            slug = slugify(f"{instance.title}-{str(uuid.uuid4())[:8]}")
            print("Este es slug", slug)
        instance.slug = slug

pre_save.connect(set_slug, sender=Product)
