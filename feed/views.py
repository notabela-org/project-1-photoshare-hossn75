from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from users.models import *
from .forms import EditProfileForm
from .forms import NewPostForm 

# Create your views here.
@login_required
def index(request):
    feed = [] 
    posts = Post.objects.all()
    for post in posts:
        feedItem = {}
        feedItem['post'] = post
        try:
            feedItem['profile'] = Profile.objects.get(user=post.user)
            feedItem['comments'] = Comment.objects.get(post=post)
        except ObjectDoesNotExist:
            print("Failed to fetch profile or comments")
        feed.append(feedItem)

    paginator = Paginator(feed,10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'feed/index.html',{'page_obj':page_obj})

    # return render(request, 'feed/index.html')

@login_required
def profile(request,username):
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
    except ObjectDoesNotExist:
        profile = None
    return render(request, 'feed/profile.html', {'profile':profile,'username':user.get_username()})

@login_required
def editprofile(request):
    print("Edit profile request")
    form = None
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST,files=request.FILES)
        print(form.errors)
        if form.is_valid():
            cleanForm = form.cleaned_data
            user = User.objects.get(username=request.user.get_username())
            user.username = cleanForm['username']
            user.save()
            profile = Profile(user=user,bio=cleanForm['bio'],image=cleanForm['image'])
            profile.save()
            return HttpResponseRedirect(reverse('index'))
        # print(form)
        return render(request, 'feed/editprofile.html',{'form':form})

    try:
        user = User.objects.get(username=request.user.get_username())
        profile = Profile.objects.get(user=user)
        form = EditProfileForm(data={'username':user.get_username(),'bio':profile.get_bio(),'image':profile.get_image()})
    except ObjectDoesNotExist:
        form = EditProfileForm(data={'username':request.user.get_username()})
    return render(request, 'feed/editprofile.html',{'form':form})


@login_required
def new_post(request):
    form = NewPostForm(data={})
    if request.method == 'POST':
        form = NewPostForm(data=request.POST,files= request.FILES)
        if form.is_valid():
            cleanForm = form.cleaned_data
            post = Post(user=request.user,image=cleanForm['image'],caption=cleanForm['caption'])
            post.save()

            return HttpResponseRedirect(reverse('index'))
        return render(request,'feed/new-post.html',{'form':form})
    return render(request, 'feed/new-post.html',{'form':form})


@login_required
def post(request,id):
    return render(request,'feed/post.html',{'id':id})
