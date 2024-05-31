from django.urls import path
from . import views as m
from register import views as v

urlpatterns = [
    path("", m.home, name="home"),
    path("about", m.about, name="about"),
    path("portfolio", m.portfolio, name="portfolio"),
    path("contact", m.contact, name="contact"),
    ]