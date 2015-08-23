# from __future__ import unicode_literals
from __future__ import division
#from numpy.ma import append
from django.template import Template, Context
import re, collections
import math
import string
from collections import Counter
from random import randint
from django.core.context_processors import csrf
from django.utils import timezone
from datetime import datetime
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
#from prediction_time.src import main_run
#from django.db.models import Avg
from django.template import Context, Template
import ast
#from notification.models import Notification
#from django.db.models.signals import post_save
#from notifications import notify
from django.db.models import Sum
import urllib
import random
from django.template import Template
import json
import pickle
from django.contrib import messages
#import textblob
#from textblob import TextBlob
#import language_check
from django.template import Library, Template
#from django.utils import simplejson
from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.utils.safestring import mark_safe
#from textblob._text import Context
import urllib2, urllib
import requests
from bs4 import BeautifulSoup
from savingadda.Flipkart import flipkart
from savingadda import Amazon
from Amazon import amazon
import nltk

def interface(request):

    return render(request, 'interface.html')

def get_product(request):

    if 'product' in request.GET and request.GET['product']:
        product = request.GET['product']

    flipkart_review = []
    amazon_review = []
    #response = urllib2.urlopen("https://affiliate-api.flipkart.net/affiliate/product/xml?id=XXX")
    #json_data = response.read()
    #return json_data
    #return HttpResponseRedirect('/interface/')
    #return HttpResponse(f)
    fk_string="http://www.flipkart.com/search?q="+product+"&as=off&as-show=off&otracker=start"

    amazon_string = "http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="+product
    flipkart_review=flipkart.scrape_flipkart(fk_string, 1)
    amazon_review=amazon.scrape_amazon(amazon_string, 1)
    tempf = "".join(flipkart_review)
    fk_split= tempf.split(" ")
    tempa = "".join(amazon_review)
    am_split= tempa.split(" ")

    nltk.pos_tag()
    nltk.pos_tag(amazon_review)
    #return render(request, 'interface.html',
                  #{'product':soup})


#def your_function():
    #response = urllib2.urlopen(https://affiliate-api.flipkart.net/affiliate/product/xml?id=XXX)
    #json_data = response.read()
    #return json_data #use this in any of your views to read json with product details
