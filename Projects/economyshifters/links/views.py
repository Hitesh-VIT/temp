from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from links.models import *
from links.forms import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.



def logout_view(request):
    logout(request)
    return redirect("login")




def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None and user.is_active:
			login(request, user)
			return redirect("home_page")
		return redirect("login")
	form = LoginForm()
	link=Links.objects.all()
	return render(request, 'index.html', {'login_form': LoginForm,'link':link})


def sign_up(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			try:
				user=User.objects.create_user(
					username=form.cleaned_data['username'],
					password=form.cleaned_data['password'],
					email=form.cleaned_data['email'])
				login(request,user)
				return  redirect("home_page")
			except :
				form = SignUpForm()
				return render(request, 'signup.html' , {'errors':'This Username has already been taken','form':form}) #To show a wrong username
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})



def sign_up_referral(request,username):
	referral_user=get_object_or_404(User,username=username)
	#referral_user=User.objects.get(username=username)

	if request.method == "POST":
		form=SignUpForm(request.POST)
		if form.is_valid():
			try:

				user =User.objects.create_user(
					username=form.cleaned_data['username'],
					password=form.cleaned_data['password'],
					email=form.cleaned_data['email'])

				User_referral_obj=User_refferal.objects.create(Main_user=user,Referred_user=referral_user)
				User_referral_obj.save()
				login(request,user)
				return redirect('home_page')
			except:
				form=SignUpForm()
				return render(request, 'signup.html',{'form':form,'errors':'This username has already been taken'})
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})



@login_required(login_url="/login")
def link_update(request,link):
	if request.method ==  "POST" :
		link=Links.objects.get(id=link)          #Get the link id
		try:
			s=Link_Info.objects.get(user=request.user, link=link)  #Update Referral
			form = LinkForm(request.POST,instance=s)
		except ObjectDoesNotExist:
			form= LinkForm(request.POST)							#Add a new Referral


		if form.is_valid():
			link_user=form.save(commit=False)
			link_user.user=request.user
			link_user.link=link
			link_user.save()
			return HttpResponseRedirect('/links/'+request.user.username)
	else:
		form = LinkForm()
	return render(request, 'Link_add.html' , {'form': form})

def link_view(request, username):											#Page that could be shared by everyone
	user=User.objects.get(username=username) 								#Contains a list of urls which contain all the links with default referral_id or user assigned
	links=Links.objects.all()
	test_user=request.user
	try:
		link_user=Link_Info.objects.filter(user=user)
		link_user_list=link_user.values_list('link',flat='True')
		links_default=Links.objects.exclude(id__in=list(link_user_list))
		return render(request, 'list.html', {'link':links_default,'default_link':link_user,'user':user,'test_user':test_user})
	except ObjectDoesNotExist:
		return render(request, 'list.html', {'link':link,'user':user,'test_user':test_user})






@login_required(login_url="/")
def home_view(request):
	user=request.user
	link=Links.objects.all()
	try:
		refferal_user=User_refferal.objects.get(Main_user=user).Referred_user
		link_user=Link_Info.objects.filter(user=refferal_user)
		link_user_list=link_user.values_list('link',flat='True')
		links_default=Links.objects.exclude(id__in=list(link_user_list))
		return render(request, 'home.html', {'link':links_default,'default_link':link_user})
	except ObjectDoesNotExist:
		return render(request, 'home.html', {'link':link})





def index(request):
	link=Links.objects.all()
	return render(request , 'index.html', {'link':link})







