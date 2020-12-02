from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import NewMP3
from .forms import MP3Form
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# from GoogleApiClient.discovery import build
from pytube import YouTube as Y
import os
import requests
import json

# Create your views here.
video_url = ''
class HomeView(LoginRequiredMixin, ListView):
    model = NewMP3

    def get_query(self):
        queryset = NewMP3.objects.all().filter(user=self.request.user)
        return queryset


    template_name = "download_app/home.html"


def download(request):
    global video_url

    search_url = "https://www.googleapis.com/youtube/v3/search"
    video_url = "https://www.googleapis.com/youtube/v3/videos"

    if request.method == 'POST':
        api_key = 'AIzaSyBOVZDzLUhH4499e_qyb2hbqG2KGNcjHlI'
        
        search_params = {
            'part':'snippet',
            'q':request.POST['name'],
            'key':settings.YOUTUBE_dATA_API_KEY,
            'type':'video',
            'maxResults':40,
        }
        video_ids = []
        response = requests.get(search_url, params=search_params)
        
        results = response.json()['items']
        
        for result in results:
            video_ids.append(result['id']['videoId'])

        videos = []
        for result in results:
            video_data = {
                'title':result['snippet']['title'],
                'url':F"https://www.youtube.com/watch?v={result['id']['videoId']}",
                'thumbnail':result['snippet']['thumbnails']['medium']['url'],
                'source':F"/static/download_app/songs/{result['snippet']['title']}___{result['id']['videoId']}.mp3"
            }
            videos.append(video_data)

        content = {'videos':videos}
        return render(request,'download_app/vodeo_view.html', content)
    else:
        return render(request, 'download_app/home.html')






    #     d={}
    #     for item in response['items']:
    #         thumbnail = response['items']['thumbnails']['default']
    #         title = response['items']['title']
    #         d.uppand({title:thumbnail})
    #     return render(request,'download_app/download_mp3.html',{"d":d})
        
    # else:
    #     return render(request,'download_app/home.html')

def downloading(request):
    global video_url
    if request.method == 'POST':
        
        yt = Y(request.POST['video_url'])
        # video_info = YoutubeDL().extract_info(url=video_url)

        # filename = f"{video_info['title']}.mp3"

        # options = {
        #     'format': 'bestaudio/best',
        #     'keepvideo': False,
        #     'outtmpl': filename,
        #     'postprocessors': [{
        #         'key':'FFmpegExtractAudio',
        #         'preferredcodec': 'mp3',
        #         'preferredquality': '192'
        #         }]
        #     }

        # homedir = os.path.expanduser('~') + '/Downloads'

        # with youtube_dl.YoutubeDL(options) as ydl:
        #     ydl.download(homedir, [video_url])
        yt.streams.filter().first().download(os.path.expanduser('~') + '/Downloads')

        return HttpResponseRedirect(reverse('url',args=('downloading_complete')))
    #     render(request,'download_app/complate.html', {"msg":"downloading completed"})
    # 