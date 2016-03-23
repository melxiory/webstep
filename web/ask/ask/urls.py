from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from qa import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^question/', include('qa.urls')),
    url(r'^$', include('qa.urls')),
    url(r'^login/.*$',views.login_view),
    url(r'^signup/.*$',views.signup),
    url(r'^ask/.*$',views.question_add),
    url(r'^popular/.*$',views.popular),
    url(r'^answer/.*$',views.answer_add),
    url(r'^question/(?P<question_id>[0-9]+)/answer/$', views.answer_add, name='answer_add'),
    url(r'^new/.*$',views.test),
    url(r'^admin/', include(admin.site.urls)),
)
