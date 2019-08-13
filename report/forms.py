from django import forms
from .models import Invoice
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class InvoiceForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = [
			'unit',
			'start',
			'end',
			'delivery_date',
			'days',
			'paid',
			'description',
		]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Save'))
