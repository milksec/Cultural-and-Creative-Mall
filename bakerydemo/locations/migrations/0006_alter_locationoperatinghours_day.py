# Generated by Django 4.2.8 on 2023-12-07 18:36

from django.db import migrations, models


def forwards_func(apps, schema_editor):
    OperatingHours = apps.get_model("locations", "locationoperatinghours")
    db_alias = schema_editor.connection.alias
    OperatingHours.objects.using(db_alias).filter(day="TUES").update(day="TUE")
    OperatingHours.objects.using(db_alias).filter(day="THUR").update(day="THU")


def reverse_func(apps, schema_editor):
    OperatingHours = apps.get_model("locations", "locationoperatinghours")
    db_alias = schema_editor.connection.alias
    OperatingHours.objects.using(db_alias).filter(day="TUE").update(day="TUES")
    OperatingHours.objects.using(db_alias).filter(day="THU").update(day="THUR")


class Migration(migrations.Migration):

    dependencies = [
        ("locations", "0005_use_json_field_for_body_streamfield"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
        migrations.AlterField(
            model_name="locationoperatinghours",
            name="day",
            field=models.CharField(
                choices=[
                    ("MON", "Monday"),
                    ("TUE", "Tuesday"),
                    ("WED", "Wednesday"),
                    ("THU", "Thursday"),
                    ("FRI", "Friday"),
                    ("SAT", "Saturday"),
                    ("SUN", "Sunday"),
                ],
                default="MON",
                max_length=3,
            ),
        ),
    ]
