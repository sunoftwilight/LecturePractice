from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'maxlength': 10,                 # 텍스트 10자까지만 넣을수 있다 x 텍스트 박스 크기가 10글자 만큼이다
            }
        ),
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={'required': '내용을 입력해주삼.'}
    )

    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title', )     # title을 포함
        # exclude = ('title', )    # title만 제외