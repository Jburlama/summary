from django import forms
from django.core.exceptions import ValidationError
import re


class YoutubeLinkForm(forms.Form):
	link = forms.CharField(
			widget=forms.TextInput(attrs={
				"class": "bg-light btn btn-primary btn-lg rounded-pill px-4 shadow-sm",
				"style": "color: #000000;",
				"placeholder": "Youtube Video URL ...",
				"name": "youtube_url",
			}))

	def youtubeUrlValidation(self):
		link = self.cleaned_data["link"]

		youtube_regex = (
		    r'(https?:\/\/)?'
		    '(?:www\.)?'
		    '(?:youtube\.com|youtu\.be)/'
		    '(?:watch\?v=|embed\/|v\/|.+\?v=)?([^&=%\s]+)'
		)
		
		pattern = re.compile(youtube_regex)
		match = pattern.match(link)
		
		if match:
		    return link, match.group(len(match.groups()))
		else:
			raise ValidationError("Invalid Youtube Video URL")
