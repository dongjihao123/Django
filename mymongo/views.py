from django.shortcuts import render
import os
from django.utils import timezone
from .models import photomodel
from django.shortcuts import HttpResponse
from django.conf import  settings
# Create your views here.

def uploadimage(request):
    if request.method == 'POST':
        image_name = request.POST.get('imagename')+'.jpg'
        t1 = timezone.localtime()
        t2 =t1.strftime("%Y-%m-%d %H:%M:%S")
        files = request.FILES
        content = files.get('image', None);
        size = content.size/1000
        photomodel.objects.create(name=image_name, created_at=t2, size=str(size)+'kB')
        content = content.read()
        path = os.path.join(settings.MEDIA_ROOT,image_name,)
        with open(path,'wb') as f:
            f.write(content)
        return HttpResponse('OK')
        pass

    #result = albummodel.objects.filter(name='上海')
    #print(result[0].name)
    #return HttpResponse('OK')

    #result = albummodel.objects.filter(name='北京').first().update(name='广州')
    #print(result[0].name)
    #return HttpResponse('OK')

    #result = albummodel.objects.filter(name='广州').delete()
    #print(result)
    #return HttpResponse('OK')



