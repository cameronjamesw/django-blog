from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.

def about_me(request):
    """
    Renders the About Page
    """
    if request.method == 'POST':
        collaboration_form = CollaborateForm(data=request.POST)
        if collaboration_form.is_valid():
            collaboration_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request submitted successfully, we will be in touch soon!!'
            )
            
    about = About.objects.all().order_by('-updated_on').first()

    collaboration_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
        "collaboration_form": collaboration_form,},
    )