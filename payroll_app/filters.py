import django_filters 
from django_filters import DateFilter, CharFilter

from .models import *


class ProfessionFilter(django_filters.FilterSet):

	note = CharFilter(field_name="name_of_proffession", lookup_expr='startswith', label='Name of profession ')
	class Meta:
		model = List_of_Profession
		fields = {
			'code' : ['startswith']
		}