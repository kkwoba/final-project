from django.shortcuts import render
from sales.models import Category, Product

# Create your views here.


def index(request):
    category_counts = {}  # Initialize an empty dictionary

    # Retrieve all categories
    categories = Category.objects.all()

    for category in categories:
        # Filter products for the current category
        products = Product.objects.filter(category=category)
        product_count = len(products)

        # Store the count in the dictionary
        category_counts[category.name] = product_count

    context = {
        'navbar': 'index',
        'categories': categories,
        'products': products,
        'category_counts': category_counts,  # Add the category counts to the context
    }
    return render(request, 'index.html', context)



def shop(request):
    return render(request, 'shop.html', {'navbar':'shop'})


def detail(request):
    return render(request, 'detail.html',{'navbar':'detail'})


def contact(request):
    return render(request, 'contact.html',{'navbar':'contact'})


def checkout(request):
    return render(request, 'checkout.html',{'navbar':'checkout'})

def cart(request):
    return render(request, 'cart.html',{'navbar':'cart'})

def layout(request):
    return render(request, 'layout.html',{'navbar':'layout'})





