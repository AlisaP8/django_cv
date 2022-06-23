from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.views.generic import ListView
from .models import Warehouse, Phone, Headphones


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


class PhoneListView(ProductListView):
    model = Phone
    queryset = Phone.on_site.prefetch_related('new_model').all()
    template_name = 'phone.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'product': {'name': 'Phone',
                        'receipt_date': '17.06.2022',
                        'price': '30000р',
                        'quantity': 'шт',
                        'vendor_name': 'MVid',
                        },
            'site': get_current_site(request=self.request),
        })
        return context


class HeadphonesListView(ProductListView):
    model = Headphones
    queryset = Headphones.objects.select_related('model').all()
    template_name = 'headphones.html'


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
        'product': return_extra(),
    })
