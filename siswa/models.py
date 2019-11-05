from django.db import models


class Siswa(models.Model):
    nomor_induk = models.CharField(max_length=10)
    nama = models.CharField(max_length=50)

    KELAMIN = (
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan'),
    )
    kelamin = models.CharField(max_length=1, choices=KELAMIN)

    alamat = models.TextField()

    PROGRAM = (
        ('HTML Basic', 'HTML Basic'),
        ('CSS Basic', 'CSS Basic'),
        ('Python Basic', 'Python Basic'),
    )
    program = models.CharField(max_length=30, choices=PROGRAM)

    def __str__(self):
        return self.nama
    
