import os
from django.shortcuts import render, redirect, get_object_or_404
from .forms import HoldingsForm, SearchForm
from . models import Holdings
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound, FileResponse, Http404

#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank
from django.views.decorators.clickjacking import xframe_options_sameorigin # xframe_options_exempt



# Create your views here.
# define the search view
def search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Holdings.objects.annotate(
                    search=SearchVector('title','authors')).filter(search=query)


    context = {'form':form,'query':query,'results':results}
    return render(request, 'dlapp/search.html', context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")# vnd.ms-excel
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def model_form_upload(request):
    if request.method == 'POST':
        form = HoldingsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
 #           return redirect('home')
    else:
        form = HoldingsForm()
    return render(request, 'dlapp/upload.html', {'form': form})


def home(request):
    holdings = Holdings.objects.all() 
    return render(request, 'dlapp/home.html')


def holdings_list(request):
	holdings = Holdings.objects.all()
	return render(request, 'dlapp/list.html', {'holdings':holdings})

@xframe_options_sameorigin
def pdf_view(request, pk):
	holdings = Holdings.objects.all().filter(id=pk)
	return render(request, 'dlapp/pdfembed.html', {'holdings':holdings})


#################################################################
def pdf_view3(request):
	fs = FileSystemStorage()
	filename = 'static/media/06-CIdef.pdf'
	if fs.exists(filename):
		with fs.open(filename) as pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			#response['Content-Disposition'] = 'attachment; filename=file'
			response['Content-Disposition'] = 'inline; filename=some_file'
			return response
	else:
		return HttpResponseNotFound('Something went wrong! The request could not be served.')			


def pdf_view1(request):
    with open('static/media/06-CIdef.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=some_file.pdf'
        return response
 

def pdf_viewxx(request):
    with open('static/media/06-CIdef.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response


def pdf_view_(request):
    try:
        return FileResponse(open('static/media/06-CIdef.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
