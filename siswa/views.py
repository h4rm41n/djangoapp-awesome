from django.shortcuts import render, redirect
from django.views import View
from .models import Siswa


# class Index(View):
#     def get(self, request):
#         template_name = "siswa/index.html"

#         data = {
#             "title_web": "Web ITEC",
#             "siswa": Siswa.objects.all() #SELECT * FROM siswa
#         }
#         return render(request, template_name, data)
    

def Index(request):
    if request.POST:
        form = request.POST
        siswa = Siswa()
        siswa.alamat = form['alamat']
        siswa.nama = form['nama']
        siswa.nomor_induk = form['nomor_induk']
        siswa.kelamin = form['kelamin']
        siswa.program = form['program']
        siswa.save()

        return redirect('/')

    else:
        template_name = "siswa/index.html"

        data = {
            "title_web": "Web ITEC",
            "siswa": Siswa.objects.all() #SELECT * FROM siswa
        }
        return render(request, template_name, data)

# class IndexPost(View):
#     def post(self, request):
#         form = request.POST
#         print(form)

        # <QueryDict: 
        # {'csrfmiddlewaretoken': ['oHBskvuCiJwcVmhXDrNpgo8RkJEkXJe4PeYRQKVxB6wLZVw7MiVU4ZuMK76M9pHR'],
        # 'nomor_induk': ['lkj'],
        # 'nama': ['ljl'],
        # 'kelamin': ['kjl'],
        # 'program': ['kj'],
        # 'alamat': ['ljl']}>
