from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import OrderForm


# Product List Page
def product_list(request):
    products = Product.objects.all()
    return render(request, "shop/product_list.html", {"products": products})

# Product Detail Page (with multiple images)
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "shop/product_detail.html", {"product": product})



def search(request):
    

    query = request.GET.get("q", "")
    results = Product.objects.filter(name__icontains=query) if query else []
    return render(request, "shop/search.html", {"query": query, "results": results,})




# Order Confirmation Page
def order_confirmation(request):
    
    product_id = request.GET.get('product')
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.price = product.price
            order.total_price = request.POST.get('total_price')
            order.save()
            return render(request, "shop/order_confirmation.html", {"order": order})
    else:
        form = OrderForm()

    return render(request, "shop/order_form.html", {"form": form, "product": product})

     
    
from django.shortcuts import render, get_object_or_404
from .models import Order

def about(request):
    return render(request, "shop/about.html")

def privacy_policy(request):
    return render(request, "shop/privacy_policy.html")