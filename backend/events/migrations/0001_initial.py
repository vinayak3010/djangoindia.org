# Generated by Django 4.2.13 on 2024-06-25 14:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                (
                    "cover_image",
                    models.ImageField(blank=True, upload_to="event_images/"),
                ),
                ("description", models.TextField()),
                ("venue", models.TextField(default="TBA")),
                ("city", models.CharField(default="TBA", max_length=255)),
                ("venue_map_link", models.URLField(blank=True)),
                ("date_time", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="EventRegistration",
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
                ("email", models.EmailField(max_length=254)),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                (
                    "occupation",
                    models.CharField(
                        choices=[
                            ("working_professional", "Working Professional"),
                            ("student", "Student"),
                            ("freelancer", "Freelancer"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("linkedin", models.URLField()),
                ("github", models.URLField(blank=True)),
                ("twitter", models.URLField(blank=True)),
                ("other_links", models.URLField(blank=True)),
                ("rsvp", models.BooleanField(default=False)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="registrations",
                        to="events.event",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="eventregistration",
            constraint=models.UniqueConstraint(
                fields=("email", "event"), name="unique_event_registration"
            ),
        ),
    ]
