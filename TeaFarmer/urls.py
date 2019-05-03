from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

import accounts
from TeaFarmer import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog_web.urls')),
    path('employee/', include('employee.urls')),
    path('farmer/',  include('farmer.urls')),
    path('', accounts.views.dashboard, name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
