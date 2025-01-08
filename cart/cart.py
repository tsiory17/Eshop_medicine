from shop.models import Product
class Cart ():
  def __init__(self,request):
    self.session = request.session
    
    cart = self.session.get('session_key')
    
    if 'session_key' not in request.session :
      cart = self.session['session_key'] = {}
      
    self.cart = cart 
    
  def add (self,product,quantity):
    product_id = str(product.id)
    product_quantity = str(quantity)
    
    if product_id in self.cart:
      pass
    else:
      # self.cart[product_id] = {'price': str(product.price)}
      self.cart[product_id] = int(product_quantity)
      
    self.session.modified = True 
    
  def quantity (self):
    return len(self.cart)
  
  def display_products(self):
    product_ids = self.cart.keys()
    products = Product.objects.filter(id__in = product_ids)
    return products
  
  def get_quantity(self):
    quantities = self.cart
    return quantities