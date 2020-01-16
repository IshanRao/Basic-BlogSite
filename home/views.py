from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import ContactForm

# Create your views here.
# redirect 

def signup(req) :
    
    if req.method == 'POST' :
        new_user = User.objects.create_user(
        first_name = req.POST.get('fname'),
        last_name = req.POST.get('lname'),
        username = req.POST.get('username'),
        email = req.POST.get('email'),
        password = req.POST.get('password')
        )
        
        return redirect("home:login")
    else :     
        return render(req,'home/signup.html')

def login_user(req) :

    if req.method == "POST" :
        user = authenticate(
             username = req.POST.get('username'),
             password = req.POST.get('password'),
         )
        # print(req.POST.get('username'))

        if user :
            login(req,user)
            return redirect('home:posts')
        else :
            return HttpResponse('Invalid username or password...Conatct Administrator')
    else :
        return render(req,'home/login.html')


@login_required
def add_posts(req) :

    if req.method == 'POST' :
        new_post = Post(
        title = req.POST.get('title'),
        content = req.POST.get('content'),
        posted_by = req.user) # Post constructor with parameters
        new_post.save() # .save() adds object to the database 

        return HttpResponse('Post added successfully')
    else :
        return render(req,'home/posts.html')      

  

@login_required
def logout_user(req) :

    logout(req)
    return redirect('home:login')        

# Primary key helps in indexing which increases the speed of retreival
# pk variable identifies the primary key ..when we don't set it it takes default as id as primary key
def index(req) :

    posts = Post.objects.all()
    return render(req,'home/index.html',{'posts' : posts})
           
def filter_by_user(req) :

    # username=req.GET['name'] is for the query string that we send 
    user = User.objects.get(username=req.GET['name'])
    posts = Post.objects.filter(posted_by=user)
    return render(req,'home/index.html',{'posts' : posts})

def filter_by_month(req) :

    month = req.GET['month']
    year = req.GET['year']
    posts = Post.objects.filter(timestamp__month=month,timestamp__year=year)
    # timestamp__month and timestamp__year gives the month and year of the post from the database
    return render(req,'home/index.html',{'posts' : posts})
    

def filter_by_year(req) :

    year = req.GET['year']
    posts = Post.objects.filter(timestamp__year=year)
    # The variable posts and the key name in the dictionary in the return statement must be the same 
    return render(req,'home/index.html',{'posts' : posts})

def filter_by_id(req,post_id) :

    posts = Post.objects.filter(id=post_id)
    return render(req,'home/index.html',{'posts' : posts})    

def contact_us(req) :

    if req.method == "POST" :
        form = ContactForm(req.POST)
        if form.is_valid() :
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
        return HttpResponse(name)    
    else :
        form = ContactForm()
        return render(req,'home/contact_us.html',{'form' : form})    



