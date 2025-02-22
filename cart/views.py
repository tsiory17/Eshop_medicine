from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .cart import Cart 
from shop.models import Product
from django.http import JsonResponse
# Create your views here.
def cart_summary (request):
  cart = Cart(request)
  cart_products = cart.display_products
  quantities = cart.get_quantity
  return render(request,'cart_summary.html',{"cart_products":cart_products , "quantities":quantities})

def add_cart (request):
  cart = Cart(request)
  #test the post 
  if request.POST.get('action') == 'post':
    #get the id 
    product_id = int (request.POST.get('product_id'))
    product_quantity = int (request.POST.get('product_qty'))
    #check the db
    product = get_object_or_404(Product, id=product_id)
    # save session 
    cart.add(product = product , quantity = product_quantity)
    #return respose 
    # response = JsonResponse({'Product Name': product.name})
    cart_quantity = cart.quantity()
    response = JsonResponse({'qty': cart_quantity})
    return response

def update_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_qty'))
        cart.update(product = product_id, quantity = product_quantity)
        
        response = JsonResponse({'product_quantity': product_quantity})
        return response
        


def delete_cart (request):
   cart = Cart(request)
   if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product = product_id)
        
        response = JsonResponse({'product': product_id})
        return response
 


