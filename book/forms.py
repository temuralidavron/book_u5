from django import forms

from book.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'file','isbn', 'price','description','image']


    # def clean_title(self):
    #     data = self.cleaned_data['title']
    #     if len(data)<3:
    #         raise forms.ValidationError("Title must be at least 3 characters long")
    #     return data


class EmailForm(forms.Form):
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    from_email = forms.EmailField()
    to_email = forms.EmailField()

