from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from datetime import datetime
from .models import Post, Meetup, Page, Contact, Category
from .forms import ContactForm, CommentForm


def get_meetup():
    meetups = Meetup.objects.filter(fromdate=timezone.now()).order_by('-fromdate')[:5]
    return meetups
    

def get_category():
    categories = Category.objects.all()
    return categories


class HomeView(TemplateView):
    template_name = "pyladies_harare/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Home Page'
        context['posts'] = Post.objects.all().order_by('-published_date')
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
        return context


class AboutView(TemplateView):
    template_name = "pyladies_harare/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['title'] = 'About'
        context['pages'] = Page.objects.filter(slug='about')
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
        return context


class MeetupsView(TemplateView):
    template_name = "pyladies_harare/meetups.html"

    def get_context_data(self, **kwargs):
        context = super(MeetupsView, self).get_context_data(**kwargs)
        context['title'] = 'Our Meetups'
        context['pages'] = Page.objects.filter(slug='meetups')
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
        return context


class UpcomingView(TemplateView):
    template_name = "pyladies_harare/upcoming.html"

    def get_context_data(self, **kwargs):
        context = super(UpcomingView, self).get_context_data(**kwargs)
        context['title'] = 'Upcoming Meetups'
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
        return context


class PastMeetupsView(TemplateView):
    template_name = "pyladies_harare/past.html"

    def get_context_data(self, **kwargs):
        context = super(PastMeetupsView, self).get_context_data(**kwargs)
        context['title'] = 'Past Meetups'
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
        return context


class PostDetailView(TemplateView):
    template_name = "pyladies_harare/post_detail.html"
    comment_form = CommentForm()

    def get_context_data(self, pk, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Blog Post'
        context['categories'] = get_category()
        context['post'] = get_object_or_404(Post, pk=pk)
        context['meetups'] = get_meetup()
        context['comment_form'] = self.comment_form
        context['year'] = datetime.now().year
        return context


class ContactView(TemplateView):
    template_name = "pyladies_harare/contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['title'] = 'Contact Us'
        contact_form = ContactForm()
        context['contact_form'] = contact_form
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
        return context


class LoginView(TemplateView):
    template_name = "account/login.html"

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['title'] = 'Log in'
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
        return context


class SignupView(TemplateView):
    template_name = "account/signup.html"

    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        context['title'] = 'Sign Up'
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
        return context


class LogoutView(TemplateView):
    template_name = "account/logout.html"

    def get_context_data(self, **kwargs):
        context = super(LogoutView, self).get_context_data(**kwargs)
        context['title'] = 'Logged out'
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
        return context
