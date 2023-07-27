from typing import Any, Dict
from django.shortcuts import render,get_object_or_404
from . models import Post
from . models import Comment
from . forms import Commentform
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

def starting_post(request):
   latest_posts=Post.objects.all().order_by("-date")[:3]

   return render (request, "du2/index.html", {
     "posts": latest_posts
          })


def post(request):
  all_posts=Post.objects.all().order_by("-date")
  return render(request,"du2/all-posts.html", {
     "all_posts": all_posts
  })


class post_detail(View):
     
     def is_stored_post(self,request,post_id):
         stored_posts=request.session.get("stored_posts")
         if stored_posts is not None:
            is_saved_for_later= post_id in stored_posts
         else:
             is_saved_for_later=False

         return is_saved_for_later

     def get(self, request, slug):
           posts=Post.objects.get(slug=slug)
           context={
               "post":posts,
               "post_tags": posts.tags.all(),
               "comment_form": Commentform(),
               "comments": posts.comments.all(),
               "save_for_later": self.is_stored_post(request,posts.id)
           }
           return render(request, "du2/post-detail.html", context)
       
     def post(self,request, slug):
          comment_form= Commentform(request.POST)
          posts=Post.objects.get(slug=slug)

          if comment_form.is_valid():
            comment= comment_form.save(commit=False)
            comment.posts=posts
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))
           
          context={
               "post":posts,
               "post_tags": posts.tags.all(),
               "comment_form": comment_form,
               "comments": posts.comments.all(),
               "save_for_later": self.is_stored_post(request,post.id)
           }

          return render(request, "du2/post-detail.html", context)



#  def post_detail(request, slug):
#    identified_post= get_object_or_404(Post,slug=slug)
#    return render(request,"du2/post-detail.html",
#                  {
#                     "post":identified_post
#                  })

class Readlater(View):


     def get(self,request):
         stored_posts= request.session.get("stored_posts")

         context={}

         if stored_posts is None or len(stored_posts)==0:
             context["posts"]=[]
             context["has_posts"]=False
         else:
             posts=Post.objects.filter(id__in=stored_posts)
             context["posts"]=posts
             context["has_posts"]=True


         return render(request,"du2/stored_post.html", context)
         

     def post(self,request):
         stored_posts= request.session.get("stored_posts")


         if stored_posts is None:
             stored_posts=[]
        
         post_id = int(request.POST["post_id"])


         if post_id not in stored_posts:
             stored_posts.append(post_id)
         else:
             stored_posts.remove(post_id)

         request.session["stored_posts"]= stored_posts

         return HttpResponseRedirect("/")