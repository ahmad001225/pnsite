from django.shortcuts import render

app_name="product"

def product_view(request):
    return render(request,'product/product.html')

