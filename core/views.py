from .forms import ResourceForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import User, Subject, Post, UserExtended, ContactSubmission, Resource

import json

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "core/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "core/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "core/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "core/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "core/register.html")


class SubjectListView(ListView):
    model = Subject
    context_object_name = 'subjects'
    template_name = 'core/subject_list.html'

class SubjectDetailView(DetailView):
    model = Subject
    context_object_name = 'subject'
    template_name = 'core/subject_detail.html'

class SubjectCreateView(CreateView):
    model = Subject
    fields = ['name', 'description']
    template_name = 'core/subject_form.html'
    success_url = reverse_lazy('subject_list')

class SubjectUpdateView(UpdateView):
    model = Subject
    fields = ['name', 'description']
    template_name = 'core/subject_form.html'
    success_url = reverse_lazy('subject_list')

class SubjectDeleteView(DeleteView):
    model = Subject
    context_object_name = 'subject'
    template_name = 'core/subject_confirm_delete.html'
    success_url = reverse_lazy('subject_list')

def forum(request):
    posts_list = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(posts_list, 10)

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, "core/forum.html", {"posts": posts})

def new_post(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    elif request.method == "POST":
        content = request.POST["post_content"]
        post = Post(post=content, user=request.user)
        post.save()
        return redirect('forum')
    return render(request, 'code/forum.html')

def faq(request): 
    return render(request, 'core/faq.html')

def contact(request):
    return render(request, 'core/contact_support.html')

def like_post(request, post_id):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Login required"}, status=401)

    try:
        post = Post.objects.get(pk=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True
        return JsonResponse({"likes": post.likes.count(), "liked": liked})
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found"}, status=404)


def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactSubmission.objects.create(name=name, email=email, message=message)

        # Add success message
        messages.success(request, 'Your message has been sent successfully!')

        # Render the same contact support template
        return render(request, 'core/contact_support.html')

    # If not POST request, just render the form
    return render(request, 'core/contact_support.html')

def upload_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resource_list')  # Redirect to the resource list page
    else:
        form = ResourceForm()
    return render(request, 'core/resource_form.html', {'form': form})

def resource_list(request):
    query = request.GET.get('query', '')
    grade_level = request.GET.get('grade_level', '')
    resource_type = request.GET.get('resource_type', '')
    
    resources = Resource.objects.all()
    if query:
        resources = resources.filter(title__icontains=query)
    if grade_level:
        resources = resources.filter(grade_level=grade_level)
    if resource_type:
        resources = resources.filter(resource_type=resource_type)

    context = {
        'resources': resources,
        'grade_levels': Resource.GRADE_LEVELS,
        'resource_types': Resource.RESOURCE_TYPES,
    }   

    return render(request, 'core/resource_list.html', {'resources': resources})

def resource_detail(request, resource_id):
    # Fetch the resource by ID or return 404 if not found
    resource = get_object_or_404(Resource, pk=resource_id)

    # Render the template with the resource context
    return render(request, 'core/resource_detail.html', {'resource': resource})