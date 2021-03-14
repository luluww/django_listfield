from django.forms.widgets import Input

class ListInput(Input):
	input_type = 'hidden'
	template_name = 'list.html'

	def value_from_datadict(self, data, files, name):
		return ','.join(data.getlist(name)[1:])