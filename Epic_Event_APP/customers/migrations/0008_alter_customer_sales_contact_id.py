# Generated by Django 4.1.1 on 2022-10-14 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("customers", "0007_customer_customer_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="sales_contact_id",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]