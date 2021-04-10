from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as auth_logout
from .models import Business, BusinessInfo, Reply
from .models import BusinessForm, ReplyForm
from django.views.generic import DetailView

# Create your views here.
def index(request):
    if request.user.is_authenticated:
            form = BusinessForm()
            return render(request,'changed/home.html',{'form':form})
    else:
            return render(request,'changed/login.html')


def about(request):
    if request.user.is_authenticated:
            return render(request,'changed/about.html')
    else:
            return render(request,'changed/login.html')


def signup(request):
    return render(request,'changed/signup.html')


def writeReview(request):
    '''
    TODO: Business = business_name, BusinessInfo = covid_compliance_rating
    '''
    user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business_name = request.POST['businessName']
            business_pid = request.POST['businessPid']
           # print(business_name)
           # print(business_pid)
            covid_compliance_rating = form.cleaned_data['covid_compliance_rating']
           # print(covid_compliance_rating)
            capacity_limit = form.cleaned_data['capacity_limit']
           # print(capacity_limit)
            indoor_dining = form.cleaned_data['indoor_dining']
           # print(indoor_dining)
            outdoor_dining = form.cleaned_data['outdoor_dining']
           # print(outdoor_dining)
            curbside_pickup = form.cleaned_data['curbside_pickup']
           # print(curbside_pickup)
            delivery = form.cleaned_data['delivery']
           # print(delivery)
            body = form.cleaned_data['body']
           # print(body)
            if(Business.objects.filter(business_name=business_name,business_pid=business_pid).exists()):
            #the business already exists, don't create a duplicate
                print('The business already exists')
                business = Business.objects.get(business_name=business_name,business_pid=business_pid)
                user = User.objects.get(username=request.user.username)
                business_info = BusinessInfo.objects.create(business=business,user=user, covid_compliance_rating=covid_compliance_rating,capacity_limit=capacity_limit,
                                                           indoor_dining=indoor_dining,outdoor_dining=outdoor_dining, curbside_pickup=curbside_pickup,delivery=delivery,body = body) 
                print(business_name)
                print(user.username)
                print(body)
                return HttpResponseRedirect(reverse('changed:index'))
            else:
                business = Business.objects.create(business_name=business_name,business_pid=business_pid)
                user = User.objects.get(username=request.user.username)
                business_info = BusinessInfo.objects.create(business=business,user=user, covid_compliance_rating=covid_compliance_rating,capacity_limit=capacity_limit,
                                                           indoor_dining=indoor_dining,outdoor_dining=outdoor_dining, curbside_pickup=curbside_pickup,delivery=delivery,body = body)
                print(business_name)
                print(user.username)
                print(review_text)
                return HttpResponseRedirect(reverse('changed:index'))
        return HttpResponseRedirect(reverse('changed:index'))
    else:
        form = BusinessForm()
    return render(request,'changed/home.html',{'form':form})

def show_reviews(request):
    #this page shows the respective business and all of its comments, shown when "Read review" is clicked
        business_name = request.POST['businessName']
        business_pid = request.POST['businessPid']
        if (Business.objects.filter(business_name=business_name,business_pid=business_pid).exists()):
            business = Business.objects.get(business_name=business_name,business_pid=business_pid)
            business_name = business.business_name
            business_info = business.businessinfo_set.all()
            print(business_name) 
            context = {
            'business_name':business_name,
            'business_info':business_info,
            "business" : business,
            }
            return render(request,'changed/comments.html',context)
        else:
            form = BusinessForm()
            return render(request,'changed/home.html',{'form':form})

def profile(request,username):
    #this page shows the respective profile and all of the user's reviews, when "profile" is clicked
        if (User.objects.filter(username=username).exists()):
            user = User.objects.get(username=username)
            username = user.username
            business_info = user.businessinfo_set.all()
            print(username) 
            context = {
            'user':user,
            'user_reviews':business_info,
            }
            return render(request,'changed/profile.html',context)
        else:
            form = BusinessForm()
            return render(request,'changed/home.html',{'form':form})   
def reply(request,id):
    #this page shows the respective profile and all of the user's reviews, when "profile" is clicked
        if (BusinessInfo.objects.filter(id=id).exists()):
            comment = BusinessInfo.objects.get(id=id)
            replies = comment.reply_set.all() 
            form = ReplyForm()
            context = {
            'comment':comment,
            'replies':replies,
            'form':form,
            }
            if request.method == 'POST':
              form = ReplyForm(request.POST)
              if form.is_valid():
                reply = form.cleaned_data['reply']
                user = request.user
                reply = Reply.objects.create(body=reply,comment=comment,user=user)
            return render(request,'changed/replies.html',context)   
        else:
          form = BusinessForm()
          return render(request,'changed/home.html',{'form':form})

       



    
    
