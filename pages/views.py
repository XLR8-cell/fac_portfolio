from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('''
        <html><body style="font-family:Arial;padding:40px;
        background:#0D1B3E;color:white"> 
        <h1 style="color:#C9A84C">FAC Academy Portfolio</h1>
        <p>Welcome to my Django web application!</p>
        <p><a href="/about" style="color:#C9A84C">About Me</a> |
           <a href="/contact" style="color:#C9A84C">Contact</a></p>
        </body></html>'''
    )
 
def about(request):
    return HttpResponse('<h1>About Me</h1><p>I am learning Django at FAC Academy!</p>')
 
def contact(request):
    return HttpResponse('<h1>Contact</h1><p>Email: brian@facacademy.com</p>')

