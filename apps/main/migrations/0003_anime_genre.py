# Generated by Django 4.1.1 on 2022-10-14 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_cartoons_serialrole_actor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Anime",
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
                ("studio", models.CharField(max_length=25, verbose_name="студия")),
                ("rating", models.IntegerField(verbose_name="рейтинг")),
                ("description", models.CharField(max_length=25, verbose_name="студия")),
                ("link", models.CharField(max_length=25, verbose_name="ссылка")),
                ("name", models.CharField(max_length=25, verbose_name="название")),
                ("start_date", models.DateTimeField(verbose_name="дата показа")),
            ],
            options={
                "verbose_name": "Аниме",
                "verbose_name_plural": "Много аниме",
            },
        ),
        migrations.CreateModel(
            name="Genre",
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
                ("name", models.CharField(max_length=25, verbose_name="студия")),
                (
                    "anime",
                    models.ManyToManyField(
                        related_name="genre", to="main.anime", verbose_name="аниме"
                    ),
                ),
            ],
        ),
    ]