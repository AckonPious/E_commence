from django.shortcuts import render
from item.models import Item, Categroy

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categroies = Categroy.objects.all()
    return render(request, "core/index.html", {
        'categroies' : categroies,
        'items' : items,
    })

def contact(request):
    return render(request, 'core/contact.html')
