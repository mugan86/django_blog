# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from django.utils import timezone
from django.db.models import Count
from .models import Post, Event, Friend
from .forms import PostForm, EventForm, ContactForm
from collections import Counter
from django.db.models import Q
#Generate PDF files
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from django.http import HttpResponse
from io import BytesIO

def create_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pdf_doc.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Anartz Mugika Blog.")

    # define a large font
    p.setFont("Helvetica", 14)

    p.setStrokeColorRGB(0.2,0.5,0.3)
    p.setFillColorRGB(1,0,1)
    # draw some lines
    p.line(0,0,0,1.7*inch)
    p.line(0,0,1*inch,0)
    # draw a rectangle
    p.rect(0.2*inch,0.2*inch,1*inch,1.5*inch, fill=1)
    # make text go straight up
    p.rotate(90)
    # change color
    p.setFillColorRGB(0,0,0.77)
    # say hello (note after rotate the y coord needs to be negative!)
    p.drawString(0.3*inch, -inch, "Hello World")

    #Create one page
    #p.showPage()

    #horizontally from left side , vertically from down side
    p.drawString(300, 600, "Anartz Mugika Blog.")

    # Close the PDF object cleanly.
    #Create one page
    p.showPage()

    #If want create new page add new "p.showPage()"
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def principal(request):

    main_object = [];
    main = Post.objects.raw('SELECT * FROM blog_post WHERE post_type_id="Inicio" AND active = 1 ORDER BY published_date DESC')
    for p in main:
        main_object.append(p)

    main_object[0].text = get_youtube_player_in_article(main_object[0].text)

    return render(request, 'blog/principal.html', {'post_categorys': get_post_categories(), 'main_post': main_object[0], 'events': get_next_events(), 'friends': get_friends_links()})

def post_list(request):
    # Add "-" inside 'order by' element to change publish order
    posts = Post.objects.filter(published_date__lte=timezone.now()).exclude(post_type_id='Inicio').filter(active=1).order_by('-published_date')

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

    # import pdb
    # pdb.set_trace()
    return render(request, 'blog/post_list.html', {'posts': posts, 'post_categorys': get_post_categories(), 'events': get_next_events()})

    #Class to test filt by category...
def post_list_by_category(request, category):
    # Add "-" inside 'order by' element to change publish order
    posts = Post.objects.filter(published_date__lte=timezone.now()).filter(Q(category1_id=category) | Q(category2_id=category)).exclude(post_type_id='Inicio').order_by('-published_date').filter(active=1)

    """print (category)
    print (posts.count())
    print (posts)"""

    ###print p.count()

    # import pdb
    # pdb.set_trace()
    return render(request, 'blog/post_list.html', {'posts': posts, 'post_categorys': get_post_categories(), 'events': get_next_events()})
    #, {'posts': posts, 'post_categorys': get_post_categories()}

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'post_categorys': get_post_categories(), 'events': get_next_events()})

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
    return render(request, 'blog/post_edit.html', {'form': form, 'title': title, 'post_categorys': get_post_categories(), 'events': get_next_events()})

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
        return render(request, 'blog/post_edit.html', {'form': form, 'title': title, 'post_categorys': get_post_categories(), 'events': get_next_events()})

#url(r'^event/(?P<pk>[0-9]+)/edit/$', views.event_edit, name='event_edit'), in urls.py file
def event_edit(request, pk):
        title = "Edit select post"
        event = get_object_or_404(Event, pk=pk)
        if request.method == "POST":
            form = EventForm(request.POST, instance=event)
            if form.is_valid():
                event = form.save(commit=False)
                event.save()
                return redirect('blog.views.principal')
        else:
            form = EventForm(instance=event)
        return render(request, 'blog/post_edit.html', {'form': form, 'title': title, 'post_categorys': get_post_categories(), 'events': get_next_events()})

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

    return render(request, 'blog/post_edit.html', {'form': form, 'title': title, 'post_categorys': get_post_categories(), 'events': get_next_events()})

def projects(request):
    return render(request, 'blog/projects.html', {'post_categorys': get_post_categories(), 'events': get_next_events()})

def about(request):
    return render(request, 'blog/about.html', {'post_categorys': get_post_categories(), 'events': get_next_events()})

def login_form(request):
    return render(request, 'blog/login.html', {'post_categorys': get_post_categories(), 'events': get_next_events()})

def logout_account(request):
    logout(request)
    return redirect('blog.views.principal')

"""def contact(request):
    return render(request, 'blog/contact.html')"""
##Get Post category appears count to show in right column space
def get_post_categories():
    post_categorys = []

    #create method to short code...

    category_1 = Post.objects.raw('SELECT id, category1_id FROM blog_post WHERE active=1 AND post_type_id <> "Inicio"')
    category_2 = Post.objects.raw('SELECT id, category2_id FROM blog_post WHERE active=1 AND post_type_id <> "Inicio"')

    for p in category_1:
        post_categorys.append("%s" % (p.category1_id))

    for p in category_2:
        post_categorys.append("%s" % (p.category2_id))

    #Extract list values and appears count
    c = Counter(post_categorys)

    appears = c.values();
    values = c.keys();

    post_categorys = []

    #Store data string in post_categorys[] list
    for x in c.keys():
        #print ("%s (%s)" % (x, c[x]))
        category_object = [x,"%s (%s)" % (x, c[x])]
        #post_categorys.append("%s (%s)" % (x, c[x]))
        post_categorys.append(category_object)

    return post_categorys

###Get Youtube Player code from send text
def get_youtube_player_in_article(article_text):
    article_text = article_text.replace("[YOUTUBE=", "<div class=\"video-container\"><iframe width=\"100%\" src=\"https://www.youtube.com/embed/")

    article_text = article_text.replace("][/YOUTUBE]", "\" frameborder=\"0\" allowfullscreen></iframe></div>")
    #print main_object[0].text

    return article_text

def get_next_events():
    ##Show next 3 events
    return Event.objects.filter(celebrate_data__gte=timezone.now()).order_by('celebrate_data')[:3]


def get_friends_links():
    return Friend.objects.filter(type='Runners').filter(active=True).order_by('name')

