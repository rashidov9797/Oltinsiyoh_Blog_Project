
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView



from .models import Category, Post,Comment

from .forms import PostForm, EditForm, CommentForm

from django.urls import  reverse_lazy,reverse
from django.http import HttpResponseRedirect
# Create your views here.


# LIKES
def LikeView(request,pk):
  post = get_object_or_404(Post,id=request.POST.get('post_id'))
  liked=False
  if post.likes.filter(id=request.user.id).exists():
    post.likes.remove(request.user)
    liked=False
  else:
    post.likes.add(request.user)
    liked=True
  return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))


# HOME
class HomeView(ListView):
  model = Post
  template_name = 'home.html'
  ordering = ['-post_date']
   
  def get_context_data(self,*args,**kwargs):
    cat_menu = Category.objects.all()
    context = super(HomeView,self).get_context_data(*args,**kwargs)
    context["cat_menu"] = cat_menu
    return context



def CategoryListView(request):
  cat_menu_list = Category.objects.all()
  return render(request,'category_list.html', {'cat_menu_list' : cat_menu_list})



def CategoryView(request,cats):
  category_posts = Post.objects.filter(category=cats.replace('-', ' '))
  return render(request,'categories.html', {'cats': cats.title().replace('-', ' ').title(), 'category_post':category_posts})


# ArticlesDetailView

class ArticlesDetailView(DetailView):
  model = Post
  template_name = 'articles_detail.html'

  def get_context_data(self,*args,**kwargs):
    cat_menu = Category.objects.all()
    context = super(ArticlesDetailView,self).get_context_data(*args,**kwargs)
    
    stuff = get_object_or_404(Post,id=self.kwargs['pk'])
    total_likes = stuff.total_likes()

    liked = False
    if stuff.likes.filter(id=self.request.user.id).exists():
      liked = True
    
    context["cat_menu"] = cat_menu
    context["total_likes"] = total_likes
    context["liked"] = liked
    return context

# ADD_POST
class AddPostView(CreateView):
  model = Post
  form_class = PostForm
  template_name = 'add_post.html'




  def form_valid(self,form):
    form.instance.author = self.request.user
    return super().form_valid(form)


# User superuser ekanini tekshiramiz

  # def test_func(self):
  #   return self.request.user.is_superuser
    




 

class AddCategoryView(CreateView):
  model = Category
  template_name = 'add_category.html'
  fields = '__all__'


 


class UpdatePostView(UpdateView):
  model = Post
  template_name = 'update_post.html'
  fields = ('title','body','header_image','category','snippet')
  
  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user



  



class DeletePostView(DeleteView):
  model = Post
  template_name = 'delete_post.html'
  success_url = reverse_lazy('home')


  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user




# KOMMENTARY

class AddCommentView(CreateView):
  model = Comment
  form_class = CommentForm
  template_name = 'add_comment.html'
  success_url = reverse_lazy('home')





    


