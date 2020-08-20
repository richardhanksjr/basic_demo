import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.views import View


# @login_required
# def create_post(request):
#     if request.method == "POST":
#         title = request.POST.get('title')
#         body = request.POST.get('body')
#         category = request.POST.get('category')
#         user = request.user
#         Post.objects.create(title=title, body=body, category=category, user=user)
#         return render(request, 'ui/post.html')
#     return HttpResponse('works')

class CreatePost(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse('works')

    def post(self, request):
        title = request.POST.get('title')
        body = request.POST.get('body')
        category = request.POST.get('category')
        user = request.user
        Post.objects.create(title=title, body=body, category=category, user=user)
        last_history = Post.objects.update_or_create(name='test',
                                                     defaults={
                                                         'message': 'test'
                                                     })
        return render(request, 'ui/post.html')

class RandomNumber(View):
    def get(self, request):
        random_number = random.randint(1, 1000)
        return JsonResponse({'random_number': random_number})
