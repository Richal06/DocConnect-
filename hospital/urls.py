
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.About,name="About"),
    path('contact/', views.contact,name="contact"),
    path('', views.Home,name="Home"),
    path('admin_login/', views.Login,name="login"),
    path('logout/', views.Logout_admin,name="logout_admin"),
    path('admin_pag/', views.Index,name="ad_page"),
    path('View_doctor/', views.View_doctor,name="View_doctor"),
    # path('delete_doctor(?P<int:pid)/', views.delete_doctor,name="delete_doctor"),
    path('delete_doctor/<int:pid>/', views.delete_doctor, name='delete_doctor'),
    path('add_doctor', views.Add_doctor, name='add_doctor'),
    path('View_patient/', views.view_patient,name="View_pateint"),
    path('delete_patient/<int:pid>/', views.delete_patient, name='delete_patient'),
    path('add_patient', views.Add_patient, name='add_patient'),
    path('View_appointment/', views.View_appointment,name="View_appointment"),
    path('delete_appointment/<int:pid>/', views.delete_appointment, name='delete_appointment'),
    path('add_appointment', views.Add_appointment, name='add_appointment'),
    path('signup/', views.doctor_signup, name='doctor_signup'),
    path('doctor_login/', views.doctor_login, name='doctor_login'),
    path('dindex/', views.dindex, name='dindex'),
    path('pindex/', views.pindex, name='pindex'),
    path('doctor_logout/', views.doctor_logout,name="logout_doc"),
    path('patient_signup/', views.patient_signup, name='doctor_signup'),
    path('patient_login/',views.patient_login,name='patient_login')
]