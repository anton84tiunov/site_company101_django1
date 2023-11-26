import re
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_json_widget.widgets import JSONEditorWidget                                                            
from .models import CustomUser, News
from django.core.exceptions import ValidationError
# from ckeditor_uploader.widgets import CKEditorUploadingWidget

# fields = ('id', 'password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'is_news_update', 'is_news_delete', 'is_news_insert'

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ["author", "author_last_update"]
        fields = ('contents_style','contents_script','contents',)

        # widgets = {
        #     'contents_style': JSONEditorWidget
        # }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError("начинается с цифры")
        return title




# class NewsArticleForm(forms.ModelForm):
#     class Meta:
#         model = News
#         fields = ['title', 'content', 'photo', 'is_published']



