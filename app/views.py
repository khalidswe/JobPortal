from email import message, message_from_binary_file
from pyexpat.errors import messages
import re
from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from . models import *
from random import randint
from django.contrib.auth import logout

# Create your views here.

def IndexPage(request):
    return render(request,"app/index.html")

def HomePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    
    can = Candidate.objects.get(user_id=user)
    return render(request,"app/homepage.html",{'user':user,'can':can})


def SignUpPage(request):
    return render(request,"app/signup.html")

def UserRegistration(request):
    if request.POST['role']=="Candidate":
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email) #here we can check email

        if user :
            message = "User already exist!!"
            return render(request,"app/signup.html",{'msg':message})
        else:
            if password == cpassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcand=Candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                return render(request,"app/otpverify.html",{'email':email})
            else:
                message = "Password doesn't Match!!"
                return render(request,"app/signup.html",{'msg':message})
    
    elif request.POST['role']=="Company":
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)

        if user :
            message = "User already exist!!"
            return render(request,"app/signup.html",{'msg':message})
        else:
            if password == cpassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcand=Company.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                return render(request,"app/otpverify.html",{'email':email})
            else:
                message = "Password doesn't Match!!"
                return render(request,"app/signup.html",{'msg':message})
    else:
        message = "Please Select Your role!"
        return render(request,"app/signup.html",{'msg':message})
        

def OTPPage(request):
    return render(request,"app/otpverify.html")

def OTPverify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.get(email=email)

    if user:
        if user.otp == otp:
            message = "OTP verified Successfully!!"
            return render(request,"app/login.html",{'msg':message})
        else:
            message = "OTP is incorrect!!"
            return render(request,"app/otpverify.html",{'msg':message})
    else:
        message = "Enter Your OTP Code"
        return render(request,"app/otpverify.html",{'msg':message})

# def LogInPage(request):
#     return render(request,"app/login.html")

def LogInUser(request):
            if request.POST['role']=="Candidate":
                email = request.POST['email']
                password = request.POST['password']
 
                user = UserMaster.objects.get(email=email) 

                if user:
                    if user.password == password and user.role=="Candidate":
                        can = Candidate.objects.get(user_id=user) #can = candidate
                        request.session['id']=user.id
                        request.session['email']=user.email
                        request.session['role']=user.role
                        request.session['firstname']= can.firstname
                        request.session['lastname']=can.lastname

                        return render(request,"app/homepage.html",{'user':user,'can':can})
                
                    else:
                        message = "Password doesn't Match!!"
                        return render(request,"app/index.html",{'msg':message})
                else:
                    message = "User doesn't Exist!!"
                    return render(request,"app/index.html",{'msg':message})
            
            elif request.POST['role']=="Company":
                email = request.POST['email']
                password = request.POST['password']
 
                user = UserMaster.objects.get(email=email) #just check email same or not

                if user:
                    if user.password == password and user.role=="Company":
                        comp = Company.objects.get(user_id=user)
                        request.session['id']=user.id #comp = company
                        request.session['email']=user.email
                        request.session['role']=user.role
                        request.session['firstname']= comp.firstname
                        request.session['lastname']=comp.lastname

                        return render(request,"app/company/index.html",{'user':user,'comp':comp})
                
                    else:
                        message = "Password doesn't Match!!"
                        return render(request,"app/index.html",{'msg':message})
                else:
                    message = "User doesn't Exist!!"
                    return render(request,"app/index.html",{'msg':message})
            else:
                message = "Select Role!!"   
                return render(request,"app/index.html",{'msg':message})

def ProfilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)
        return render(request,"app/profile-candidate.html",{'user':user,'can':can})
    elif user.role == "Company": 
        comp = Company.objects.get(user_id=user)
        return render(request,"app/company/profile-company.html",{'user':user,'comp':comp})

def EditProfileView(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)
        return render(request,"app/edit-profile-candidate.html",{'user':user,'can':can})
    elif user.role == "Company":
        comp = Company.objects.get(user_id=user) 
        return render(request,"app/company/edit-profile-company.html",{'user':user,'comp':comp})

def UpdateProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)
        can.firstname=request.POST['firstname']
        can.lastname=request.POST['lastname']
        can.contact = request.POST['contact']
        can.dob= request.POST['dob']
        can.gender = request.POST['gender']
        can.maritual_status=request.POST['maritual_status']
        can.portfolio=request.POST['portfolio']
        can.address = request.POST['address']
        can.state= request.POST['state']
        can.city= request.POST['city']
        can.country = request.POST['country']
        can.uni_college1=request.POST['uni_college1']
        can.major1=request.POST['major1']
        can.degree1=request.POST['degree1']
        can.sgpa1=request.POST['sgpa1']
        can.uni_college2=request.POST['uni_college2']
        can.major2=request.POST['major2']
        can.degree2=request.POST['degree2']
        can.sgpa2=request.POST['sgpa2']
        can.skill=request.POST['skill']
        can.additional_skill=request.POST['additional_skill']
        can.profile_pic =request.FILES['image']
        can.save()
        url= f'/profilecandidate/{pk}' # formating url
        return redirect(url)
    elif user.role == "Company":
        comp = Company.objects.get(user_id=user)
        comp.firstname=request.POST['firstname']
        comp.lastname=request.POST['lastname']
        comp.contact = request.POST['contact']
        comp.website=request.POST['website']
        comp.address = request.POST['address']
        comp.state= request.POST['state']
        comp.city= request.POST['city']
        comp.country = request.POST['country']
        comp.about_us=request.POST['about_us']
        comp.services=request.POST['services']
        comp.logo=request.FILES['image']
        comp.save()
        url= f'/profilecompany/{pk}' # formating url
        return redirect(url)

        
def LogOut(request,pk):
    user = UserMaster.objects.get(pk=pk)
    logout(request)
    message = "Logged out successfully!"
    return render(request,"app/index.html",{'msg':message})

def AboutPage(request):
    return render(request,"app/about.html")

def UnderContructionPage(request):
    return render(request,"app/pageunderconstruction.html")

def JobListPageCandidate(request):

    all_jobs = JobDetails.objects.all()
    return render(request,"app/joblist_candidate.html",{'all_jobs':all_jobs})

def JobDetailsPage(request):
    comp = Company.objects.all()
    job = JobDetails.objects.all()
    
    return render(request,"app/job_details.html",{'job':job,'comp':comp})

####### Company side #######

def CompanyIndexPage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user :
        return render(request,"app/company/index.html",{'user':user})


def JobListPage(request,pk):
    user = UserMaster.objects.get(pk=12)
    
    comp = Company.objects.get(user_id=user)
    job = JobDetails.objects.filter(company_id=comp)
    if job:
        all_jobs = JobDetails.objects.all()
        return render(request,"app/company/joblist.html",{'all_jobs':all_jobs})
    # else:
    #     return render(request,"app/company/joblist.html")

def PostAJobPage(request,pk):
    user = UserMaster.objects.get(id=pk)
    if user:
        comp= Company.objects.get(user_id=user)
        return render(request,"app/company/post_a_job.html",{'user':user,'comp':comp})

def PostAJob(request,pk):
    user = UserMaster.objects.get(pk=pk)
    
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        jobname = request.POST['jobname']
        job_position = request.POST['job_position']
        company_name = request.POST['company_name']
        company_email = request.POST['company_email']
        contact =request.POST['contact']
        company_website=request.POST['company_website']
        location=request.POST['location']
        job_context=request.POST['job_context']
        responsibilities=request.POST['responsibilities']
        qualification=request.POST['qualification']
        employement_status=request.POST['employement_status']
        experience=request.POST['experience']
        vacancy  = request.POST['vacancy']
        salary = request.POST['salary']
        apply_deadline = request.POST['apply_deadline']
        job_logo =request.FILES['job_logo']
        
        newjob = JobDetails.objects.create(company_id=comp,jobname=jobname,job_position=job_position,company_name=company_name,company_email=company_email,
        contact=contact,company_website=company_website,location=location,job_context=job_context,responsibilities=responsibilities,
        qualification=qualification,employement_status=employement_status,experience=experience,vacancy=vacancy,
        salary=salary,apply_deadline=apply_deadline,job_logo=job_logo)

        message = "Job Posted Successfully"

        return render(request,"app/company/joblist.html",{'msg':message})