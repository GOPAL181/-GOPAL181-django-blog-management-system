from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import Post
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.info(request, "Please fill the Form Correctly")
        else:
            # making contact obj of Contact model to save all of the data.
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your Issue is submitted Our Team will contact you Soon")
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    query = request.GET['query']
    if len(query) > 70:
        SrchPosts = Post.objects.none()
    else:
        SrchPostsTitle = Post.objects.filter(title__icontains=query)
        SrchPostsContent = Post.objects.filter(content__icontains=query)
        print("SrchPostsTitle = ",SrchPostsTitle , " SrchPostsContent = ",SrchPostsContent)
        SrchPosts = SrchPostsTitle.union(SrchPostsContent)

    if SrchPosts.count() == 0:
        messages.warning(request, "No search result found please refine our query.")
    params = {'SrchPosts': SrchPosts, 'query': query}
    return render(request, 'home/search.html', params)

def HandleSignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        # Check for errors
        if len(username) > 12:
            messages.warning(request, "Username must be under 12 characters !!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.warning(request, "Username should only contain letters and numbers !!!")
            return redirect('home')

        if pass1 != pass2:
            messages.warning(request, "Passwords do not match")
            return redirect('home')
        # Create the user
        my_user = User.objects.create_user(username, email, pass1)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.save()
        messages.success(request, "Your 'LaughTale' Account has been Successfully Created")
        return redirect('home')
    else:
        return HttpResponse("404 - Not Found")
    
def HandleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.warning(request, "Invalid Credentials, Please try again...")
            return redirect('home')

def HandleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')
