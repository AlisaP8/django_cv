from django.urls import path
from .views import WarehouseListView, get_page

urlpatterns = [
    path('', WarehouseListView.as_view()),
    path('get', get_page),

]
