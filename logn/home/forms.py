from django import forms
from .models import Student, Emp, Sigh

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = '__all__'

class SignForm(forms.ModelForm):
    class Meta:
        model = Sigh
        fields = '__all__'

