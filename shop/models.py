from django.db import models
import datetime 

#Category , customer , product , order 
# Create your models here.
  
class Category(models.Model):
  name = models.CharField(max_length=50)
  
  def __str__(self):
    return self.name
   
  
class Customer(models.Model):
  firstName = models.CharField (max_length=50)
  lastName = models.CharField (max_length=50)
  email = models.EmailField(max_length=80)
  password = models.CharField(max_length=50)
  
  def __str__(self):
    return f'{self.firstName} {self.lastName}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2,max_digits=7,default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default = 1) # to reference the category model 
    description = models.CharField(max_length=350 , default='' , blank= True)
    image = models.ImageField(upload_to='uploads/product')
    
    #add sale
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(decimal_places=2,max_digits=7,default=0)
    
    def __str__(self):
      return self.name
    
class Order (models.Model) : 
  product = models.ForeignKey(Product , on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)
  customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
  date = models.DateTimeField(default = datetime.datetime.today)
  status = models.BooleanField(default=False)
  
  def __str__(self):
    return f'{self.product}'
  