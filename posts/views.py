from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, FileResponse
from posts.models import Post, Comment, News




def home(request):
    try:
        news = News.objects.all()[0]
    except IndexError:
        return render(request, 'base.html', {'title': "Home",})


    return render(request, 'home.html', {'title': "Home", 'news': news})

def contact(request):
    return render(request, 'contact.html', {'title': "Contact"})

def about(request):
        return render(request, 'me.html', {'title': "About Me"})


def thoughts(request):
    posts = Post.objects.all()
    return render(request, 'thoughts.html', {'title': "Thoughts", 'posts': posts})

"""def resume(request):
    try:
        return FileResponse(open('static/images/resume.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()"""

def resume(request):
    return render(request, 'resume.html', {'title': "Resume"})

def blog_post(request, post_name):
    try:
        post_name = str(post_name)
    except ValueError:
        raise Http404()
    html = ""
    #find post and store it
    try:
        post = Post.objects.get(title=post_name)
    except Post.DoesNotExist:
        html = "This post you are looking for does not exist"

    comments = Comment.objects.filter(parent_post__title = post_name)
    return render(request, 'blog_post.html', {'title': "Thoughts", 'post': post, 'comments': comments,})

def comment(request):
    if request.method == 'POST':
        if 'text' in request.POST:
            comment_text = str(request.POST['text'])
            if comment_text != "":
                message = "Your comment has been successfully submitted:   %s" % comment_text
                parent = str(request.path)
                parent = Post.objects.get(title=parent.split("/")[2])
                Comment.objects.create(
                    text=comment_text,
                    likes = 0,
                    parent_post = parent
                )

            comments = Comment.objects.filter(parent_post__title = parent.title)
            return render(request, 'blog_post.html', {'title': parent.title, 'post': parent, 'comments': comments,})
