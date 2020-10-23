from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create-listing", views.create_listing, name="create_listing"),
    path("listing-page/<int:listing_id>", views.listing_page, name="listing_page"),
    path("create-bid/<int:listing_id>", views.create_bid, name="create_bid"),
    path("watchlist-action/<int:listing_id>", views.watchlist_action, name="watchlist action"),
    path("close-listing/<int:listing_id>",views.close_listing, name="close_listing"),
    path("watchlist_page",views.watchlist_page, name="watchlist_page"),
    path("add-comment/<int:listing_id>", views.add_comment, name="leave_comment"),
    path("categories/<str:category>", views.categories, name='categories'),
    path("category_index", views.category_index, name="category_index"),
    path("all_listing",views.all_listing,name="all_listing")

]
