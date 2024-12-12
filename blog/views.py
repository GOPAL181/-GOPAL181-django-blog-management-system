from django.shortcuts import render, redirect
from blog.models import Post, BlogComment
from django.contrib import messages
from blog.templatetags import extras
# Create your views here.

def blogHome(request):
    allpost = Post.objects.all()
    cntxt = {'posts': allpost}
    return render(request, 'blog/blogHome.html', cntxt)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)    
    repDict = {}
    for reply in replies:
        if reply.parent.sno not in repDict.keys():
            repDict[reply.parent.sno] = [reply]
        else:
            repDict[reply.parent.sno].append(reply)
    cntxt = {'post': post, 'comments': comments, 'user': request.user, 'replyDict': repDict}
    return render(request, 'blog/blogPost.html', cntxt)

def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your Comment has been Posted Successfully")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent )
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
    return redirect(f'/blog/{post.slug}')