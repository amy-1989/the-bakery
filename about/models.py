from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)
    profile_image = models.ImageField(null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class ContactForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    seen = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"
