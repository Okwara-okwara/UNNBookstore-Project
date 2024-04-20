from django.shortcuts import render, redirect
from Cart.cart import Cart
from payment.forms import DeliveryForm, PaymentForm
from payment.models import DeliveryInfo, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib import messages
from Unnapp.models import Product




def clear_cart(request):
    request.session.pop('cart', None)
    request.session.save()

def process_order(request):
    if request.POST:
        # Get the cart
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()

        # Get payment info from the last page
        payment_form = PaymentForm(request.POST or None)

        # Get delivery session Data
        my_delivery = request.session.get('my_delivery')

        # Gather Order Info
        full_name = my_delivery['Delivery_full_name']
        email = my_delivery['Delivery_email']

        # Create delivery address from session info
        delivery_info = f"{my_delivery['Delivery_address']}\n{my_delivery['Delivery_full_name']}\n{my_delivery['Phone_No']}\n{my_delivery['Delivery_email']}\n{my_delivery['Delivery_date']}\n{my_delivery['Delivery_time']}"
        amount_paid = totals

        # Create an order
        if request.user.is_authenticated:
            user = request.user
            create_order = Order(user=user, full_name=full_name, email=email, delivery_info=delivery_info, amount_paid=amount_paid)
            # Save the order
            create_order.save()

            #Add order items
            #Get the order ID
            order_id = create_order.pk
            
            #Get product info
            for product in cart_products():

                #Get product id
                product_id = product.id

                #Get product price
                price = product.price
                
                #Get quantity
                for key,value in quantities().items():
                    if int(key) == product.id:
                        #create order item
                        create_order_item = OrderItem(order_id=order_id, product_id=product_id, user=user, quantity=value, price=price) 
                        create_order_item.save()                      



            cart = Cart(request)
            # Before clearing the cart
            print("Cart contents before clearing:", cart.cart)
            cart.clear()
            # after clearing the cart
            print("Cart contents before clearing:", cart.cart)
            clear_cart(request)

            messages.success(request, "Order Placed!")
            return redirect('home')
        
        else:
            #if not logged in
            create_order = Order(full_name=full_name, email=email, delivery_info=delivery_info, amount_paid=amount_paid)
            create_order.save()


            for product in cart_products():

                #Get product id
                product_id = product.id

                #Get product price
                price = product.price
                
                #Get quantity
                for key.value in quantities().items():
                    if int(key) == product.id:
                        #create order item
                        create_order_item = OrderItem(order=order_id, product=product_id, quantity=value, price=price) 
                        create_order_item_save()   


            cart = Cart(request)
            print("Cart contents before clearing:",{cart.cart})
            cart.clear()
            print("Cart contents after clearing:", {cart.cart})
            messages.success(request, "Order Placed! Make sure to remove item from cart!")
            return redirect('home')
        

    else:
        messages.success(request, "Access Denied")
        redirect('home')



def billing_info(request):
	if request.POST:
		# Get the cart
		cart = Cart(request)
		cart_products = cart.get_prods
		quantities = cart.get_quants
		totals = cart.cart_total()

		#create a session with delivery info
		my_delivery = request.POST
		request.session['my_delivery'] = my_delivery

		# Check to see if user is logged in
		if request.user.is_authenticated:
			# Get The Billing Form
			billing_form = PaymentForm()
			return render(request, "payment/billing_info.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "delivery_info":request.POST, "billing_form":billing_form})

		else:
			# Not logged in
			# Get The Billing Form
			billing_form = PaymentForm()
			return render(request, "payment/billing_info.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form})


		
		shipping_form = request.POST
		return render(request, "payment/billing_info.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "delivery_form":delivery_form})	
	else:
		messages.success(request, "Access Denied")
		return redirect('home')





def checkout(request):
    #Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()




    if request.user.is_authenticated:
		# Checkout as logged in user
        delivery_user = DeliveryInfo.objects.get(user__id=request.user.id)
		# delivery Form
        delivery_form = DeliveryForm(request.POST or None, instance=delivery_user)
        return render(request, "payment/checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "delivery_form":delivery_form})
    else:
		# Checkout as guest
        delivery_form = DeliveryForm(request.POST or None)
        return render(request, "payment/checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "delivery_form":delivery_form})

	

    

def payment_success(request):

    return render(request, "payment/paymemt_success.html", {})