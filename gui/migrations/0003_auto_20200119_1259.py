# Generated by Django 3.0.2 on 2020-01-19 11:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('gui', '0002_auto_20200119_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='template',
            field=models.CharField(
                default='\n{\n    "sleepMode": false \n    "brightness": 125\n    "bitmap": {\n    },\n    "bitmapAnimation": {\n    },\n    "text": {\n        "textString": "Test It :D",\n        "bigFont": false,\n        "scrollText": "auto", \n        "scrollTextDelay": 20,\n        "position": {\n            "x": 8,\n            "y": 1\n        },\n        "color": {\n            "r": 255, \n            "g": 255, \n            "b": 255    \n        }\n    },\n    "sound": {\n        "volume": 20, // 0 - 30\n        "control": "pause",\n        "file": 0 \n    }\n}\n',
                max_length=2048),
        ),
    ]
