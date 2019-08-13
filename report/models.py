from django.db import models
import pandas as pd
from datetime import date
from core.models import UNIT
from django.utils.text import slugify


# Create your models here.

class Invoice(models.Model):
	"""
    A model to store invoice data.
    """
	unit = models.ForeignKey(UNIT, on_delete=models.CASCADE)
	slug = models.SlugField(blank=True, unique=True)
	vat_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.21)  # daily
	date = models.DateField(editable=False, auto_now_add=True)
	start = models.DateField()
	end = models.DateField()
	delivery_date = models.DateField(blank=True, null=True)
	days = models.DecimalField(max_digits=5, decimal_places=2)
	paid = models.BooleanField(default=False)
	description = models.CharField(max_length=500, null=True, blank=True)
	is_credit_invoice = models.BooleanField(default=False)

	def __str__(self):
		return '{} - {}'.format(self.date, self.unit)

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		self.slug = slugify(str(self.unit) + str(self.date))
		super(Invoice, self).save()


class InvoiceItem(models.Model):
	invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	vat = models.DecimalField(max_digits=7, decimal_places=2,
							  help_text='If the VAT% is not equal to the overall VAT rate', null=True, blank=True
							  )
