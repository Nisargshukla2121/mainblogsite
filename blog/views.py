from django.shortcuts import render, HttpResponse
from blog.models import Post
from django.utils import timezone
from django.conf import settings 
from django.core.mail import send_mail 
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.conf import settings 
from django.core.mail import send_mail 


def blogHome(request):
    allPosts = Post.objects.all().order_by('-date_posted')
    allPosts = allPosts.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(allPosts, 3)
    try:
        allPosts = paginator.page(page)
    except PageNotAnInteger:
        allPosts = paginator.page(1)
    except EmptyPage:
        allPosts = paginator.page(paginator.num_pages)
    

    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)
    #return render(request, 'blog/blogHome.html', { 'allPosts': allPosts })
@login_required
def blogMy(request):
    alluserPosts = Post.objects.filter(author = request.user).order_by('-date_posted')
    context2 = {'alluserPosts': alluserPosts}
    return render(request, 'blog/blogMy.html', context2)

@login_required
def blogWrite(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        author = request.user.email
        post = Post(title=title,content=content,slug=title,author=author)
        
        post.save()  

        subject = 'your post added successfyly'
        message = f'Hi {post.author}, Thank you for posting blogs in Blogsite and hoping for some new blog from .you'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [author, ]
        send_mail( subject, message, email_from, recipient_list ) 
    return render(request, 'blog/blogWrite.html')

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'blog/blogPost.html', context)


