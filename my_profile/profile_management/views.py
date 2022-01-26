from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from profile_management.models import Faculty, Member

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello DSSU!!!</h1><be><h3>Welcome to Our Team Profile</h3>")

def name(request):
    return HttpResponse("<h1>Nuttida Lapthanachai </h1> <h2> 620710405 </h2>")

def index(request):
    header_str1 = 'Nuttida Lapthanachai'
    header_str2 = 'Arthitaya Chomthong'
    template = loader.get_template('index.html')
    fac_list = Faculty.objects.filter(facname='Science')
    context = {
        'var1' : header_str1 ,
        'var2' : header_str2 , 
        'my_fac' : fac_list[0].facname
    }
    return HttpResponse(template.render(context,request))

def profile(request):
    header_str1 = 'YAMMIE'
    header_str2 = 'Nuttida Lapthanachai'
    header_str3 = '620710405'
    header_str4 = '21/01/2001'
    header_str5 = 'Discover New K-Series'
    template = loader.get_template('profile.html')
    context = {
        'var1' : header_str1 ,
        'var2' : header_str2 ,
        'var3' : header_str3 ,
        'var4' : header_str4 ,
        'var5' : header_str5
    }
    return HttpResponse(template.render(context,request))

def myweb(request):
    template = loader.get_template('index00.html')
    context = {
    }
    return HttpResponse(template.render(context,request))

def myweb0(request):
    header_str1 = 'YAMMIE'
    header_str2 = 'My name is Nuttida Lapthanachai'
    header_str3 = 'TANGMAY'
    header_str4 = 'My name is Arthitaya Chomthong'
    template = loader.get_template('index0.html')
    context = {
        'var1' : header_str1 ,
        'var2' : header_str2 ,
        'var3' : header_str3 ,
        'var4' : header_str4
    }
    return HttpResponse(template.render(context,request))

def yam(request):
    header_str1 = 'YAMMIE'
    header_str2 = 'Nuttida Lapthanachai'
    header_str3 = '21/01/2001'
    header_str4 = 'Mathematics, Statistics'
    header_str5 = 'R, Python, MySQL, HTML, CSS'
    template = loader.get_template('index1.html')
    context = {
        'var1' : header_str1 ,
        'var2' : header_str2 ,
        'var3' : header_str3 ,
        'var4' : header_str4 ,
        'var5' : header_str5
    }
    return HttpResponse(template.render(context,request))

def tangmay(request):
    header_str1 = 'TANGMAY'
    header_str2 = 'ARTHITAYA CHOMTHONG'
    header_str3 = '18/03/2001'
    header_str4 = 'Mathematics, Statistics'
    header_str5 = 'R, Python, MySQL, HTML, CSS'
    template = loader.get_template('index2.html')
    context = {
        'var1' : header_str1 ,
        'var2' : header_str2 ,
        'var3' : header_str3 ,
        'var4' : header_str4 ,
        'var5' : header_str5
    }
    return HttpResponse(template.render(context,request))

def contact(request):
    template = loader.get_template('index3.html')
    context = {
    }
    return HttpResponse(template.render(context,request))

def index_o(request):
    template = loader.get_template('index_o.html')
    context = {
    }
    return HttpResponse(template.render(context,request))

def index1_o(request):
    header_str1 = 'YAMMIE'
    header_str2 = 'Nuttida Lapthanachai'
    header_str3 = '21/01/2001'
    template = loader.get_template('index1_o.html')
    context = {
        'var1' : header_str1 ,
        'var2' : header_str2 ,
        'var3' : header_str3 
    }
    return HttpResponse(template.render(context,request))

def index2_o(request):
    header_str1 = 'TANGMAY'
    header_str2 = 'ARTHITAYA CHOMTHONG'
    header_str3 = '18/03/2001'
    template = loader.get_template('index2_o.html')
    context = {
        'var1' : header_str1 ,
        'var2' : header_str2 ,
        'var3' : header_str3 
    }
    return HttpResponse(template.render(context,request))