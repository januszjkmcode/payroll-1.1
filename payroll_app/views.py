from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *
from django.contrib.auth import authenticate  
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from .forms import CreateUserForm
from django.contrib import messages
from formtools.wizard.views import SessionWizardView


@login_required(login_url="login")
def home(request):
	employee_con_var = Employee_Variable_Constant.objects.all()
	employee_uncon_var = Employee_Variable_Unconstant.objects.all()

	context = {
		'employee_con_var': employee_con_var,
		'employee_uncon_var': employee_uncon_var,
	}


	return render(request, 'dashboard.html', context)


def login(request):
	if request.method == "POST": 
		username = request.POST.get('username')
		password = request.POST.get('password')	

		user = authenticate(request, username=username , password=password)

		if user is not None:
			auth_login(request, user)
			return redirect("home")
		else:
			messages.info(request, "Invalid login or password")

	return render(request, "login.html")


def register(request):
	form = CreateUserForm()
	if request.method == "POST": 
		form = CreateUserForm(request.POST)	 

		if form.is_valid():	  
			username = form.cleaned_data.get('username')
			user_email = form.cleaned_data.get('email')	
			list_of_emails = []
			useres = User.objects.all()

			for user in useres:
				list_of_emails.append(user.email)

			if user_email in list_of_emails:
				messages.info(request, "Email already exist")
				return redirect("login")

			messages.success(request, "User"+" "+ username +" "+ "was created successfully" )
			user = form.save()
			return redirect("login")

	context = {
		"form": form,
	}

	return render(request, "register.html", context)


def logout(request):
	auth_logout(request)

	return redirect("login")


@login_required(login_url="login")
def del_emp(request, pk):
	emp_var_unconst = Employee_Variable_Unconstant.objects.get(id_employee=pk)

	if request.method == 'POST':
		if "Yes" in request.POST:
			emp_var_unconst.delete()	
			return redirect('/')	

		else:
			return redirect('/')

	context = {
		'emp_var_unconst': emp_var_unconst,
	}	

	return render(request, 'emp_delete.html', context)


class EmployeeWizard(LoginRequiredMixin, SessionWizardView):

	login_url = 'login'
	def done(self, form_list, form_dict, **kwargs):
		a = Employee_Variable_Constant(
				pesel = form_dict['0'].cleaned_data['pesel'],
				date_of_birth =  form_dict['0'].cleaned_data['date_of_birth'],
				place_of_birth = form_dict['0'].cleaned_data['place_of_birth'],
				fathers_name = form_dict['0'].cleaned_data['fathers_name'],
				mothers_name = form_dict['0'].cleaned_data['mothers_name'],
				mothers_family_name = form_dict['0'].cleaned_data['mothers_family_name'],
		)

		a.save()

		b = Employee_Variable_Unconstant(
				id_employee = a,
				name1 = form_dict['0'].cleaned_data['name1'],
				name2 = form_dict['0'].cleaned_data['name2'],
				surname = form_dict['0'].cleaned_data['surname'],
				gender = form_dict['0'].cleaned_data['gender'],
				doc = form_dict['0'].cleaned_data['doc'],
				nr_doc = form_dict['0'].cleaned_data['nr_doc'],
				nationality = form_dict['0'].cleaned_data['nationality'],
		)

		b.save()

		c = Address (
				id_employee = a,
				type_address = form_dict['1'].cleaned_data['type_address'],
				voivodeship = form_dict['1'].cleaned_data['voivodeship'],
				district = form_dict['1'].cleaned_data['district'],
				commune = form_dict['1'].cleaned_data['commune'],
				city = form_dict['1'].cleaned_data['city'],
				street = form_dict['1'].cleaned_data['street'],
				building_no = form_dict['1'].cleaned_data['building_no'],
				apartment_no = form_dict['1'].cleaned_data['apartment_no'],
				post = form_dict['1'].cleaned_data['post'],
				post_code = form_dict['1'].cleaned_data['post_code'],
		)

		c.save()


		var_supp = form_dict['2'].cleaned_data['list_of_profession']
		proffesion = ""
		code = ""
		v = 0 
		for x in var_supp:
			if x == "-":
				code = var_supp[v+2:]
				break
			else:
				proffesion += x
			v+=1


		d = Profession(
				id_employee = a,
				working_hours = form_dict['2'].cleaned_data['working_hours'],
				name_of_proffession = proffesion,
				code = code,
		)	

		d.save()

		e = Contract(
				id_employee = a,
				type_of_contract = form_dict['2'].cleaned_data['type_of_contract'],
				date_of_start_work = form_dict['2'].cleaned_data['date_of_start_work'],
				copyright_contract = form_dict['2'].cleaned_data['copyright_contract'],
				place_of_work = form_dict['2'].cleaned_data['place_of_work'],
				main_place_of_work = form_dict['2'].cleaned_data['main_place_of_work'],
				daily_norm = form_dict['2'].cleaned_data['daily_norm'],
				type_of_base_salary = form_dict['2'].cleaned_data['type_of_base_salary'],
				amount_of_base_salary = form_dict['2'].cleaned_data['amount_of_base_salary'],
				method_of_payment =  form_dict['2'].cleaned_data['method_of_payment'],
				account_number = form_dict['2'].cleaned_data['account_number'],
				type_of_perks = form_dict['2'].cleaned_data['type_of_perks'],
				amount_of_perks = form_dict['2'].cleaned_data['amount_of_perks'],
				conclusion_of_the_contract = form_dict['2'].cleaned_data['conclusion_of_the_contract'],
				company_representative = form_dict['2'].cleaned_data['company_representative'],
				contract_period = form_dict['2'].cleaned_data['contract_period'],
		)	

		e.save()

		return redirect('/')


@login_required(login_url="login")
def emp_show(request, pk):
	emp_show = Employee_Variable_Unconstant.objects.get(id_employee=pk)
	emp_address = Address.objects.filter(id_employee=pk)
	emp_profesion = Profession.objects.filter(id_employee=pk)

	contex = {
		'emp_show': emp_show,
		'emp_address': emp_address,
		'pk': pk,
		'emp_profesion' : emp_profesion,
	}

	return render(request, 'show_employee.html', contex)

	
@login_required(login_url="login")
def add_address(request, pk):
	address_add = Address_form()

	if request.method == 'POST':
		address_add = Address_form(request.POST)
		if address_add.is_valid():
			k = Employee_Variable_Constant.objects.get(id=pk)
			b = Address (
					id_employee = k,
					type_address = address_add.cleaned_data['type_address'],
					voivodeship = address_add.cleaned_data['voivodeship'],
					district = address_add.cleaned_data['district'],
					commune = address_add.cleaned_data['commune'],
					city = address_add.cleaned_data['city'],
					street = address_add.cleaned_data['street'],
					building_no = address_add.cleaned_data['building_no'],
					apartment_no = address_add.cleaned_data['apartment_no'],
					post = address_add.cleaned_data['post'],
					post_code = address_add.cleaned_data['post_code'],
				)
			b.save()
			return redirect('emp_show', pk=k.id)
		else:
			print(address_add.errors)

	context = {
		'address_add': address_add,
	}

	return render(request, 'address.html', context)


def address_del(request, pk3, pk_del):
	adr_emp = Address.objects.get(id=pk_del)

	if request.method == 'POST':
		if "Yes" in request.POST:
			adr_emp.delete()

			b = Address_ARC (
						id_employee = adr_emp.id_employee,
						type_address = adr_emp.type_address,
						voivodeship = adr_emp.voivodeship,
						district = adr_emp.district,
						commune = adr_emp.commune,
						city = adr_emp.city,
						street = adr_emp.street,
						building_no = adr_emp.building_no,
						apartment_no = adr_emp.apartment_no,
						post = adr_emp.post,
						post_code = adr_emp.post_code,
						date_of_entry = adr_emp.date_of_entry,
						type_of_change = "deleted",
				)
			b.save()			

			return redirect('emp_show', pk=adr_emp.id_employee.id) 
		else:
			return redirect('emp_show', pk=adr_emp.id_employee.id) 																	

	context = {
		'adr_emp': adr_emp,
		'text': 'Are you sure you want to delete address?',
	}	

	return render(request, 'emp_adr_delete.html',context)


def emp_edit_adr(request, pk2, pk_edit):
	adr_edit = Address.objects.get(id=pk_edit)
	adr_edit_arc = Address.objects.get(id=pk_edit)
	form = Address_form(instance=adr_edit)

	if request.method == 'POST':
		if "Save" in request.POST:
			form = Address_form(request.POST, instance=adr_edit)
			if form.is_valid():
				form.save()

				b = Address_ARC (
						id_employee = adr_edit_arc.id_employee,
						type_address = adr_edit_arc.type_address,
						voivodeship = adr_edit_arc.voivodeship,
						district = adr_edit_arc.district,
						commune = adr_edit_arc.commune,
						city = adr_edit_arc.city,
						street = adr_edit_arc.street,
						building_no = adr_edit_arc.building_no,
						apartment_no = adr_edit_arc.apartment_no,
						post = adr_edit_arc.post,
						post_code = adr_edit_arc.post_code,
						date_of_entry = adr_edit_arc.date_of_entry,
						type_of_change = "edited",
				)

				b.save()

				return redirect('emp_show', pk=adr_edit.id_employee.id)
			else:
				print(form.errors)	
		else:
			return redirect('emp_show', pk=adr_edit.id_employee.id)

	context = {
		'form': form,
	}	

	return render(request, 'address_editing.html',context)


def emp_adr_show(request, pk1, pk_show):
	adr_show = Address.objects.get(id=pk_show)
	emp_additional = Employee_Variable_Unconstant.objects.get(id_employee=pk1)

	if request.method == 'POST':
		return redirect('emp_show', pk=adr_show.id_employee.id)

	context = {
		'adr_show': adr_show,
		'emp_additional': emp_additional,
	}	

	return render(request, 'pokaz_adr.html', context)


def add_profesion(request, pk):
	list_of_prof = List_of_Profession.objects.all()
	emp_var_con = Employee_Variable_Constant.objects.get(id=pk)
	emp_var_uncon = Employee_Variable_Unconstant.objects.get(id_employee=pk)
	filter_list_of_profession = ProfessionFilter(request.GET, queryset=list_of_prof)
	list_of_prof = filter_list_of_profession.qs
	txt_zip = zip(list_of_prof, list_of_prof)
	profesion_form = List_of_Profession_Form(txt_zip=txt_zip)	

	if request.method == 'POST':
		if "Save" in request.POST:
			txt_zip = zip(list_of_prof, list_of_prof)	

			profesion_form = List_of_Profession_Form(request.POST, txt_zip=txt_zip)
			if profesion_form.is_valid():
				var_supp = profesion_form.cleaned_data['professions']
				proffesion = ""
				code = ""
				index = 0 
				for x in var_supp:
					if x == "-" and var_supp[index+1] == ' ':
						code = var_supp[index+2:]
						break
					else:
						proffesion += x
					index+=1

				d = Profession(
						id_employee = emp_var_con,
						working_hours = profesion_form.cleaned_data['working_hours'],
						name_of_proffession = proffesion,
						code = code,
					)	

				d.save()
				return redirect('emp_show', pk=pk)
			else:
				print(profesion_form.errors)
		else:
			return redirect('emp_show', pk=pk)

	context = {
		'list_of_prof': list_of_prof,
		'emp_var_con': emp_var_con,
		'emp_var_uncon': emp_var_uncon,
		'profesion_form': profesion_form,
		'filter_list_of_profession': filter_list_of_profession,	
	}	

	return render(request, 'profession.html', context)


def profession_del(request, pk, pk_del):
	del_profession = Profession.objects.get(id=pk_del)

	if request.method == 'POST':
		if "Yes" in request.POST:
			del_profession.delete()
			profession_save_arc = Profession_ARC (
						id_employee = del_profession.id_employee,
						date_of_entry = del_profession.date_of_entry,
						code = del_profession.code,
						name_of_proffession = del_profession.name_of_proffession,
						working_hours = del_profession.working_hours,
						type_of_change = "deleted",
				)
			profession_save_arc.save()			

			return redirect('emp_show', pk=del_profession.id_employee.id) 
		else:
			return redirect('emp_show', pk=del_profession.id_employee.id)	

	context = {
		'text': 'Are you sure you want to delete profession ?',
	}	

	return render(request, 'emp_adr_delete.html', context)


def edit_profession(request, pk, pk_edit):
	edit_profesion = Profession.objects.get(id=pk_edit)
	edit_profesion_arc = Profession.objects.get(id=pk_edit)

	list_of_prof = List_of_Profession.objects.all()
	emp_var_con = Employee_Variable_Constant.objects.get(id=pk)
	emp_var_uncon = Employee_Variable_Unconstant.objects.get(id_employee=pk)
	filter_list_of_profession = ProfessionFilter(request.GET, queryset=list_of_prof)
	list_of_prof = filter_list_of_profession.qs
	txt_zip = zip(list_of_prof, list_of_prof)
	profesion_form = List_of_Profession_Form(txt_zip=txt_zip)	

	if request.method == 'POST':
		if "Edit" in request.POST:
			txt_zip = zip(list_of_prof, list_of_prof)
			profesion_form = List_of_Profession_Form(request.POST, txt_zip=txt_zip)
			if profesion_form.is_valid():
				var_supp = profesion_form.cleaned_data['professions']
				proffesion = ""
				code = ""
				index = 0 
				for x in var_supp:
					if x == "-" and var_supp[index+1] ==' ':
						code = var_supp[index+2:]
						break
					else:
						proffesion += x
					index+=1
				edit_profesion.delete()

				a = Profession_ARC (
						id_employee = edit_profesion_arc.id_employee,
						date_of_entry = edit_profesion_arc.date_of_entry,
						code = edit_profesion_arc.code,
						name_of_proffession = edit_profesion_arc.name_of_proffession,
						working_hours = edit_profesion_arc.working_hours,
						type_of_change = "edited",
					)

				a.save()

				b = Profession(
						id_employee = emp_var_con,
						code = code,
						name_of_proffession = proffesion,
						working_hours = profesion_form.cleaned_data['working_hours']
					)

				b.save()

				return redirect('emp_show', pk=edit_profesion.id_employee.id)

			else:
				print('walidacja niedziała')
				print(profesion_form.errors)

		else:
			return redirect('emp_show', pk=edit_profesion.id_employee.id)

	context = {
		'list_of_prof': list_of_prof,
		'filter_list_of_profession': filter_list_of_profession,
		'emp_var_uncon': emp_var_uncon,
		'profesion_form': profesion_form,
		'edit_profesion': edit_profesion,
	}

	return render(request, 'profession.html', context)


def edit_general_inf(request, pk):
	emp_var_uncon = Employee_Variable_Unconstant.objects.get(id_employee=pk)
	emp_var_uncon_arc = Employee_Variable_Unconstant.objects.get(id_employee=pk)
	emp_var_uncon_form = Employee_edit_form(instance=emp_var_uncon)

	if request.method == 'POST':
		print('Metoda POST')
		if "Save change" in request.POST:
			emp_var_uncon_form = Employee_edit_form(request.POST, instance=emp_var_uncon)
			print('po save change')
			if emp_var_uncon_form.is_valid():
				print('walidacja OK')
				emp_var_uncon_form.save()

				save_emp_var_uncon_arc = Employee_Variable_Unconstant_ARC(name1 = emp_var_uncon_arc.name1,
									  name2 = emp_var_uncon_arc.name2,
									  surname = emp_var_uncon_arc.surname,
									  gender = emp_var_uncon_arc.gender,
									  doc = emp_var_uncon_arc.doc,
									  nr_doc = emp_var_uncon_arc.nr_doc,
									  nationality = emp_var_uncon_arc.nationality,
									  date_of_entry = emp_var_uncon_arc.date_of_entry,
									  id_employee = emp_var_uncon_arc.id_employee
				)

				save_emp_var_uncon_arc.save()

				return redirect("emp_show", pk=pk)
			else:
				print(emp_var_uncon_form.errors)
		else:
			return redirect("emp_show", pk=pk)


	context = {
		'emp_var_uncon_form': emp_var_uncon_form,
	}	

	return render(request, 'edit_employee_uncon.html',context)


def show_emp_history(request,pk):
	emp_uncons = Employee_Variable_Unconstant.objects.get(id_employee=pk)
	emp_uncons_arc = Employee_Variable_Unconstant_ARC.objects.filter(id_employee=pk)
	emp_address = Address_ARC.objects.filter(id_employee=pk)
	emp_profession = Profession_ARC.objects.filter(id_employee=pk)

	if request.method == 'POST':
		if "Return" in request.POST:
			return redirect("emp_show", pk=pk)

	context = {
		'emp_uncons': emp_uncons,
		'emp_uncons_arc': emp_uncons_arc,
		'emp_address': emp_address,
		'emp_profession': emp_profession
	}	

	return render(request, 'show_emp_history.html',context)








