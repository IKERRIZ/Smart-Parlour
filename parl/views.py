from django.http import Http404
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfileForm,ImageForm,CommentForm
from .models import Image,Comment,Likes,Profile


# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def all_hairstyle(request):
    current_user = request.user
    all_images = Image.objects.all()
    comments = Comment.objects.all()
    likes = Likes.objects.all
    profile = Profile.objects.all()
    
    print(likes)
    return render(request,'hairstyle.html',locals())

def add_hairstyle(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.profile = current_user
            add.save()

            return redirect('index')
    else:
        form = ImageForm()

    return render(request, 'hairstyle.html',locals())


@login_required(login_url='/accounts/login/')
def all_makeup(request):
    current_user = request.user
    all_images = Image.objects.all()
    comments = Comment.objects.all()
    likes = Likes.objects.all
    profile = Profile.objects.all()
    
    print(likes)
    return render(request,'make_up.html',locals())

def add_makeup(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.profile = current_user
            add.save()

            return redirect('index')
    else:
        form = ImageForm()

    return render(request, 'make_up.html',locals())


@login_required(login_url='/accounts/login/')
def all_acrylix(request):
    current_user = request.user
    all_images = Image.objects.all()
    comments = Comment.objects.all()
    likes = Likes.objects.all
    profile = Profile.objects.all()
    
    print(likes)
    return render(request,'acrylix.html',locals())

def add_acrylix(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.profile = current_user
            add.save()

            return redirect('acrylix')
    else:
        form = ImageForm()

    return render(request, 'acrylix.html',locals())


@login_required(login_url='/accounts/login/')
def all_therapy(request):
    current_user = request.user
    all_images = Image.objects.all()
    comments = Comment.objects.all()
    likes = Likes.objects.all
    profile = Profile.objects.all()
    
    print(likes)
    return render(request,'skin_therapy.html',locals())

def add_therapy(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.profile = current_user
            add.save()

            return redirect('skin_therapy')
    else:
        form = ImageForm()

    return render(request, 'skin_therapy.html',locals())    


@login_required(login_url='/login')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.owner = current_user
            profile.save()
    else:
        form=ProfileForm()
    return render(request,'profile/new.html', locals())

@login_required(login_url='/accounts/login/')
def display_profile(request, id):
    seekuser=User.objects.filter(id=id).first()
    profile = seekuser.profile
    profile_details = Profile.get_by_id(id)
    images = Image.get_profile_images(id)
    usersss = User.objects.get(id=id)
    follower = len(Follow.objects.followers(usersss))
    following = len(Follow.objects.following(usersss))
    people=User.objects.all()
    pip_following=Follow.objects.following(request.user)
    


    return render(request,'profile/profile.html',locals()) 

def search(request):
    profiles = User.objects.all()

    if 'username' in request.GET and request.GET['username']:
        search_term = request.GET.get('username')
        results = User.objects.filter(username__icontains=search_term)
        print(results)

        return render(request,'results.html',locals())

    return redirect(index)



def comment(request,image_id):
    current_user=request.user
    image = Image.objects.get(id=image_id)
    profile_owner = User.objects.get(username=current_user)
    comments = Comment.objects.all()
    print(comments)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.comment_owner = current_user
            comment.save()
            
            print(comments)

        return redirect(index)

    else:
        form = CommentForm()

    return render(request, 'comment.html',locals())

def like(request, image_id):
    current_user = request.user
    image=Image.objects.get(id=image_id)
    new_like,created= Likes.objects.get_or_create(liker = current_user, image=image)
    new_like.save()

    return redirect('index')

