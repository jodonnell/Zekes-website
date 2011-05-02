# Create your views here.
from django.shortcuts import render_to_response
from django.core.paginator import Paginator

from zeke.zeke_site.models import Videos, News

def index(request):
    news = News.objects.all().order_by('-created_on')
    return render_to_response('index.html', {'all_news':news})


def get_paginated_videos(videos, GET):
    paginator = Paginator(videos, 3)

    try:
        page = int(GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        paged_videos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        paged_videos = paginator.page(paginator.num_pages)

    return paged_videos

def work(request):
    videos = Videos.objects.filter(type='W').order_by('-created_on')
    paged_videos = get_paginated_videos(videos, request.GET)
    return render_to_response('videos.html', {'videos':paged_videos})

def play(request):
    videos = Videos.objects.filter(type='P').order_by('-created_on')
    paged_videos = get_paginated_videos(videos, request.GET)
    return render_to_response('videos.html', {'videos':paged_videos})

def contact(request):
    return render_to_response('contact.html')
