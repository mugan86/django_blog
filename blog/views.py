# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from django.utils import timezone
from django.db.models import Count
from .models import Post, Event, Friend, Project
from .forms import PostForm, EventForm, ContactForm
from collections import Counter
from django.db.models import Q
#Generate PDF files
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
#reportlab colors import
from reportlab.lib.colors import pink, black, red, blue, green
from reportlab.lib.pagesizes import A4
from django.http import HttpResponse
from io import BytesIO
from polls.models import Question, Choice
#serializer objects
from django.core import serializers

#pisa
from xhtml2pdf import pisa
import cStringIO as StringIO
from django.template.loader import get_template 
from django.template import Context 


#Return all post objects in json format
def get_posts(request):
    data = serializers.serialize('json', Post.objects.all(), fields=('author','title', 'description', 'text', 'source'))
    new_data = []
    for item in data:
        new_data.append(item[0])
    return HttpResponse(new_data, content_type='application/json')

def create_pdf_with_pisa(request):
    template = get_template("pisa_hello.html") 
    context = Context({'pagesize':'A4'}) 
    html = template.render(context) 
    result = StringIO.StringIO() 
    pdf = pisa.pisaDocument(StringIO.StringIO(html), dest=result) 
    if not pdf.err: 
        return HttpResponse(result.getvalue(), content_type='application/pdf') 
    else: return HttpResponse('Errors') 
    
def create_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    filename_attachment = 'attachment; filename="pdf_%s.pdf"' % (timezone.now())
    print (filename_attachment)
    response['Content-Disposition'] = filename_attachment

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."

    #Reference: https://www.reportlab.com/docs/reportlab-userguide.pdf (Page 16)

    c = canvas.Canvas(buffer, pagesize = A4)

    c.setStrokeColor(pink)
    c.grid([inch, 2*inch, 3*inch, 4*inch], [0.5*inch, inch, 1.5*inch, 2*inch, 2.5*inch])
    c.setStrokeColor(black)
    c.setFont("Times-Roman", 20)
    c.drawString(500,2.5*inch, "(0,0) the Origin")
    c.drawString(2.5*inch, inch, "(2.5,1) in inches")
    c.drawString(4*inch, 6*inch, "(4, 2.5)")
    c.setFillColor(red)
    c.rect(0,2*inch,0.2*inch,0.3*inch, fill=1)
    c.setFillColor(green)
    c.circle(4.5*inch, 0.4*inch, 0.2*inch, fill=1)

    #If want create new page add new "p.showPage()"
    c.showPage()

    c.setLineWidth(.3)
    c.setFont('Helvetica', 12)

    c.drawString(30,750,'OFFICIAL COMMUNIQUE')
    c.drawString(30,735,'OF ACME INDUSTRIES')
    c.drawString(500,750,"12/12/2010")
    c.line(480,747,580,747)

    c.drawString(275,725,'AMOUNT OWED:')
    c.drawString(500,725,"$1,000.00")
    c.line(378,723,580,723)

    c.drawString(30,703,'RECEIVED BY:')
    c.line(120,700,580,700)
    c.drawString(120,703,"Anartz Muxika Ledo")

    c.showPage()
    c.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def principal(request):

    main_object = [];
    main = Post.objects.raw('SELECT * FROM blog_post WHERE  active = 1 ORDER BY published_date DESC')
    for p in main:
        main_object.append(p)

    main_object[0].text = get_youtube_player_in_article(main_object[0].text)

    """question = Question.objects.get(id=4) 'question': question"""

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
    projects = Project.objects.filter(active=1).order_by('published_date')[:6]
    for p in projects:
        print (p)

    return render(request, 'blog/projects.html', {'projects': projects, 'post_categorys': get_post_categories(), 'events': get_next_events()})

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
        post_categorys.append("%s" % (p.title))
        
    for p in category_2:
        post_categorys.append("%s" % (p.title))

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

