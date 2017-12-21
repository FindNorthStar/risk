"""Risk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    # 2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from RiskAnalysis import views as app_views

urlpatterns = [
    url(r'^$', app_views.home, name='home'),
    url(r'^platform/', app_views.platform, name='platform'),
    url(r'^platformregion.json$', app_views.platform_region, name='platform_region'),
    url(r'^businessrelation.json$', app_views.business_relation, name='business_relation'),
    url(r'^price.json$', app_views.price, name='price'),
    url(r'^guotaiprice.json$', app_views.guotai_price, name='guotai_price'),
    url(r'^incomerate.json$', app_views.income_rate, name='income_rate'),
    url(r'^guotaiincomerate.json$', app_views.guotai_income_rate, name='guotai_income_rate'),
    url(r'^employseason.json$', app_views.employ_season, name='emoloy_season'),
    url(r'^employlevel.json$', app_views.employ_level, name='emoloy_level'),
    url(r'^newswords.json$', app_views.news_words, name='news_words'),
    url(r'^titlewords.json$', app_views.title_words, name='title_words'),
    url(r'^judgementprovince.json$', app_views.judgement_province, name='judgement_province'),
    url(r'^salarylevel.json$', app_views.salary_level, name='salary_level'),
    url(r'^admin/', admin.site.urls),

]
