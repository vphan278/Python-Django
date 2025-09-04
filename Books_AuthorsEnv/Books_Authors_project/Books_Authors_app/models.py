from django.db import models

class Item(models.Model):
    # attributes
    item_name = models.CharField(max_length=55)
    
    publisher = models.ForeignKey('Author', related_name="items", on_delete= models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#popcorn = Item.objects.create(
#    item_name = 'Butter popcorn',
#    description = 'Butter overload',
#    size = 'XL',
#    quantity = 1,
#    price = 19.99
#)

# all_items = Item.objects.all()

class Author(models.Model):

    name = models.CharField(max_length=55)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
