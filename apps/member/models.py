from random import randint

from django.db import models

# Create your models here.


# |=| Método que asigna una fotografía al |=|
# |=| trabajador registrado.              |=|
# |=| Para el caso de esta app, el núm    |=|
# |=| maximo se debe considerar respecto  |=|
# |=| a la cantidad de opciones de foto   |=|
# |=| en la carpeta "static/memb/".     |=|
def get_default_memb_image():
    return "memb/memb_memb_image" + str(randint(0, 5)) + ".png"
class memberphoto(models.Model):
    loadDate = models.DateTimeField(auto_now_add=True)
    loadImage = models.ImageField(upload_to=get_default_memb_image,blank=True)