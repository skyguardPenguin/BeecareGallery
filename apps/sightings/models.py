from uuid import uuid4
from django.db import models
import datetime

from pathlib import Path

def get_img_sighting(instance,filename):
    today = datetime.datetime.now()
    extension = Path(filename).suffix
    today = datetime.datetime.now()
    year = today.strftime("%Y/")
    month = today.strftime("%m/")
    day = today.strftime("%d/")
    time = today.strftime("%H%M%S")
    uuid = uuid4().hex
    route = '%s/%s/%s' % (year,month, day)
    return 'Sightings/%s/%s_%s%s' % (route,uuid,time,extension)
class beephoto(models.Model):
    loadDate = models.DateTimeField(auto_now_add=True)
    loadImage = models.ImageField(upload_to=get_img_sighting,blank=True)


    
