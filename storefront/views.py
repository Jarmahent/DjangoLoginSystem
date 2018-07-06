from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from storefront.models import store_item
from django.contrib.auth.decorators import user_passes_test
from storefront.forms import ItemModelForm

def store(request):
    items = list(store_item.objects.values())
    return render(request, 'storefront/item.html', {"items": items})

@user_passes_test(lambda u: u.is_superuser)
def submit_item(request):
    if request.method == 'POST':
        form = ItemModelForm(request.POST)
        if form.is_valid():
            form.save()
            print({
                "item_name": form.cleaned_data.get('item_name'),
                "item_description": form.cleaned_data.get('item_description'),
                "item_price": form.cleaned_data.get('item_price'),
                "item_is_available": form.cleaned_data.get('item_is_available')
            })
            return HttpResponseRedirect('/store')
    else:
        form = ItemModelForm()
    return render(request, 'storefront/submit_item.html', {"form": form})