from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login
from .views import *
from .forms import LoginForm

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login,logout
from .views import *
from .forms import LoginForm


urlpatterns = [
    url(r'^links/(?P<username>\w{0,50})',link_view), #List Page which would be shared by any user
    url(r'^sign_up', sign_up,name='sign_up'), #SignUp Page,redirect action page=Add a Link
    url(r'^referral/(?P<username>\w{0,50})',sign_up_referral, name="referral_sign_up"),
    url(r'^home_page/',home_view , name="home_page"),
    url(r'^link_update/(?P<link>\w{0,50})', link_update , name= 'link_add'), #Add a new Link to a user, user should be authenticated to view this
    url(r'^logout/', logout_view, name='logout'),
    url(r'^', login_view, name='login'), #Login Form Authentication
    

]
