from django.shortcuts import render
from django.views import View
from .models import Siswa


class Index(View):
    def get(self, request):
        template_name = "siswa/index.html"

        data = {
            "title_web": "Web ITEC",
            "siswa": Siswa.objects.all() #SELECT * FROM siswa
        }
        return render(request, template_name, data)