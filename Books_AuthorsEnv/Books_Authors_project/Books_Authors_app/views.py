from django.shortcuts import render, redirect
from . models import Item, Author


def index(request):
    context = {
        'all_items': Item.objects.all(),
        'all_authors': Author.objects.all()
    }
    print(context['all_items'])
    return render(request, "index.html", context)

def add_item_to_inventory(request):
    print(request.POST)

    author_id = request.POST['author']
    author_instance = Author.objects.get(id=author_id)

    # add item to Database
    Item.objects.create(
        item_name = request.POST['item_name'],
        
        publisher = author_instance
    )

    return redirect('/')

def add_author(request):
    print(request.POST)

    new_author = Author.objects.create(
        name = request.POST['author']
    )

    print('We created a author!', new_author)
    return redirect('/')

    supplier_id = request.POST['author']