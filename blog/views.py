from django.shortcuts import render
from .models import Post 

# Create your views here.

def frontpage(request):
    posts = Post.objects.all()
    return render(request,'blog/frontpage.html',{'posts':posts})

def post_detail(request):
    post = Post.objects.get(slug=post.slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            commet.save()
            
            return redirect('post_detail', slug=post.slug)
        
    else:
        form = CommentForm()
        
    return render(request, 'blog/post_detail.html',{
        'post':post , 'form':form 
    })
        