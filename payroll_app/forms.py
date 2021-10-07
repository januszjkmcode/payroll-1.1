from django.forms import ModelForm
from .models import *
from django import forms

from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

from datetime import date
from datetime import datetime, timedelta
from networkdays import networkdays
#import datetime


def start_data():
	a = datetime.now() - timedelta(days=7305)
	return a


class DateInput(forms.DateInput):

    input_type = 'date'	 


class NewEmployee(forms.Form):

	country=list()
	countries=Countries.objects.all()
	for i in countries:
		country.append(i.en)
	country_zip=zip(country,country)

	name1 =  forms.CharField(max_length=50,label='First name',
    							widget=forms.TextInput(attrs={'class': 'form-control'}))

	name2 =  forms.CharField(max_length=50,label='Middle name',required=False,
    							widget=forms.TextInput(attrs={'class': 'form-control'}))

	surname =  forms.CharField(max_length=50,
    							widget=forms.TextInput(attrs={'class': 'form-control'}))

	nationality = forms.ChoiceField(choices=country_zip,
    							widget=forms.Select(attrs={'class': 'form-control'}))

	pesel = forms.CharField(label="Pesel", max_length=11,required=False,							
    							widget=forms.TextInput(attrs={'class': 'form-control'}))	

	date_of_birth = forms.DateField(label="Date of birth",
    									widget=DateInput(attrs={'class':'.form-select-sm'}),
    									initial=start_data)

	place_of_birth = forms.CharField(label="Place_of_birth",max_length=50,
    									widget=forms.TextInput(attrs={'class': 'form-control'}))

	fathers_name = forms.CharField(label="Father's name", max_length=50,required=False,
    							   		widget=forms.TextInput(attrs={'class': 'form-control'}))

	mothers_name = forms.CharField(label="Mother's name",max_length=50,required=False,
    									widget=forms.TextInput(attrs={'class': 'form-control'}))

	family_name = forms.CharField(label="Family name", max_length=50,required=False,
    									widget=forms.TextInput(attrs={'class': 'form-control'}))

	mothers_family_name = forms.CharField(label="Mothers family name",max_length=50,required=False,
    									widget=forms.TextInput(attrs={'class': 'form-control'}))
	
	gender = [
		('Woman', 'Woman'),
		('Man', 'Man'),
	]	

	doc = [
		('Passport', 'Passport'),
		('ID card', 'ID card'),
		('Driving license', 'Driving license'),
		('Other', 'Other'),
	]
	gender = forms.ChoiceField(choices=gender,
    							widget=forms.Select(attrs={'class': 'form-control'}))

	doc = forms.ChoiceField(choices=doc,label='Type of document',
    							widget=forms.Select(attrs={'class': 'form-control'}))

	nr_doc = forms.CharField(max_length=50,label='No. document',
    							widget=forms.TextInput(attrs={'class': 'form-control'}))

	
	def clean_pesel(self):
		pesel = self.cleaned_data.get('pesel')
		if pesel == '':
			return pesel
		
		digits = ['0','1','2','3','4','5','6','7','8','9']

		for x in pesel:
			if x in digits:
	  			pass
			else:
	  			raise forms.ValidationError("Pesel only consists of numbers")

		if len(pesel) == 11:   
			pass
		else:
			raise forms.ValidationError("Pesel must contain 11 characters")
			
		return pesel

	def clean_date_of_birth(self):
		date_of_birth = self.cleaned_data.get('date_of_birth')
		pesel = self.cleaned_data.get('pesel')

		if pesel == '':
			return date_of_birth

		year = date_of_birth.year
		str_year = str(year)
		month = date_of_birth.month
		day = date_of_birth.day

		a = pesel[0:2]
		b = pesel[2:4]
		c = pesel[4:6]

		if year > 1999:
			month = month + 20

		if month < 10:
			str_month = "0"+str(month)
		else:
			str_month = str(month)

		if day < 10:
			str_day = "0"+str(day)
		else:
			str_day = str(day)

		#print("ROK", str_year[2:4], "MIESIĄC", str_month, "DZIEŃ",str_day)
		if (str_year[2:4] == a) and (str_month == b) and (str_day == c) :
			pass
		else:
			raise forms.ValidationError("Incorrect PESEL or date of birth")

		return date_of_birth


class Address_form(ModelForm):


	class Meta:
		model = Address
		fields = ['type_address',
					'voivodeship',
					'district',
					'commune',
					'city',
					'street',
					'building_no',
					'apartment_no',
					'post','post_code'
			]
			
		widgets = {
			'type_address': forms.Select(attrs={'class': 'form-control'}),
			'voivodeship': forms.TextInput(attrs={'class': 'form-control'}),
			'district': forms.TextInput(attrs={'class': 'form-control'}),
			'commune': forms.TextInput(attrs={'class': 'form-control'}),
			'city': forms.TextInput(attrs={'class': 'form-control'}),
			'street': forms.TextInput(attrs={'class': 'form-control'}),
			'building_no': forms.TextInput(attrs={'class': 'form-control'}),
			'apartment_no': forms.TextInput(attrs={'class': 'form-control'}),
			'post': forms.TextInput(attrs={'class': 'form-control'}),
			'post_code': forms.TextInput(attrs={'class': 'form-control'}),
		}

	def clean_post_code(self):
		post_code = self.cleaned_data.get('post_code')

		code = ['0','1','2','3','4','5','6','7','8','9','-']

		if post_code[2] == '-':
			pass
		else:
			raise forms.ValidationError("The post code should be in the format XX-XXX")

		for x in post_code:
			if x in code:
				pass
			else:
				raise forms.ValidationError(
					"The post code should be in the format XX-XXX and include only digits")

		if len(post_code)==6:
			pass
		else:
			raise forms.ValidationError("The post code should be in the format XX-XXX")

		return	post_code


class Contract_form_creator(forms.Form):

	x = List_of_Profession.objects.all()

	x2 = zip(x,x)

	working_hours = [
		('Full time', 'Full time'),
		('3/4', '3/4'),
		('3/5', '3/5'),
		('1/2', '1/2'),
		('1/4', '1/4'),
		('Unlimited', 'Unlimited'),
	]

	working_hours = forms.ChoiceField(choices=working_hours,
										widget=forms.Select(attrs={'class': 'form-control'}))

	daily_norm = forms.DecimalField(label="Daily norm", initial=8,
										widget=forms.NumberInput(attrs={'class': 'form-select-sm'}))

	type_of_contract = [
			('Employment contract', 'Employment contract'),
			('Mandate contract', 'Mandate contract'),
			('Contract of specific task', 'Contract of specific task'),
			('Civil-legal contract', 'Civil-legal contract'),
	]
	
	type_of_contract = forms.ChoiceField(choices=type_of_contract,
										widget=forms.Select(attrs={'class': 'form-control'}))

	place_of_work = [
			('Headquarters', 'Headquarters'),
			('Field work ', 'Field work '),
			('Other ', 'Other '),
	]

	place_of_work = forms.ChoiceField(choices=place_of_work,
										widget=forms.Select(attrs={'class': 'form-control'}))

	copyright_contract = forms.BooleanField(label="Copyright contract", required=False,
										widget=forms.CheckboxInput(attrs={'class':'.form-select-sm'}))

	main_place_of_work = forms.BooleanField(label="Main place of work", required=False,
										widget=forms.CheckboxInput(attrs={'class':'.form-select-sm'}))

	amount_of_base_salary = forms.DecimalField(label="Amount of base salary", initial=1000,
										widget=forms.NumberInput(attrs={'class': 'form-select-sm'}))

	type_of_base_salary = [
			('monthly', 'monthly'),
			('hourly', 'hourly'),
			('weekly', 'weekly'),
	]

	type_of_base_salary = forms.ChoiceField(choices=type_of_base_salary,
										widget=forms.Select(attrs={'class': 'form-control'}))
	type_of_perks = [
			('perk1', 'perk1'),
			('perk2', 'perk2'),
			('perk3', 'perk3'),
			('perk4', 'perk4'),
	]

	type_of_perks = forms.ChoiceField(choices=type_of_perks,
										widget=forms.Select(attrs={'class': 'form-control'}))

	amount_of_perks = forms.DecimalField(label="Amount of perks", initial=100, required=False,
										widget=forms.NumberInput(attrs={'class': 'form-select-sm'}))

	account_number = forms.DecimalField(label="Account number", required=False,
										widget=forms.TextInput(attrs={'class': 'form-control'})) 

	method_of_payment = [
			('cash', 'cash'),
			('bank transfer', 'bank transfer'),
	]

	method_of_payment = forms.ChoiceField(choices=method_of_payment,
										widget=forms.Select(attrs={'class': 'form-control'}))

	list_of_profession = forms.ChoiceField(choices=x2,
										widget=forms.Select(attrs={'class': 'form-control'}))

	conclusion_of_the_contract = forms.DateField(label="Conclusion of the contract",
										widget=DateInput(attrs={'class': '.form-select-sm'}))

	date_of_start_work = forms.DateField(label="Date of start work",
										widget=DateInput(attrs={'class':'.form-select-sm'}))

	contract_period = forms.DateField(label="Contract period", required=False,
										widget=DateInput(attrs={'class': '.form-select-sm'}))

	company_representative = forms.CharField(required=False,
										widget=forms.TextInput(attrs={'class': 'form-control'}))

	# def clean_daily_norm(self):
	# 	daily_norm = self.cleaned_data.get('daily_norm')
	# 	if daily_norm < 1:
	# 		print('działa dobrze')
			#raise forms.ValidationError("Daily norm must be greater than 0")



class CreateUserForm(UserCreationForm):

	
	class Meta:
		model = User 
		fields = ['username','email','password1','password2']


class List_of_Profession_Form(forms.Form):


	def __init__(self, *args, **kwargs):
		self.txt = kwargs.pop('txt_zip', None)
		super(List_of_Profession_Form, self).__init__(*args, **kwargs)
		self.fields['professions'].choices = self.txt

	working_hours = [
		('Full time', 'Full time'),
		('3/4', '3/4'),
		('3/5', '3/5'),
		('1/2', '1/2'),
		('1/4', '1/4'),
		('Unlimited', 'Unlimited'),
	]	

	working_hours = forms.ChoiceField(choices=working_hours,widget=forms.Select(attrs={'class': 'form-control'}))
	professions = forms.ChoiceField(choices=(), widget=forms.Select(attrs={'class': 'form-control'}))


class Employee_edit_form(ModelForm):
	class Meta:


		model = Employee_Variable_Unconstant
		fields = ['name1','name2','surname','gender','doc','nr_doc','nationality']

		widgets = {
			'name1': forms.TextInput(attrs={'class': 'form-control'}),
			'name2': forms.TextInput(attrs={'class': 'form-control'}),
			'surname': forms.TextInput(attrs={'class': 'form-control'}),
			'gender': forms.Select(attrs={'class': 'form-control'}),
			'doc': forms.Select(attrs={'class': 'form-control'}),
			'nr_doc': forms.TextInput(attrs={'class': 'form-control'}),
			'nationality': forms.Select(attrs={'class': 'form-control'}),

		}