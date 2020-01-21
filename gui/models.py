from django.db import models
from PIL import Image, GifImagePlugin
import json
from slugify import slugify
import logging

logger = logging.getLogger(__name__)

# TODO img2json
# Create your models here.


PixTemp = """{
    "text": {
        "textString": "PixOn",
        "scrollText": "auto", 
        "scrollTextDelay": 20,
        "position": {
            "x": 8,
            "y": 1
        }
    }
}"""


class Sound(models.Model):
    name = models.CharField(max_length=12, blank=False)
    mp3 = models.FileField(blank=False, upload_to='MP3')

    def __str__(self):
        return "<id> " + str(self.pk) + " " + str(
            slugify(getattr(self, "name"), entities=True, max_length=10, word_boundary=False, separator='-',
                    lowercase=True))

"""
# TODO rename on save
    new_name = 'photos_preview/' + str(uuid.uuid1())
    os.rename(photo.image_preview.path, settings.MEDIA_ROOT + new_name)
    photo.image_preview.name = new_name
    photo.save()
"""



class Template(models.Model):
    name = models.CharField(max_length=12, blank=False)
    template = models.TextField(default=PixTemp, blank=False, max_length=3072)
    note = models.TextField(blank=False, max_length=512)

    def __str__(self):
        return "<name> " + self.name + " <templatesize> " + str(len(self.template)) + " <note> " + self.note


class Screen(models.Model):
    name = models.CharField(max_length=20)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    message = models.CharField(max_length=30)
    start_dt = models.DateTimeField("DT to start display this screen")
    end_dt = models.DateTimeField("DT to end display of this screen")

    def __str__(self):
        return "<name> " + self.name + " <message> " + self.message


class Bitmap(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="img")
    json = models.CharField(max_length=2048, blank=True)
    width = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)

    def __str__(self):
        return "<name> " + self.name

    def save(self, *args, **kwargs):
        img = Image.open(self.image)
        img.thumbnail((32, 8), Image.ANTIALIAS)
        self.json = self.to565(img)
        super().save(*args, **kwargs)

    def to565(self, img):

        w, h = img.size
        self.width = w
        self.height = h
        try:
            frames = img.n_frames
        except:
            frames = 0

        if frames > 0:
            ret = "["
        else:
            ret = ""
        for frame in range(0, 9):
            try:
                img.seek(frame)
                rgb_img = img.convert('RGB')
                ret += "["
                for y in range(h):
                    for x in range(w):
                        r, g, b = rgb_img.getpixel((x, y))
                        rgb = ((r & 0b11111000) << 8) | ((g & 0b11111100) << 3) | (b >> 3)
                        ret += str(rgb) + ","
                ret = ret[:-1] + "],"
            except:
                pass
        if frames > 0:
            ret = ret[:-1] + "]"
        else:
            ret = ret[:-1]
        return ret
