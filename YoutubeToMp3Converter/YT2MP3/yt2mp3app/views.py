from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import pytube, os

def index(request):
    return render(request, 'yt2mp3app/index.html')

def GetInfo(request):
    video_url = request.POST['URLdata']
    video = pytube.YouTube(video_url)

    audioFile = video.streams.get_audio_only()
    audioFileName = "\'" + audioFile.default_filename + "\'"
    audioFileDownload = audioFile.download('./media')
    download_path = "./media/" + audioFile.default_filename

    os.rename(download_path,download_path.replace('mp4','mp3'))


    context = {'vid_title' : video.title , 'vid_length' : video.length, 'vid_id' : video.video_id,
               'vid_ageRest' : video.age_restricted, 'vid_thumbnail' : video.thumbnail_url,
               'path_download' : download_path.replace('mp4','mp3') }
    
    return JsonResponse(context)