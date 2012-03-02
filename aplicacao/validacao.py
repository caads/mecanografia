# coding: utf-8 

from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _


class UploadFile(FileField):

	def __init__(self, *args, **kwargs):
		self.max_upload_size = kwargs.pop("max_upload_size")
		
		super(UploadFile, self).__init__(*args, **kwargs)

	def clean(self, *args, **kwargs):        
		data = super(UploadFile, self).clean(*args, **kwargs)
        
		file = data.file
		try:
			if file._size > self.max_upload_size:
				raise forms.ValidationError(_('O arquivo deve ter o tamanho igual ou inferior a %s. O seu arquivo possui %s.') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
		except AttributeError:
			pass        
            
		return data
