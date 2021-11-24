from django.forms import ModelForm
from home import models

class StudentForm(ModelForm):
    class Meta:
        model=models.student
        fields = '__all__'