from django.shortcuts import render, render_to_response
# Create your views here.
def home(recuest):
    return render_to_response("posts.html",{})