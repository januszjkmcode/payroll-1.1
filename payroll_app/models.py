from django.db import models

class Countries(models.Model):
	en = models.CharField(max_length=100)
	pl = models.CharField(max_length=100)
	
	
	def __str__(self):
		return (str (self.en))	
	

class Employee_Variable_Constant(models.Model):


	pesel = models.CharField(max_length=11,null=True,blank=True)	
	date_of_birth = models.DateField()
	place_of_birth = models.CharField(max_length=50)
	fathers_name = models.CharField(max_length=50,null=True,blank=True)
	mothers_name = models.CharField(max_length=50,null=True,blank=True)
	family_name = models.CharField(max_length=50,null=True,blank=True)
	mothers_family_name = models.CharField(max_length=50,null=True,blank=True)
	date_of_entry = models.DateTimeField(auto_now=True)

	def __str__(self):
		return (str (self.pesel) + "constans variable")	


class Employee_Variable_Unconstant(models.Model):


	gender = [
		('Woman', 'Woman'),
		('Man', 'Man'),
	]	

	doc = [
		('Passport', 'Passport'),
		('ID card', 'ID card'),
		('Other', 'Other'),
		('Driving license', 'Driving license'),		
	]	
	country=list()
	countries= Countries.objects.all()
	for i in countries:
		country.append(i.en)

	countries_zip=zip(country,country)
	 
	id_employee = models.OneToOneField(Employee_Variable_Constant,
									   on_delete=models.CASCADE, primary_key=True
									)
	name1 =  models.CharField(max_length=50)
	name2 =  models.CharField(max_length=50,null=True,blank=True)
	surname =  models.CharField(max_length=50)
	gender = models.CharField(max_length=200, choices=gender)
	doc = models.CharField(max_length=200, choices=doc)
	nr_doc = models.CharField(max_length=50)
	nationality = models.CharField(max_length=100, choices=countries_zip)
	date_of_entry = models.DateTimeField(auto_now=True)

	def __str__(self):
		return (str (self.name1) + " "+ str(self.surname))


class Employee_Variable_Unconstant_ARC(models.Model):


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

	id_employee = models.ForeignKey(Employee_Variable_Constant,
									   on_delete=models.CASCADE
									)
	name1 =  models.CharField(max_length=50)
	name2 =  models.CharField(max_length=50,null=True,blank=True)
	surname =  models.CharField(max_length=50)
	gender = models.CharField(max_length=200, choices=gender)
	doc = models.CharField(max_length=200, choices=doc)
	nr_doc = models.CharField(max_length=50)
	nationality = models.CharField(max_length=50)
	date_of_entry = models.DateTimeField()
	date_of_exit = models.DateTimeField(auto_now=True)

	def __str__(self):
		return (str (self.name1) + " "+ str(self.surname))


class Address(models.Model):


	type_adr = [
		('Constans', 'Constans'),
		('Temporary', 'Temporary'),
		('Correspondence', 'Correspondence'),
		('Address of residence ', 'Address of residence'),
	]


	type_address = models.CharField(max_length=100,choices=type_adr)
	id_employee = models.ForeignKey(Employee_Variable_Constant,
									 on_delete=models.CASCADE
								)
	voivodeship = models.CharField(max_length=100)
	district = models.CharField(max_length=100)
	commune = models.CharField(max_length=100)
	city  =models.CharField(max_length=100)
	street = models.CharField(max_length=200)
	building_no = models.CharField(max_length=50)
	apartment_no = models.CharField(max_length=50, null=True, blank=True)
	post =  models.CharField(max_length=50)
	post_code = models.CharField(max_length=50)
	date_of_entry = models.DateTimeField(auto_now=True)


class Address_ARC(models.Model):


	type_adr = [
		('Constans', 'Constans'),
		('Temporary', 'Temporary'),
		('Correspondence', 'Correspondence'),
		('Address of residence ', 'Address of residence'),
	]


	type_address = models.CharField(max_length=100,choices=type_adr)
	id_employee = models.ForeignKey(Employee_Variable_Constant,
									on_delete=models.CASCADE)	
	voivodeship = models.CharField(max_length=100)
	district = models.CharField(max_length=100)
	commune = models.CharField(max_length=100)
	city  =models.CharField(max_length=100)
	street = models.CharField(max_length=200)
	building_no = models.CharField(max_length=50)
	apartment_no = models.CharField(max_length=50, null=True, blank=True)
	post =  models.CharField(max_length=50)
	post_code = models.CharField(max_length=50)
	date_of_entry = models.DateTimeField()
	date_of_exit = models.DateTimeField(auto_now=True)
	type_of_change = models.CharField(max_length=15)


class Profession(models.Model):


	working_hours = [
		('Full time', 'Full time'),
		('3/4', '3/4'),
		('3/5', '3/5'),
		('1/2', '1/2'),
		('1/4', '1/4'),
		('Unlimited', 'Unlimited'),
	]	


	id_employee = models.ForeignKey(Employee_Variable_Constant, 
									on_delete=models.CASCADE)
	code = models.CharField(max_length=6)
	name_of_proffession = models.CharField(max_length=100)
	working_hours = models.CharField(max_length=30, choices=working_hours)
	date_of_entry = models.DateTimeField(auto_now=True)


class Profession_ARC(models.Model):


	id_employee = models.ForeignKey(Employee_Variable_Constant,
									on_delete=models.CASCADE)
	code = models.CharField(max_length=6)
	name_of_proffession = models.CharField(max_length=100)
	working_hours = models.CharField(max_length=30)
	date_of_entry = models.DateTimeField()
	date_of_exit = models.DateTimeField(auto_now=True)
	type_of_change = models.CharField(max_length=15)


class List_of_Profession(models.Model):


	code = models.CharField(max_length=6)
	name_of_proffession = models.CharField(max_length=100)


	def __str__(self):
		return (str(self.name_of_proffession)+ " - " +str(self.code))	


class Contract(models.Model):


	id_employee = models.ForeignKey(Employee_Variable_Constant,
									null=True, on_delete=models.CASCADE)
	type_of_contract = models.CharField(max_length=50)
	date_of_start_work = models.DateField(null=True)
	copyright_contract = models.BooleanField(null=True,blank=True)
	place_of_work = models.CharField(max_length=50)
	main_place_of_work = models.BooleanField(null=True,blank=True)
	daily_norm = models.DecimalField(max_digits=4, decimal_places=2)
	type_of_base_salary = models.CharField(max_length=50)
	amount_of_base_salary = models.DecimalField(max_digits=7, decimal_places=2)
	method_of_payment =  models.CharField(max_length=50)
	account_number = models.CharField(max_length=26,null=True,blank=True)
	type_of_perks = models.CharField(max_length=50)
	amount_of_perks = models.DecimalField(max_digits=7, decimal_places=2, null=True,blank=True)
	conclusion_of_the_contract = models.DateField()
	company_representative = models.CharField(max_length=50, null=True,blank=True)
	contract_period = models.DateField(null=True,blank=True)


