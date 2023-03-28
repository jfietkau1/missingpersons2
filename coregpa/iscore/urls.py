from django.urls import path
from .views import indexPageView

#from .bootstrap import index.html   not sure if this is how I'm supposed to do this..
# I also notice that it imported a function, not a file. I think I need to make my html file into a function using the method in the views file


urlpatterns = [
    path("", indexPageView, name="index")
 
]












