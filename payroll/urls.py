from django.contrib import admin
from django.urls import path
from payroll_app.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('login', login, name='login'),
    path('logout', logout,  name='logout'),
    path('creator_wizard/', 
            EmployeeWizard.as_view([NewEmployee, Address_form, Contract_form_creator]), 
            name='creator_wizard'),
    path('del_emp/<str:pk>/', del_emp, name="del_emp"),
    path('emp_show/<str:pk>/', emp_show, name="emp_show"),
    path('register', register, name='register'),

    path('emp_show/<str:pk>/address', add_address, name="add_address"),
    path('emp_show/<str:pk3>/<str:pk_del>/delete/', address_del, name="del_adr"),
    path('emp_show/<str:pk2>/<str:pk_edit>edit_adr/', emp_edit_adr, name="edit_adr"),
    path('emp_show/<str:pk1>/<str:pk_show>show/', emp_adr_show, name="show_adr"),

    path('emp_show/<str:pk>/add_profession/', add_profesion, name='add_profession'),
    path('emp_show/<str:pk>/<str:pk_del>/profession_del/', profession_del, name="profession_del"),
    path('emp_show/<str:pk>/<str:pk_edit>/edit_profession/', edit_profession, name="edit_profession"),
    path('emp_show/<str:pk>/edit_general_inf', edit_general_inf, name="edit_general_inf"),
    path('emp_show/<str:pk>/show_emp_history', show_emp_history, name="show_emp_history"),

    #changing password
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="password_reset.html"), name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="password_reset_sent.html"), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_form.html"), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset_done.html"), name= 'password_reset_complete'),
]
