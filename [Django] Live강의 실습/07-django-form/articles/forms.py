from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

# Models 정보 받아오자~
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class':'my-title'
            }
        )
    )
    # model 등록!
    class Meta:
        model = Article
        fields = '__all__'