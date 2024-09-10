from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator


class Enquiry(models.Model):

    class ActivityChoice(models.TextChoices):
        LN = ("LN", "Lend")
        BR = ("BR", "Borrow")

    phone_validator = RegexValidator(
        r"^\d{10}$", message="Enter a valid 10-digit phone number."
    )
    semester_validators = [MinValueValidator(1), MaxValueValidator(8)]

    full_name = models.CharField(max_length=64)
    phone_number = models.CharField(
        max_length=10,
        validators=[
            phone_validator,
        ],
    )
    activity = models.CharField(max_length=2, choices=ActivityChoice.choices)
    college = models.CharField(max_length=128)
    department = models.CharField(max_length=64)
    semester = models.PositiveSmallIntegerField(validators=semester_validators)
    subject = models.CharField(max_length=128)
    book_name = models.CharField(max_length=128)

    class Meta:
        db_table = "mysite_enquiries"
