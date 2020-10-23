from django.forms import ModelForm, Textarea
from auctions.models import Listing, Bid


class ListingForm(ModelForm):
    
    class Meta:
        model = Listing
        fields = ['title', 'category', 'bid', 'description', 'image_url']
        widgets = {
             'description': Textarea(attrs={'cols': 50, 'rows': 9}),
        }

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['value_offer']
