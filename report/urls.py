from django.conf.urls import url
from .views import generate_invoice, display_invoice, check_invoices, home_view


app_name = 'invoice'

urlpatterns = [
	url(r'^$', home_view, name='generate_invoice'),
	url(r'^check_invoice/$', check_invoices, name='check invoice'),
	url(r'^invoice_view/(?P<slug>[\w-]+)/$', display_invoice, name='display_invoice_page'),
]