from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("signup/",views.SignUpPage,name="signup"),
    path("homepage/<int:pk>",views.HomePage,name="homepage"),
    path("register/",views.UserRegistration,name="register"),
    path("otppage/",views.OTPPage,name="otppage"),
    path("otpverify/",views.OTPverify,name="otpverify"),
    #path("login/",views.LogInPage,name="login"),
    path("home/",views.LogInUser,name='home'),
    path("profilecandidate/<int:pk>",views.ProfilePage,name='profilecandidate'),
    path("profilecompany/<int:pk>",views.ProfilePage,name='profilecompany'),
    path("editprofileview/<int:pk>",views.EditProfileView,name='editprofileview'),
    path("updateprofile/<int:pk>",views.UpdateProfile,name='updateprofile'),
    path("logout/<int:pk>",views.LogOut,name='logout'),
    path("aboutpage",views.AboutPage,name='aboutpage'),
    path("pageunderconstructions",views.UnderContructionPage,name='pageunderconstructions'),
    path("joblistpagecandidate",views.JobListPageCandidate,name='joblistpagecandidate'),
    path("jobdetailspage",views.JobDetailsPage,name="jobdetailspage"),


    ####### Company side #######
    
    path("companyindex/<int:pk>",views.CompanyIndexPage,name="companyindex"),
    path("joblistpage/<int:pk>",views.JobListPage,name='joblistpage'),
    path("postajobpage/<int:pk>",views.PostAJobPage,name='postajobpage'),
    path("postajob/<int:pk>",views.PostAJob,name="postajob"),
    

]
 