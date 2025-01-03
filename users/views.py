from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login') 
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html',context)

def send_test_email(request):
    try:
        send_mail(
            'Test Email',
            'This is a test email sent using SendGrid.',
            'chiraghasija0609@gmail.com',  # Replace with your email
            ['chiraghasija0609@gmail.com'],  # Replace with the recipient's email
            fail_silently=False,
        )
        messages.success(request, "Test email sent successfully!")
    except Exception as e:
        messages.error(request, f"Failed to send test email. Error: {e}")
    return redirect('profile')  # Redirect to profile or any other page after sending email
