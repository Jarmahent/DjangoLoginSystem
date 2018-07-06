from django import forms
from storefront.models import store_item

class Itemform(forms.ModelForm):
    item_name = forms.CharField(label="Item Name" ,max_length=200)
    item_description = forms.CharField(label="Item Description" ,max_length=500, widget=forms.Textarea)
    item_price = forms.DecimalField(label="Item Price", max_value=500, decimal_places=3)
    item_is_available = forms.TypedChoiceField(choices=((False, 'No'), (True, 'Yes')))


class ItemModelForm(Itemform):
    class Meta:
        model = store_item
        field = ['item_name', 'item_price', 'item_is_available', 'item_description']
        exclude = ['item_id']