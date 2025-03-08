from django.shortcuts import render, redirect
from django.http import HttpResponse
import time

from .form import *
from .utils import *
from .models import *

# Create your views here.
def index(request):
	data = Summary.objects.all()

	if request.method == "POST":
		form = YoutubeLinkForm(request.POST)
		if form.is_valid():
			try:
				link = form.youtubeUrlValidation()
				video_id = link[1]
				response = llm(video_id)
				save_response(response)
				content = Summary.objects.get(slug=video_id)
			except Exception as e:
				print(e)
				return redirect("index")

			return redirect("content", link[1])

	else:
		form = YoutubeLinkForm()
	
	return render(request, "index.html", {
		"form": form,
		"data": data,
	})



def content(request, video_id):
	try:
		content = Summary.objects.get(slug=video_id)
	except Exception as e:
		print(e)
		return redirect("index")

	data = Summary.objects.all()
	return render(request, "summary.html", {
		"data": data,
		"summary": content,
	})
