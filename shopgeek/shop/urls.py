from django.urls import path
from .views import WarehouseListView, get_page, PhoneListView, HeadphonesListView

urlpatterns = [
    path('', WarehouseListView.as_view()),
    path('phone', PhoneListView.as_view()),
    path('headphones', HeadphonesListView.as_view()),
    path('get', get_page),

]
