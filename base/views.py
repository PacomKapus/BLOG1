from django.shortcuts import get_object_or_404,render,redirect
from .forms import SignUpForm,PostForm
from .models import Post
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import  check_password
from django.contrib import messages
from django.contrib.auth.models import User


def signup(request):
    form = SignUpForm() 
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            
            login(request, user)
            
            return redirect('/blog')  
        
    return render(request, 'sign-up.html', {'form': form})

def loginPage(request):
    error = ""
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
            
            if check_password(password, user.password):
                login(request, user)
            return redirect('base:index')
         
        except:
            messages.error(request, 'Email or Password is incorrect')
    
    return render(request, 'log-in.html', {'error': error})
    
def blog(request):
    search_query = request.GET.get('search','')
    
    if search_query:
        posts = Post.objects.filter(description__icontains=search_query)
    else:
        posts = Post.objects.all()   
    
    return render(request, 'blog.html', {'posts': posts})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('blog')

def create(request):
    form=PostForm()
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    return render(request,'create.html',{'form':form})    


def trending(request):
    return render(request, 'trending.html')

def readmore(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'read-more.html', {'post': post})

def profile(request):
    return render(request, 'profile.html')

def updatepost(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog')
    return render(request, 'updatepost.html', {'form': form,'post': post})
 
