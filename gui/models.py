from django.db import models

# Create your models here.

PixTemp = """{
    "text": {
        "textString": "PixOn",
        "scrollText": "auto", 
        "scrollTextDelay": 20,
        "position": {
            "x": 8,
            "y": 1
        },
        "color": {
            "r": 255, 
            "g": 255, 
            "b": 255    
        }
    }
}"""

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
