from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

class GithubContribs(View):
    """Fetches and format github conrib history."""
    def get(self, request):
        return HttpResponse('List of Contribs')
