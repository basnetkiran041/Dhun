from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=255)
    audio = models.FileField(upload_to='songs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title