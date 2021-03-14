from django.db.models import CharField
from django.forms import CharField as CharFormField

from .widgets import ListInput

class CharListFormField(CharFormField):
	widget = ListInput


class CharListField(CharField):
	def formfield(self, **kwargs):
		return super().formfield(**{
			'form_class': CharListFormField,
			**kwargs
			})