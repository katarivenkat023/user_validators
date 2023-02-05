from django import forms

def validate_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('name start with a')

def validate_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('low lenght')
# write forms here
class Name_Form(forms.Form):
    name = forms.CharField(max_length=150,validators=[validate_for_a,validate_for_len])
    age = forms.IntegerField()
    email = forms.EmailField(max_length=100)
    Reemail = forms.EmailField(max_length=100)
    bootcatch = forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['Reemail']
        if e!=r:
            raise forms.ValidationError('not math')
    
    def bootcatch(self):
        bot=self.cleaned_data['bootcatch']
        if len(bot)>=0:
            raise forms.ValidationError('bot is catch')





