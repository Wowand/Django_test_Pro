from django.shortcuts import render, render_to_response
from test_1.models import Post
# Create your views here.


def home(request):
    return render_to_response("posts.html", {'posts': Post.objects.all()})