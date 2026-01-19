# Generated manually to add completed field

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]



