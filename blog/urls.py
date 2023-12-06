from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from django.views.decorators.cache import cache_page
from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView
from newsletter.apps import NewsletterConfig

app_name = BlogConfig.name

urlpatterns = [
                  path('blog_page/', cache_page(60)(BlogListView.as_view()), name='blog_page'),
                  path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
