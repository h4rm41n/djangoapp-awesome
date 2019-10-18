from django.contrib import admin
from .models import Siswa


class SiswaAdmin(admin.ModelAdmin):
    list_display = ['nomor_induk', 'nama', 'kelamin', 'program', 'alamat']

admin.site.register(Siswa, SiswaAdmin)