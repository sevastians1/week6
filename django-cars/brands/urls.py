from . import views
from django.urls import path
urlpatterns = [
    path("", views.all_brands), # a list of all the car brands
    path("new", views.new_brand),  # form for a new car brand
# /brands/<:id> # see a specific car brand
# /brands/<:id>/edit # edit page for a specific car brand
    path("<int:brand_id>/cars", views.one_brand),
    # path("<:brand_id>/cars/new"),
    path("<int:brand_id>/cars/<int:car_id>", views.one_car),
    # path("<:brand_id>/cars/<:car_id>/edit")
    # path("test", views.side_page)
]