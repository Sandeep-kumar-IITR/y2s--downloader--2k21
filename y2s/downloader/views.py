import os

from django.shortcuts import render
from pytube import YouTube

# Create your views here.
#main page or landing page
def y2s_down(request):
    return render(request,'y2s main.html')


#function to get url
def y2s_download(request):
    global url
    url = request.GET.get("link")
    video = YouTube(url)
    video_stream = video.streams.filter(progressive =True).all()
    embd_link = url.replace('watch?v=','embed/')
    titles = video.title
    context = {'video': video_stream,'embed': embd_link , "titled": titles}
    return render(request , 'y2s download.html',context)


# to define os location

def yt_doanload_done(request,resolution):
    os.chdir("C://")
    list = os.listdir()
    if "y2s--downloader" not in list:
        os.makedirs("y2s--downloader")
    dirs = "C:\y2s--downloader"
    pa = dirs
    if request.method == "POST":
        YouTube(url).streams.get_by_resolution(resolution).download(dirs)
        s = " !!! Your video is downloaded .  Don't forget to share with your friend 😍 "
        symbol = {'symd': s , 'path': pa}
        return render(request,'y2s download.html',symbol)
    else :
        e = "!!! sorry to say , but there are some error in downloading your video 😢 !!!"
        symbole = {'syme': e}
        return render(request,'y2s download.html',symbole)




