from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, date


class User(AbstractUser):
    pass


class Listing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_listings")
    title = models.CharField(max_length=64, help_text="Title(required), Maximum 70 characters")
    category = models.CharField(max_length=64,blank=True,  help_text="(not required) This could help your "
                                                                     "product gain the spotlight it deserves! "
                                                                     "Examples of categories include Fashion, Toys, "
                                                                     "Electronics, Home, etc.")
    bid = models.DecimalField(max_digits=10, decimal_places=2, help_text="Starting bid (required), greater than 0 but less than $9,999,999")
    description = models.CharField(max_length=2048, help_text="Description(required), Lets users know more about what you're selling! ")
    image_url = models.CharField(max_length=2048,blank=True, help_text="(not required) but if you want to "
                                                                        "include an image for your product, "
                                                                        "please include an online url for it here!")
    closed = models.BooleanField(default=False)
    watchlist_users = models.ManyToManyField(User, blank=True, related_name="watchlist_items")
    post_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.title} : {self.description}"

    def current_price(self):
        return max([bid.value_offer for bid in self.bids.all()]+[self.bid])

    def no_of_bids(self):
        return len(self.bids.all())

    def current_winning_bidder(self):
        return self.bids.get(value_offer=self.current_price()).user if self.no_of_bids() > 0 else None

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    value_offer = models.DecimalField(max_digits=8, decimal_places=2, help_text="How much are you willing to pay for "
                                                                                "this item?")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids_made")

    def clean(self):
        # Don't allow value offer to be lower than current price of listing
        print(self.value_offer)
        print(self.listing.current_price())
        if self.value_offer and self.listing.current_price():
            if self.value_offer <= self.listing.current_price():
                raise ValidationError({'value_offer':('Please make sure your bid value is higher than the current '
                                                        'price of the item!')})


    def __str__(self):
        return f"{self.user} offers to pay ${self.value_offer} for the listing: {self.listing}"



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")

    message = models.CharField(max_length=2048)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")


    def __str__(self):
        return f"{self.author} says {self.message} for listing: {self.listing}"
