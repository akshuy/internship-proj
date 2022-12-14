from django.shortcuts import render, HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from blog.models import Post
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request,'home/home.html')


def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name,email,phone,content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request,"Plese fill the form correctly ")
        else:
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"Your message has been send ")
        
    return render(request,'home/contact.html')

def search(request):
    query=request.GET['query']
    if len(query)>70:
        allPosts = Post.objects.none()
    else:    
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()== 0:
         messages.warning(request,"No search results found . Please check your query ")    
    param = {'allPosts': allPosts,'query':query}
    return render(request,'home/search.html',param)

def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # checks for errorness inputs
        # user name shoul be under 10 charactor
        if len(username) > 10:
            messages.error(request,"username can not be under 10 charactor")
            return redirect("home")

        # username should be alfanumeric
        if not username.isalnum():
            messages.error(request,"username should only contain only letters and numbers")
            return redirect("home")
        # passwords should match 
        if pass1 !=pass2:    
            messages.error(request,"passwords do not match")
            return redirect("home")            
        # Create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"your account has been successfully created")
        return redirect('home')
    else:
        return HttpResponse('404 Not Found')       

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user= authenticate(username = loginusername,password = loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"successfully login")
            return redirect('home')

        else:
            messages.error(request, "invalid user id or password plese try again")
            return redirect('home')

    return HttpResponse('404 Not Found')       


def handleLogout(request):
    logout(request)
    messages.success(request,"successfully logout")
    return redirect('home')

