from django.db import models

# importing the User model
from django.contrib.auth.models import User 

# import cart model from mainapp
from Book.models import Comic

# Create your models here.
class CartItem(models.Model):
    comic = models.ForeignKey(Comic, on_delete= models.CASCADE)
    # Foreign key(product_id) references mainapp_comic(id) on delete cascade

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default= 0)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username.capitalize()} added {self.comic.name} to cart!!!"
    
    def sub_total(self):
        return self.quantity * self.comic.price 