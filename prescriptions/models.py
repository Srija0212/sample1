from django.db import models

# Create your models here.


from django.db import models

class Prescription(models.Model):
    image = models.ImageField(upload_to="prescriptions/")
    extracted_text = models.TextField(blank=True, null=True)
    medications = models.JSONField(default=list)  # Store extracted medications
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription {self.id}"

from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    last_visit = models.DateField()

    def __str__(self):
        return self.name
