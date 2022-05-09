from django.db import migrations


class Migration (migrations.Migration):
    dependencies = [
        ('healthapp', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(
            code=migrations.RunPython.noop,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
