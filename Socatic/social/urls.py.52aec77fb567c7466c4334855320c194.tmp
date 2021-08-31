from django.urls import path
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView,ProfileView, ProfileEditView, AddLike, AddDislike, AddCommentLike, AddCommentDislike, CommentReplyView, Explore , Blooddonation ,bloodform , News, PostListView1, PostDetailView1, PostEditView1, PostDeleteView1, CommentDeleteView1, AddLike1, AddDislike1, AddCommentLike1, AddCommentDislike1, CommentReplyView1,Plantation , Pform
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path('', Explore.as_view(), name='post-list'),
    path('animalrescue/', PostListView.as_view(), name='post-list1'),
    path('blooddonation/', Blooddonation.as_view(), name='blood-donation'),
    path('plantation/', Plantation.as_view(), name='plantation'),
    path('pform/', Pform.as_view(), name='pform'),
    path('news/', News.as_view(), name='news'),
    path('blooddonation/form/', bloodform.as_view(), name='blood-form'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/',
         CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:post_pk>/comment/<int:pk>/like',
         AddCommentLike.as_view(), name='comment-like'),
    path('post/<int:post_pk>/comment/<int:pk>/dislike',
         AddCommentDislike.as_view(), name='comment-dislike'),
    path('post/<int:post_pk>/comment/reply/<int:pk>',
         CommentReplyView.as_view(), name='comment-reply'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),

    #problems
    path('problems/', PostListView1.as_view(), name='post-list2'),   
    path('problems/post/<int:pk>/', PostDetailView1.as_view(), name='post-detail1'),
    path('problems/post/edit/<int:pk>/', PostEditView1.as_view(), name='post-edit1'),
    path('problems/post/delete/<int:pk>/', PostDeleteView1.as_view(), name='post-delete1'),
    path('problems/post/<int:post_pk>/comment/delete/<int:pk>/',
         CommentDeleteView1.as_view(), name='comment-delete1'),
    path('problems/post/<int:post_pk>/comment/<int:pk>/like',
         AddCommentLike1.as_view(), name='comment-like1'),
    path('problems/post/<int:post_pk>/comment/<int:pk>/dislike',
         AddCommentDislike1.as_view(), name='comment-dislike1'),
    path('problems/post/<int:post_pk>/comment/reply/<int:pk>',
         CommentReplyView1.as_view(), name='comment-reply1'),
    path('problems/post/<int:pk>/like', AddLike1.as_view(), name='like1'),
    path('problems/post/<int:pk>/dislike', AddDislike1.as_view(), name='dislike1'),

]
