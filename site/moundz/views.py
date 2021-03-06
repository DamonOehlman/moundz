# Create your views here.

from google.appengine.api import mail
from django.http import HttpResponse
from django.shortcuts import render_to_response
import logging
import os
import re

def empty_file(request):
    return HttpResponse()
    
def main(request):
    page_name = re.sub(r'^(.*?)(\.htm|\.html)?$', r'\1', request.path)
    
    # find the template name
    template_name = 'moundz' + page_name + '.html'
    index_template_name = 'moundz' + page_name + 'index.html'

    abs_templatepath = os.path.abspath("templates/" + template_name)
    
    # if we could not find the specified template, use the page not found template
    logging.info("looking for template: %s", abs_templatepath)
    if not os.path.exists(abs_templatepath):
        # check the index file
        abs_templatepath = os.path.abspath("templates/" + index_template_name)
        if os.path.exists(abs_templatepath):
            template_name = index_template_name
        else:
            template_name = 'moundz/page-not-found.html'
    
	# define the page context
    return render_to_response(template_name)