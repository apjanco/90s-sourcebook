from django.shortcuts import render
from sourcebook_app.forms import rsvpForm, SearchForm
from sourcebook_app.models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape, format_html, mark_safe
from django.urls import reverse

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
            return format_html("<p style='font-size: 10px; text-align: left;'>{}</p>".format(mark_safe(row.text),))
        if column == 'filename':
            path = reverse('ko', args=(row.filename,))
            return format_html("<a href='{0}'>{1}</a>".format(path, row.filename))

        #else:
        #    return super(KOListJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(text__icontains=search)
        return qs