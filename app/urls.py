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
    path("aboutpage/",views.AboutPage,name='aboutpage'),
    path("pageunderconstructions/",views.UnderContructionPage,name='pageunderconstructions'),
    path("joblistpagecandidate/",views.JobListPageCandidate,name='joblistpagecandidate'),
    path("jobdetailspage/",views.JobDetailsPage,name="jobdetailspage"),
    path("applyjobpage/<int:pk>",views.ApplyJobPage,name="applyjobpage"),
    path("applyjob/<int:pk>",views.Applyjob,name="applyjob"),


    ####### Company side #######
    
    path("companyindex/<int:pk>",views.CompanyIndexPage,name="companyindex"),
    path("joblistpage/<int:pk>",views.JobListPage,name='joblistpage'),
    path("postajobpage/<int:pk>",views.PostAJobPage,name='postajobpage'),
    path("postajob/<int:pk>",views.PostAJob,name="postajob"),
    path("appliedjoblist/<int:pk>",views.AppliedJobList,name="appliedjoblist"),

    ####### Admin side #######

    #path("adminpage/",views.AdminRegister,name="adminpage"),
    path("adminpage/",views.AdminLogInPage,name="adminpage"),
    path("adminindex/",views.AdminIndex,name="adminindex"),
    path("logoutadmin/",views.LogOut,name='logoutadmin'),
    path("adminlogin/",views.AdminLogIn,name="adminlogin"),
    path("candidatelist/",views.CadidateList,name="candidatelist"),
    path("companylist/",views.CompanyList,name="companylist"),
    path("candidatedelete/<int:pk>",views.UserDelete,name="candidatedelete"),
    path("companydelete/<int:pk>",views.CompanyDelete,name="companydelete"),
    path("verifycompanypage/<int:pk>",views.VerifyCompanyPage,name="verifycompanypage"),
    path("verifycompany/<int:pk>",views.VerifyCompany,name="verifycompany"),


]   
 