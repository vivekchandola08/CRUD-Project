from django.conf.urls import url
from BRMapp import views
urlpatterns=[
   url('view-books',views.viewbook),
   url('new-book',views.newbook),
   url('edit-book',views.editbook),
   url('delet-book',views.deletbook),
   url('search-book',views.searchbook),
   url('search',views.search),
   url('edit',views.edit),
   url(r'^add',views.add),
   url('login',views.userlogin),
   url('logout',views.userlogout),
]
