# Generated by Django 4.1.1 on 2022-10-28 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=25)),
                ("last_name", models.CharField(max_length=25)),
                ("email", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=20)),
                ("mobile", models.CharField(max_length=20)),
                ("company_name", models.CharField(max_length=250)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                (
                    "customer_type",
                    models.CharField(
                        choices=[
                            ("POTENTIAL", "Potential customer"),
                            ("EXISTING", "Existing customer"),
                        ],
                        default="POTENTIAL",
                        max_length=16,
                    ),
                ),
            ],
        ),
    ]
