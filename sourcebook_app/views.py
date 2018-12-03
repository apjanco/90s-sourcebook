from django.shortcuts import render
from sourcebook_app.forms import rsvpForm, SearchForm, TextSummarizationForm
from sourcebook_app.models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape, format_html, mark_safe
from django.urls import reverse
from django.http import JsonResponse
import json
import tempfile
from sourcebook_app.text_summarization import handle_uploaded_file, handle_url
from django.utils.datastructures import MultiValueDictKeyError




# Create your views here.

def index(request):
    if request.method == 'POST':
        form = rsvpForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name', None)
            email = request.POST.get('email', None)
            note = request.POST.get('note', None)
            rsvp1 = rsvp.objects.update_or_create(
                            name = name,
                            email = email,
                            note = note,
                            )
            message = 'Thank you, see you in Boston'
            return render(request, 'index_sidebar.html', { 'message':message })

    else:
        form = rsvpForm()
        kos = KO.objects.all()
        return render(request, 'index_sidebar.html', { 'form':form, 'kos':kos })

def secret(request):
    return render(request, 'secret.html')

def bestsellers(request):
	bestsellers = BestsellerList.objects.all()
	return render(request, 'bestsellers.html', {'bestsellers': bestsellers })

def wind(request):
    return render(request, 'wind.html')


def people(request):
	people = rsvp.objects.all()
	return render(request, 'people.html', {'people': people })


def items(request):
    items = item.objects.all()
    return render(request, 'items.html', { 'items':items })


def item_view(request, title):
    the_item = item.objects.get(title=title)
    return render(request, 'item.html', { 'item':the_item })


def kos(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = request.POST.get('search', None)
            kos = KO.objects.filter(text__icontains=query)
            return render(request, 'kos.html', {'kos': kos, 'form': form, })

    else:
        form = SearchForm()
        kos = KO.objects.all()
        return render(request, 'kos.html',  {'kos': kos, 'form': form, })


def kos2(request, year, issue, date):
    kos = KO.objects.filter(year=year,issue=issue,date=date)
    return render(request, 'kos1.html', { 'kos':kos })


def kos1(request, year, issue):
    kos = KO.objects.filter(year=year, issue=issue)
    return render(request, 'kos1.html', { 'kos':kos })


def kos0(request, year):
    kos = KO.objects.filter(year=year)
    return render(request, 'kos1.html', { 'kos':kos })


def ko_text(request, year):
    text = ''.join([str(ko.text) for ko in KO.objects.filter(year=year)])
    return HttpResponse(text, content_type="text/plain")


def ko(request, filename):
    ko = KO.objects.get(filename=filename)
    similar = KO.objects.filter(year=ko.year).order_by('filename')
    item_list = []
    # make a list of the possible items with index values
    for index, item in enumerate(similar):
        if item not in item_list:
            item_list.append(item)
    for item in item_list:
        if item.filename == ko.filename:
            current = item
            print('current is', current)
    # find index in list for current
    index_current = item_list.index(current)
    previous_ko = item_list[index_current - 1]
    try:
        next_ko = item_list[index_current + 1]
    except:
        next_ko = item_list[0]
    return render(request, 'ko.html', {'ko': ko, 'next': next_ko, 'previous': previous_ko, })


def media(request, file):
    file = open('/srv/sourcebook/sourcebook_app/media/{}' % file)
    response = HttpResponse(content=file)
    return response


def text_summarization(request):
    if request.method == 'POST':
        form = TextSummarizationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                text = handle_uploaded_file(request.FILES['file'])
            except MultiValueDictKeyError:
                text = 'Error'

            url = handle_url(request.POST.get('url', None))

            return render(request, 'text_summarization.html', {'form': form, 'url': url, 'text': text})

    else:
        form = TextSummarizationForm()
        return render(request, 'text_summarization.html', {'form': form})


def network_json(request):

    """{
      "nodes":[
            {"name":"node1","group":1},
            {"name":"node2","group":2},
            {"name":"node3","group":2},
            {"name":"node4","group":3}
        ],
        "links":[
            {"source":2,"target":1,"weight":1},
            {"source":0,"target":2,"weight":3}
        ]
    }"""
    bestsellers = BestsellerList.objects.all()
    graph = {"nodes": [], "links": []}

    # create nodes for authors, titles, publishers,
    authors = set([bestseller.author for bestseller in bestsellers])
    for author in authors:
        graph['nodes'].append({"name":author,"group":1},)

    publishers = set([bestseller.publisher for bestseller in bestsellers])
    for publisher in publishers:
        graph['nodes'].append({"name":publisher,"group":1},)
    titles = set([bestseller.title for bestseller in bestsellers])
    for title in titles:
        graph['nodes'].append({"name":title,"group":1},)

    counter = 0
    for bestseller in bestsellers:

        if bestseller.author == '':
            author = 'na{}'.format(counter)
            graph['nodes'].append({"name": author, "group": 1}, )
            author = graph['nodes'].index({"name": 'na{}'.format(counter), "group": 1}, )
            counter += 1
        else:
            author = graph['nodes'].index({"name":bestseller.author,"group":1},)
        title = graph['nodes'].index({"name":bestseller.title,"group":1},)
        publisher = graph['nodes'].index({"name":bestseller.publisher,"group":1},)

        # author-title edge
        graph['links'].append({"source": author, "target": title, "weight": 1},)
        # author-publisher edge
        graph['links'].append({"source": author, "target": publisher, "weight": 1},)
        # publisher-title edge
        graph['links'].append({"source": publisher, "target": title, "weight": 1},)

    response = JsonResponse(graph)
    return response



class KOListJson(BaseDatatableView):
    model = KO
    columns = ['year', 'issue', 'date', 'filename','text',]


    # define column names that will be used in sorting order is important and should be same as order of columns displayed by datatables.
    # For non sortable columns use empty value like ''
    order_columns = ['year', 'issue', 'date', 'filename','text', ]

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site and make it return huge amount of data
    max_display_length = 500

    def render_column(self, row, column):
        if column == 'year':
            path = reverse('kos0', args=(row.year,))
            return format_html("<a href='{0}'>{1}</a>".format(path, row.year,))
        if column == 'issue':
            path = reverse('kos1', args=(row.year, row.issue))
            return format_html("<a href='{0}'>{1}</a>".format(path, row.issue))
        if column == 'date':
            path = reverse('kos2', args=(row.year, row.issue, row.date))
            return format_html("<a href='{0}'>{1}</a>".format(path, row.date))
        if column == 'text':
            return format_html("{0}".format(mark_safe(row.text)))
        if column == 'filename':
            path = reverse('ko', args=(row.filename,))
            return format_html("<a href='{0}'>{1}</a>".format(str(path), str(row.filename)))

        #else:
        #    return super(KOListJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(text__icontains=search)
        return qs


class DistantViewingJson(BaseDatatableView):
    model = DistantViewing
    columns = ['frame', 'time', 'score', 'object',]


    # define column names that will be used in sorting order is important and should be same as order of columns displayed by datatables.
    # For non sortable columns use empty value like ''
    order_columns = ['frame', 'time', 'score', 'object',]

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site and make it return huge amount of data
    max_display_length = 500

    def render_column(self, row, column):
        if column == 'frame':
            return format_html("<p>{}</p>".format(row.frame,))
        if column == 'time':
            return format_html("<a onclick='set_time({})'>{}</a>".format(row.time, row.time,))
        if column == 'score':
            return format_html("<p>{}</p>".format(row.score,))
        if column == 'object':
            return format_html("<p>{}</p>".format(row.object,))
        #else:
        #    return super(KOListJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(object__icontains=search)
        return qs

def distant_viewing(request):
    return render(request, 'distant.html', )