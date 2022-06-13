from django.shortcuts import render
from django.views.generic import ListView
from .models import Warehouse


class ProductListView(ListView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            # 'product': {'name': 'Phone',
            #             'receipt_date': '11.06.2022',
            #             'price': '25000р',
            #             'quantity': 'шт',
            #             'vendor_name': 'MVid',
            #             }
        })
        return context


class WarehouseListView(ProductListView):
    model = Warehouse
    queryset = Warehouse.objects.all()
    template_name = 'index.html'


def return_extra():
    return {'name': 'Phone',
            'receipt_date': '11.06.2022',
            'price': '25000р',
            'quantity': 'шт',
            'vendor_name': 'MVid',
            }


def get_page(request):
    return render(request, 'index.html', context={
        'object_list': Warehouse.objects.all(),
        'user': return_extra()
    })
