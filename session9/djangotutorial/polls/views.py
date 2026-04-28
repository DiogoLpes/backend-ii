from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Product, Order
import json


# ============ HTML Pages ============

def home(request):
    """Main products page with HTML UI"""
    products = Product.objects.all()
    
    # Get current cart
    user_id = 1
    cart_order = Order.objects.filter(user_id=user_id, paid=False).first()
    cart_items = cart_order.cart if cart_order and cart_order.cart else []
    cart_total = cart_order.total if cart_order else 0
    
    return render(request, "polls/products.html", {
        "products": products,
        "cart_items": cart_items,
        "cart_total": cart_total
    })


def cart_page(request):
    """Cart page with HTML UI"""
    user_id = 1
    cart_order = Order.objects.filter(user_id=user_id, paid=False).first()
    cart_items = cart_order.cart if cart_order and cart_order.cart else []
    cart_total = cart_order.total if cart_order else 0
    
    return render(request, "polls/cart.html", {
        "cart_items": cart_items,
        "cart_total": cart_total
    })


# ============ API Product Views ============

def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        data = [
            {"id": p.pk, "name": p.name, "price": p.price}
            for p in products
        ]
        return JsonResponse({"products": data}, status=200)
    
    elif request.method == "POST":
        try:
            body = json.loads(request.body)
            product = Product.objects.create(
                name=body.get("name"),
                price=body.get("price")
            )
            return JsonResponse({
                "id": product.pk,
                "name": product.name,
                "price": product.price
            }, status=201)
        except (json.JSONDecodeError, KeyError) as e:
            return JsonResponse({"error": str(e)}, status=400)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == "GET":
        return JsonResponse({
            "id": product.pk,
            "name": product.name,
            "price": product.price
        })
    
    elif request.method == "PUT":
        body = json.loads(request.body)
        product.name = body.get("name", product.name)
        product.price = body.get("price", product.price)
        product.save()
        return JsonResponse({
            "id": product.pk,
            "name": product.name,
            "price": product.price
        })
    
    elif request.method == "DELETE":
        product.delete()
        return JsonResponse({"message": "Product deleted"}, status=204)


# ============ API Order Views ============

def order_list(request):
    if request.method == "GET":
        orders = Order.objects.all()
        data = [
            {
                "id": o.pk,
                "user_id": o.user_id,
                "cart": o.cart,
                "total": o.total,
                "paid": o.paid,
                "updated": o.update_time.isoformat()
            }
            for o in orders
        ]
        return JsonResponse({"orders": data}, status=200)
    
    elif request.method == "POST":
        try:
            body = json.loads(request.body)
            user_id = body.get("user_id")
            
            order = Order.objects.create(
                user_id=user_id,
                cart=[],
                total=0
            )
            return JsonResponse({
                "id": order.pk,
                "user_id": order.user_id,
                "cart": order.cart,
                "total": order.total
            }, status=201)
        except (json.JSONDecodeError, KeyError) as e:
            return JsonResponse({"error": str(e)}, status=400)


def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    
    if request.method == "GET":
        return JsonResponse({
            "id": order.pk,
            "user_id": order.user_id,
            "cart": order.cart,
            "total": order.total,
            "paid": order.paid,
            "updated": order.update_time.isoformat()
        })
    
    elif request.method == "DELETE":
        order.delete()
        return JsonResponse({"message": "Order deleted"}, status=204)


@require_http_methods(["POST"])
def add_to_cart(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    
    if order.paid:
        return JsonResponse({"error": "Order already paid"}, status=400)
    
    try:
        body = json.loads(request.body)
        product_id = body.get("product_id")
        quantity = body.get("quantity", 1)
        
        product = get_object_or_404(Product, pk=product_id)
        
        cart_item = {
            "product_id": product.pk,
            "name": product.name,
            "price": product.price,
            "quantity": quantity
        }
        
        cart = order.cart if order.cart else []
        cart.append(cart_item)
        order.cart = cart
        
        order.total = sum(item["price"] * item["quantity"] for item in cart)
        order.save()
        
        return JsonResponse({
            "message": "Product added to cart",
            "cart": order.cart,
            "total": order.total
        })
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404)
    except (json.JSONDecodeError, KeyError) as e:
        return JsonResponse({"error": str(e)}, status=400)


@require_http_methods(["POST"])
def remove_from_cart(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    
    if order.paid:
        return JsonResponse({"error": "Order already paid"}, status=400)
    
    try:
        body = json.loads(request.body)
        product_id = body.get("product_id")
        
        cart = order.cart if order.cart else []
        
        original_len = len(cart)
        cart = [item for item in cart if item.get("product_id") != product_id]
        
        if len(cart) == original_len:
            return JsonResponse({"error": "Product not in cart"}, status=404)
        
        order.cart = cart
        order.total = sum(item["price"] * item["quantity"] for item in cart)
        order.save()
        
        return JsonResponse({
            "message": "Product removed from cart",
            "cart": order.cart,
            "total": order.total
        })
    except (json.JSONDecodeError, KeyError) as e:
        return JsonResponse({"error": str(e)}, status=400)


@require_http_methods(["POST"])
def pay_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    
    if order.paid:
        return JsonResponse({"error": "Order already paid"}, status=400)
    
    if not order.cart:
        return JsonResponse({"error": "Cart is empty"}, status=400)
    
    order.paid = True
    order.save()
    
    return JsonResponse({
        "message": "Order paid successfully",
        "order_id": order.pk,
        "total": order.total,
        "paid": order.paid
    })


# ============ Simple Cart Views (user-based) ============

def cart_view(request):
    """Get or create current user's cart"""
    user_id = 1
    
    order = Order.objects.filter(user_id=user_id, paid=False).first()
    
    if not order:
        order = Order.objects.create(user_id=user_id, cart=[], total=0)
    
    return JsonResponse({
        "cart": order.cart,
        "total": order.total,
        "item_count": len(order.cart) if order.cart else 0
    })


@require_http_methods(["POST"])
def add_to_cart_simple(request, product_id):
    """Add product to cart (simpler version)"""
    user_id = 1
    
    order = Order.objects.filter(user_id=user_id, paid=False).first()
    if not order:
        order = Order.objects.create(user_id=user_id, cart=[], total=0)
    
    product = get_object_or_404(Product, pk=product_id)
    
    cart = order.cart if order.cart else []
    cart.append({
        "product_id": product.pk,
        "name": product.name,
        "price": product.price,
        "quantity": 1
    })
    
    order.cart = cart
    order.total = sum(item["price"] * item["quantity"] for item in cart)
    order.save()
    
    return JsonResponse({
        "message": f"{product.name} added to cart",
        "cart": order.cart,
        "total": order.total
    })


@require_http_methods(["POST"])
def remove_from_cart_simple(request, product_id):
    """Remove product from cart (simpler version)"""
    user_id = 1
    
    order = Order.objects.filter(user_id=user_id, paid=False).first()
    if not order:
        return JsonResponse({"error": "Cart is empty"}, status=400)
    
    cart = order.cart if order.cart else []
    cart = [item for item in cart if item.get("product_id") != product_id]
    
    order.cart = cart
    order.total = sum(item["price"] * item["quantity"] for item in cart)
    order.save()
    
    return JsonResponse({
        "message": "Product removed from cart",
        "cart": order.cart,
        "total": order.total
    })


@require_http_methods(["POST"])
def pay_cart(request):
    """Pay for the current cart"""
    user_id = 1
    
    order = Order.objects.filter(user_id=user_id, paid=False).first()
    if not order:
        return JsonResponse({"error": "No active cart"}, status=400)
    
    if not order.cart:
        return JsonResponse({"error": "Cart is empty"}, status=400)
    
    order.paid = True
    order.save()
    
    return JsonResponse({
        "message": "Order paid successfully!",
        "order_id": order.pk,
        "total": order.total,
        "items": len(order.cart)
    })
