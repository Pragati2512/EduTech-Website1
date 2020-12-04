from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import UserForm, RegisterForm, StudentForm, TeacherForm, DoubtForm
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.forms import AuthenticationForm
from .models import person, teacher, student, doubt


def home(request):
    if request.user.is_authenticated:
        uss = request.user
        prsn = person.objects.get(user=uss)
        return render(request, 'index.html', {"prsn": prsn,} )
    else :
        return render(request, 'index.html')


def login_request(request):
    message = ''
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                message = "Success: You are now logged in. "
                uss = request.user
                prsn = person.objects.get(user=uss)
                return render(request, 'index.html',{"message": message,"prsn": prsn,})
            else:
                message = "Error: Invalid Username or Password."
        else:
            message = "Error: Invalid Username or Password."
    form = AuthenticationForm()
    context = {"form": form, "message": message, }
    return render(  request = request, template_name = "registration/login.html", context=context)


def logout_request(request):
    logout(request)
    message = "Logged out successfully!"
    return render(request, 'index.html', {"message": message, })


def register_st(request):
    form1 = RegisterForm()
    form2 = StudentForm()
    if request.method == 'POST':
        userName = request.POST.get('username', None)
        userPass = request.POST.get('password', None)
        user1 = User.objects.create_user(username=userName, password=userPass)
        form1 = RegisterForm(request.POST)
        form2 = StudentForm(request.POST)
        if form1.is_valid() and form2.is_valid() :
            prs = form1.save(False)
            prs.user = user1
            prs.user_type = "Student"
            form1.save(True)
            stud = form2.save(False)
            stud.prsn = prs
            form2.save(True)
            return render(request, 'index.html' )
        message = 'ERROR !! Could not register. Please try again. '
        return render(request,  'index.html', {'message': message })
    return render(request, 'person/student_form.html')



def doubt_form(request):
    form1 = DoubtForm()
    if request.method == 'POST':
        form1 = DoubtForm(request.POST)
        if form1.is_valid() :
            doubt = form1.save(False)
            doubt.student = person.objects.get(user=request.user)
            form1.save(True)
            return render(request, 'index.html' )
        message = 'ERROR !! Could not submit question . Please try again. '
        return render(request,  'index.html', {'message': message })
    return render(request, 'person/doubt_form.html')




def my_doubts(request):
    stud = person.objects.get(user=request.user)
    list1 = doubt.objects.filter(student=stud)
    return render(request, 'person/my_doubts.html', { 'doubts1' : list1} )


'''
def view_profile(request):
    prsn = person.objects.get(user=request.user)
    if prsn.user_type == "Student":
        stud = student.objects.get(prsn=prsn)
        sec = stud.section
        if sec == "SM":
            sec = "Science-Maths"
        elif sec == "SB":
            sec = "Science-Bio"
        elif sec == "CM":
            sec = "Commerce(Maths)"
        elif sec == "CT":
            sec = "Commerce(Type)"
        return render(request, 'person/profile_stud.html', {'prsn': prsn, 'standard': stud.standard, 'sec': sec, })
    elif prsn.user_type == "Teacher":
        tech = teacher.objects.get(prsn=prsn)
        g = grade.objects.filter(class_teacher=tech).count()
        ct = "Not Class Teacher"
        if g>0 :
            ctec = grade.objects.get(class_teacher=tech)
            ct = ctec.standard + " " + ctec.section
        return render(request, 'person/profile_tech.html', {'prsn': prsn, 'sub': tech.subject , 'ct' : ct })
'''