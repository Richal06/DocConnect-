from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Doctor,Patient,Appointment


from django.contrib.auth.decorators import login_required

# Create your views here.
def About(request):
    return render(request ,'about.html')
def Home(request):
    return render(request ,'home.html')
def contact(request):
    return render(request ,'contact.html')

# def Index(request):
#     if not request.user.is_staff:
#         return redirect('login')
#     doctors = Doctor.objects.all()
#     patient= Patient.objects.all()
#     appointment = Appointment.objects.all()

#     d=0
#     p=0
#     a=0
#     for i in doctors:
#         d+=1
#     for i in patient:
#         p+=1
#     for i in appointment:
#         a+=1
#     d1 = {'d':d, 'p':p,'a':a}

#     return render(request, 'index.html')
from django.shortcuts import render

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()

    d = doctors.count()
    p = patient.count()
    a = appointment.count()

    d1 = {'d': d, 'p': p, 'a': a}
    
    return render(request, 'index6.html', {'d': d1})


def Login(request):
    error=""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password= p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"

            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'login1.html',d)

def Logout_admin(request):
    if not request.user.is_staff and not hasattr(request.user, 'doctor') and not hasattr(request.user, 'patient'):
    

        return redirect('login')

    logout(request)
    return redirect('login')

def View_doctor(request):
    doc = Doctor.objects.all()
    d = {'doc' : doc}
    return render(request , 'view_doctor.html',d)

def delete_doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id = pid)
    doctor.delete()
    
    
    return redirect('View_doctor')



def Add_doctor(request):
    error = ""

    # Remove the user authentication check for simplicity
    # if not request.user.is_staff:
    #     return redirect('login')

    if request.method == "POST":
        e = request.POST['name']
        m = request.POST['mobile']
        sp = request.POST['Special']
        
        try:
            # Ensure the 'Name' field in Doctor model is unique
            Doctor.objects.create(Name=e, mobile=m, Special=sp)
            error = "no"
        except Exception as e:
            print(f"An error occurred: {e}")
            error = "yes"

    d = {'error': error}
    return render(request, 'add_doctor.html', d)

# def Add_doctor(request):
#     error=""
#     if not request.user.is_staff:
#         return redirect('login')

#     if request.method == "POST":
#         e = request.POST['name']
#         m = request.POST['mobile']
#         sp = request.POST['Special']
        
#         try:
#             print("hello")
#             Doctor.objects.get_or_create(Name=e,mobile=m,Special=sp)
#             error = "no"

           
#         except:
#             error = "yes"
        

    
#     d = {'error':error}
#     return render(request,'add_doctor.html',d)


# def Add_doctor(request):
#     error = ""
#     if not request.user.is_staff:
#         return redirect('login')

#     if request.method == "POST":
#         e = request.POST.get('name', '')
#         m = request.POST.get('mobile', '')
#         sp = request.POST.get('special', '')

#         if e and m and sp:
#             try:
#                 Doctor.objects.create(name=e, mobile=m, special=sp)
#                 error = "no"
#             except Exception as e:
#                 # Handle the exception, e.g., log it or return an error message.
#                 error = "An error occurred while creating the doctor."
#         else:
#             error = "Please provide all the required information."

#     d = {'error': error}
#     return render(request, 'add_doctor.html', d)

def view_patient(request):
    if not request.user.is_staff and not hasattr(request.user, 'doctor'):
        return redirect('login')
    doc = Patient.objects.all()
    d = {'doc' : doc}
    return render(request , 'view_patient.html',d)

def delete_patient(request, pid):
    if not request.user.is_staff and not hasattr(request.user, 'doctor'):
        return redirect('login')
    patient = Patient.objects.get(id = pid)
    patient.delete()
    
    
    return render(request ,'view_patient.html')

def Add_patient(request):
    error=""
    if not request.user.is_staff and not hasattr(request.user, 'doctor'):
        return redirect('login')

    if request.method == "POST":
        e = request.POST['name']
        m = request.POST['mobile']
        g = request.POST['gender']
        h = request.POST['Problem']
        j = request.POST['address']
        
        try:
            print("hello")
            Patient.objects.get_or_create(Name=e,mobile=m,gender=g,problem=h,address=j)
            error = "no"

           
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'add_patient.html',d)
from django.shortcuts import render, redirect
from .models import Doctor, Patient, Appointment

def Add_appointment(request):
    error = ""
    
    if not request.user.is_staff and not hasattr(request.user, 'doctor') and not hasattr(request.user, 'patient'):
        return redirect('login')
    
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()

    if request.method == "POST":
        doctor_name = request.POST['doctor']
        patient_name = request.POST['patient']
        date = request.POST['date']
        time = request.POST['time']

        doctor = Doctor.objects.filter(Name=doctor_name).first()
        patient = Patient.objects.filter(Name=patient_name).first()

        try:
            appointment, created = Appointment.objects.get_or_create(doctor=doctor, patient=patient, date=date, time=time)
            
            if created:
                error = "no"
            else:
                error = "yes"  # Appointment already exists
            
        except Exception as e:
            print(f"An error occurred: {e}")
            error = "yes"

    context = {'doctors': doctors, 'patients': patients, 'error': error}
    return render(request, 'add_appointment.html', context)

# def Add_appointment(request):
#     error=""
#     if not request.user.is_staff and not hasattr(request.user, 'doctor') and not hasattr(request.user, 'patient'):

#         return redirect('login')
#     doctor1=Doctor.objects.all()
#     patient1=Patient.objects.all()

#     if request.method == "POST":
#         n = request.POST['doctor']
#         p = request.POST['patient']
#         g = request.POST['date']
#         h = request.POST['time']
#         doctor = Doctor.objects.filter(Name=n).first()
#         patient = Patient.objects.filter(Name=p).first()
    
        
#         try:
#             print("hello")
#             Appointment.objects.get_or_create(doctor=n,patient=p,date=g,time=h)
#             print("hello")
#             error = "no"

           
#         except:
#             error = "yes"
#     d = {'doctor': doctor1 , 'patient': patient1, 'error':error}
#     return render(request,'add_appointment.html',d)

def View_appointment(request):
    doc = Appointment.objects.all()
    d = {'doc' : doc}
    return render(request , 'view_appointment.html',d)

def delete_appointment(request, pid):
    if not request.user.is_staff and not hasattr(request.user, 'doctor'):
        return redirect('login')
    app = Appointment.objects.get(id = pid)
    app.delete()
    return redirect('View_appointment')

# def doctor_signup(request):
#     error=""
#     if request.method == "POST":
#         g = request.POST['name']
#         h = request.POST['mobile']
#         q = request.POST['yoe']
#         s = request.POST['specialization']
        

        
#         try:
#             print("hello")
#             Doctor.objects.get_or_create(Name=g,mobile=h,yoe=q,Special=s)
#             error = "no"

            
#         except:
#             error = "yes"
#     d = {'error':error}
    
#     return render(request ,'doctor_signup.html',d)


def doctor_signup(request):
    error = ""
    if request.method == "POST":
        # Retrieve data from the form
        name = request.POST['name']
        mobile = request.POST['mobile']
        yoe = request.POST['yoe']
        specialization = request.POST['specialization']
        username = request.POST['username']
        password = request.POST['password']

        try:
            # Create a user
            user = User.objects.create_user(username, password=password)
            
            # Create a doctor associated with the user
            doctor = Doctor.objects.create(user=user, Name=name, mobile=mobile, yoe=yoe, Special=specialization)
            
            error = "no"  # No error if successful
            
        except:
            error = "yes"  # If there's an issue

    d = {'error': error}
    return render(request, 'doctor_signup.html', d)





def doctor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            try:
                
                doctor = Doctor.objects.get(user__username=username)
                user = authenticate(request, username=doctor.user.username, password=password)
                if user is not None:
                    login(request, user)
                    # Redirect to a success page or any other page after login
                    return redirect('/hospital/dindex')  # Change 'success_page' to your desired URL name
                else:
                    # Return an invalid login message
                    messages.error(request, 'Invalid username or password')
            except Doctor.DoesNotExist:
                # Return an invalid login message if the Doctor doesn't exist
                messages.error(request, 'Invalid username or password')
        else:
            # Handle if username or password is empty
            messages.error(request, 'Please provide both username and password')

    return render(request, 'doctor_login.html')

def dindex(request):
    
    
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()

    p = patient.count()
    a = appointment.count()

    d1 = { 'p': p, 'a': a}
    
    return render(request, 'doctor.index.html', {'d': d1})
    
def pindex(request):
    appointment = Appointment.objects.all()
    a=appointment.count()
    

    d1 = { 'a': a}
    
    return render(request, 'pinndex.html',{'d': d1})
def doctor_logout(request):
    if not request.user.is_staff:
        return redirect('login')

    logout(request)
    return redirect('doctor_login')

def patient_signup(request):
    error = ""
    if request.method == "POST":
        # Retrieve data from the form
        name = request.POST['name']
        mobile = request.POST['mobile']
        yoe = request.POST['yoe']
        address = request.POST['address']
        specialization = request.POST['specialization']
        username = request.POST['username']
        password = request.POST['password']

        try:
            # Create a user
            user = User.objects.create_user(username, password=password)
            
            # Create a patient associated with the user
            patient = Patient.objects.create(user=user, Name=name, mobile=mobile, problem=yoe, gender=specialization, address=address)
            
            error = "no"  # No error if successful
            
        except Exception as e:
            print(f"An error occurred: {e}")
            error = "yes"  # If there's an issue

    d = {'error': error}
    return render(request, 'patient_signup.html', d)

def patient_login(request):
    error = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login the user
            login(request, user)
            error = "no"  # No error if successful
        else:
            error = "yes"  # Invalid login

    d = {'error': error}
    return render(request, 'patient_login.html', d)