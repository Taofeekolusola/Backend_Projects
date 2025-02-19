from django.db import migrations

def fix_item_codes(apps, schema_editor):
    Item = apps.get_model('dispatch', 'Item')
    for item in Item.objects.filter(code__isnull=True):
        item.code = f"ITEM_{item.id}"  # Assign a unique value
        item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0004_auto_20241223_1322'),  # Last migration file in your app
    ]

    operations = [
        migrations.RunPython(fix_item_codes),
    ]
