from django import forms


# write forms here
class Name_Form(forms.Form):
    name = forms.CharField(max_length=150)
    age = forms.IntegerField()





