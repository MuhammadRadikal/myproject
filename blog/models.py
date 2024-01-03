from django.db import models

class Artikel(models.Model):
    judul = models.CharField(max_length=200)
    konten = models.TextField()
    tanggal_publikasi = models.DateTimeField('tanggal publikasi')

    def __str__(self):
        return self.judul
