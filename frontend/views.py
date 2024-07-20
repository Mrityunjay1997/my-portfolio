from django.shortcuts import render,redirect
 

def index(request):
    return render(request, "portfolio/index.html")


def MyProjects(request):
    return render(request,'admin/projects.html')


def MyBlogs(request):
    return render(request,'admin/blog.html')


def MyGallery(request):
    return render(request,'admin/gallery.html')

def ContactUs(request):
    return render(request,'admin/contact.html')


def AboutMe(request):
    return render(request,'portfolio/about.html')


def ProjectDetails(request):
    return render(request,'admin/project-details.html')

def BlogDetails(request):
    return render(request,'admin/blog-details.html')