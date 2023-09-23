from django.urls import path, include, re_path
from apis import views 
 
urlpatterns = [ 
     re_path(r'^/', views.empty),          
     re_path(r'^api/list$', views.getList),
     re_path(r'^api/add$', views.addObject),
     re_path(r'^api/update$', views.addParameter),
     re_path(r'^api/getPeer$', views.getPeerById),
     re_path(r'^api/getProjectsList$', views.getProjectList),
     re_path(r'^api/getProject$', views.getProjectById)
]
# Document ID	about	avatar	contact	education	experience	favourites	myprojects	name	skills	uid
# 1011	"am an android developer"	"https://images.unsplash.com/photo-1603415526960-f7e0328c63b1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"	{phone: "9837724914", email: "aj@gmail.com"}	{institution: [{name: "iit delhi", major...]}	[{description: "random", wo...}]	["2011"]	["2011"]	"atishay"	["java", "kotlin", "android", "django"]	"aj5203"