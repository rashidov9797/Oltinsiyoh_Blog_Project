from django import  forms
from .models import Post, Category, Comment


choices = Category.objects.all().values_list('name','name')


choices_list =[]

for item in choices:
    choices_list.append(item)

class PostForm(forms.ModelForm): 
    class Meta:
        model = Post
        fields = ('title', 'author', 'category' ,'body','snippet','header_image')

        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control',}),

        # 'title_tag':forms.TextInput(attrs={'class':'form-control ','placeholder':'Title nomini kiriting'}),

        'author':forms.TextInput(attrs={'class':'form-control ', 'value': ' ' , 'type':'hidden' ,'placeholder':'Muallif nomini kiriting','id':'azik'}),

        # 'author': forms.Select(attrs={'class': 'form-control', }),

        'category': forms.Select(choices=choices_list, attrs={'class': 'form-control',}),

        
        'body':forms.Textarea(attrs={'class': 'form-control'}),

         
        'snippet':forms.Textarea(attrs={'class': 'form-control'}),
      }




class EditForm(forms.ModelForm): 
    class Meta:

        model = Post

        fields = ('title','body','snippet')

        widgets = {
        'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Maqola nomini kiriting'}),

        'title_tag':forms.TextInput(attrs={'class': 'form-control','placeholder':'Title nomini kiriting'}),

        'body':forms.Textarea(attrs={'class': 'form-control bg-dark col-md-10'}),
        'snippet':forms.Textarea(attrs={'class': 'form-control'}),
        }




# COMMENT

class CommentForm(forms.ModelForm): 
    class Meta:

        model = Comment

        fields = ('name','body')

        widgets = {

        'name':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Maqola nomini kiriting'}),
        'body':forms.Textarea(attrs={'class': 'form-control bg-dark col-md-10'}),
        }