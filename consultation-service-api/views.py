from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from django.http import HttpResponse
from .forms import UserRegistrationForm, DiagnosisForm
from .forms import CaseForm
from .models import Caselist
from django.shortcuts import redirect
from .extract_tags import ExtractTags
extract_tags = ExtractTags(lang='english')

# Create your views here.
def home(request):
    #return render(request, 'helper/home.html')
    if request.user.get_username()=='assistant':
    	return render(request, 'helper/homeassist.html', {'tags':extract_tags.tags})
    else:
	    if request.method == "POST":
	        form = CaseForm(request.POST)
	        if form.is_valid():
	            post = form.save(commit=False)
	            post.patientid = request.user
	            post.groupname = ', '.join(extract_tags.get_tags(post.symptoms))
	            post.save()
	            return redirect('redirectto')
	    else:
	        form = CaseForm()
	    return render(request, 'helper/home.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'helper/register.html', {'form' : form})

def redirectto(request):
	return render(request, 'helper/redirect.html')

def history(request):
	try:
		case_history = Caselist.objects.filter(patientid = request.user.get_username())
		print(case_history)
		return render(request, 'helper/history.html', {'history': case_history})
	except Caselist.DoesNotExist:
		raise Http404

def homeassist(request):
	if request.user.get_username()=='assistant':
		return render(request, 'helper/homeassist.html', {'tags':extract_tags.tags})
	else:
		return HttpResponse("You are not authorized to view this information")

def allcases(request):
	if request.user.get_username()=='assistant':
		try:
			cases = Caselist.objects.all()
			print(cases)
			return render(request, 'helper/allcases.html', {'allcases': cases})
		except Caselist.DoesNotExist:
			raise Http404
	else:
		return HttpResponse("You are not authorized to view this information")

def casetag(request,pk):
	if request.user.get_username()=='assistant':
		try:
			cases = Caselist.objects.filter(groupname__contains = pk)
			print(cases)
			return render(request, 'helper/allcases.html', {'allcases': cases})
		except Caselist.DoesNotExist:
			raise Http404
	else:
		return HttpResponse("You are not authorized to view this information")

def updatecase(request,pk):
	if request.user.get_username()=='assistant':
		if request.method == "POST":
			form = DiagnosisForm(request.POST)
			if form.is_valid():
				userObj = form.cleaned_data
				Caselist.objects.filter(caseid = int(pk)).update(diagnosis = userObj['diagnosis'])
				return HttpResponseRedirect('/homeassist')
		else:
			form = DiagnosisForm()
		case = Caselist.objects.get(caseid = int(pk))
		return render(request, 'helper/diagnosis.html', {'form': form, 'case': case})
	else:
		return HttpResponse("You are not authorized to view this information")


			