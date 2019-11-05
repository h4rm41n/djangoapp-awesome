from django import forms
from .models import Siswa

class SiswaForm(forms.ModelForm):

    class Meta:
        model = Siswa
        fields = ('nomor_induk', 'nama', 'kelamin', 'alamat', 'program')

    def __init__(self, *args, **kwargs):
        super(SiswaForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            # field.required = False
    # def clean_nomor_induk(self):
    #     nomor_induk = self.cleaned_data['nomor_induk']
            
    #     if Siswa.objects.filter(nomor_induk=nomor_induk).exists():
    #         raise forms.ValidationError("Data sudah terdaftar")
        
    #     return nomor_induk