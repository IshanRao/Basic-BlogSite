

from django.urls import path
from . import views
app_name = "home"

urlpatterns = [
    path('',views.index,name="index"),
    path('signup/',views.signup,name="signup"),
    path('posts/',views.add_posts,name="posts"),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('posts/author/',views.filter_by_user,name="author_filter"),
    path('posts/archive/monthly/',views.filter_by_month,name="month_filter"),
    path('posts/archive/yearly/',views.filter_by_year,name="year_fiter"),
    path('posts/id/<int:post_id>',views.filter_by_id,name="id_filter"),
    
]

# We can give unique name to a URL pattern that help to identify the URL anywhere
# Namespacing concept is used to avoid confusion with name across multiple apps in the project
# So we will enclosee the URL within the namespace and it is a good practice to give namespace as the name of the app itself
# IN URL , string after the ? represents the query string that won't be written here in urls.py 
# <data type:value> for dynamic URL that is not passed as a query string 
# req.GET() returns only a single value which is not iterable in the for loop of the html tag ,hence we use filter() that retuns list
# all the time irrespective of the number of elements 