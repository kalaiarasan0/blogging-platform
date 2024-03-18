from django.urls import path
from .views import HomeView,ArticleDetailView,CreateInputView,UpdatePostView,DeletePostView,CreateCategoryView,AddCommentView,CategoryView,CategoryListView,LikeView

urlpatterns = [
    path('',HomeView.as_view(),name='Home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='Articles-Detail'),
    path('inputdata', CreateInputView.as_view(), name='Input-Data'),
    path('createcategory', CreateCategoryView.as_view(), name='Add_Category'),
    path('article/update/<int:pk>', UpdatePostView.as_view(), name='Updata_Post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='Delete_Post'),
    path('category/<str:cats>/', CategoryView, name='Category_View'),
    path('category-list/', CategoryListView, name='Category_View_List'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]