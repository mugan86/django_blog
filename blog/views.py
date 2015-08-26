# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Count
from .models import Post
from .forms import PostForm
from .forms import ContactForm
from collections import Counter

def post_list(request):
    # Add "-" inside 'order by' element to change publish order
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    p_count = Post.objects.all().count()

    post_per_page = 10

    pages = round(p_count / post_per_page, 0)

    if (p_count % post_per_page > 0):
        pages = pages + 1

    #print "Post total: %s" % (p_count)
    #print "Pages total: %s" % (pages)

    """p = Post.objects.all().annotate(Count('title',
                                         distinct=True))"""

    ###print p.count()

    ##Get Post category appears count to show in right column space
    post_categorys = []

    #create method to short code...

    category_1 = Post.objects.raw('SELECT id, category1_id FROM blog_post')
    category_2 = Post.objects.raw('SELECT id, category2_id FROM blog_post')

    for p in category_1:
        post_categorys.append("%s" % (p.category1_id))

    for p in category_2:
        post_categorys.append("%s" % (p.category2_id))

    #Extract list values and appears count
    c=Counter(post_categorys)

    appears = c.values();
    values = c.keys();
    
    post_categorys = []

    for i in range(len(appears)):
        print i, appears[i]
        post_categorys.append("%s (%s)" % (values[i] , appears[i]))
    
    # import pdb
    # pdb.set_trace()
    return render(request, 'blog/post_list.html', {'posts': posts, 'post_categorys': post_categorys})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):

    title = "Add new post"
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'title': title})

def post_edit(request, pk):
        title = "Edit select post"
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form, 'title': title})

def contact_new(request):

    title = "Contact Form"
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
            # import pdb
            # pdb.set_trace()
            return render(request, 'blog/post_list.html', {'posts': posts})
    else:
        form = ContactForm()

    return render(request, 'blog/post_edit.html', {'form': form, 'title': title})

def about(request):
    return render(request, 'blog/about.html')

"""def contact(request):
    return render(request, 'blog/contact.html')"""
