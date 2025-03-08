import ollama
import re
from youtube_transcript_api import YouTubeTranscriptApi
import requests
from bs4 import BeautifulSoup

from .models import *


def llm(video_id):
	video_url = "https://www.youtube.com/watch?v=" + video_id
	title = get_youtube_title(video_url)
	transcript = YouTubeTranscriptApi.get_transcript(video_id)

	content = ""
	for x in transcript:
		content += f'{ x["text"]} '
		
	response = ollama.chat(
	    model="deepseek-r1:7b",
	    messages=[
			{
				"role": "system", # can only have one system
				"content": f"You are a teacher teaching about {title}",
			},
			{
				"role": "assistant",
				"content": f"The contents of what you need to explain are on the following video transcript: {content}",
			},
			{
				"role": "user", # only have one user that will provide the query
				"content": f"please give me a detailed summary, formated with HTML, just need the contents inside the <body></body>",
			},
	    ],
		stream=False,
	)
	
	r = response["message"]["content"].split("</think>\n")[-1].split("<body>")[-1].split("</body>")[0].strip()
	return (video_url, video_id, title, r)


def save_response(response):
	url = response[0]
	slug = response[1]
	title = response[2]
	content = response[3]

	s = Summary(url=url, title=title, content=content, slug=slug)
	s.save()


def get_youtube_title(link):
	r = requests.get(link)
	soup = BeautifulSoup(r.text, "lxml")
	title = soup.title.text
	return (title)

