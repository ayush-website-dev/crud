from django import forms  
from crud.models import CRUD  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = CRUD  
        fields = "__all__"  