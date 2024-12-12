from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Payment, User, EVCenter, Booking
from .forms import UserRegistrationForm, BookingForm

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

# User Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('nearby_centers')  # Redirect to the nearby centers view
    return render(request, 'core/login.html')

# Display Nearby EV Centers
@login_required
def nearby_centers(request):
    query = request.GET.get('q', '')  # Get search query for filtering
    sort_by = request.GET.get('sort_by', 'name')  # Default sorting by name

    # Filter EV centers by name or location
    centers = EVCenter.objects.filter(name__icontains=query) | EVCenter.objects.filter(location__icontains=query)
    centers = centers.order_by(sort_by)

    return render(request, 'core/nearby_centers.html', {
        'centers': centers,
        'query': query,
        'sort_by': sort_by,
    })

# Book a Slot at a Specific EV Center
@login_required
def book_slot(request, center_id):
    center = get_object_or_404(EVCenter, id=center_id)
    if request.method == 'POST':
        slot = request.POST.get('slot')  # Slot time picked by the user
        booking = Booking.objects.create(
            user=request.user,
            center=center,
            slot=slot
        )
        return redirect('payment_page', booking_id=booking.id)  # Redirect to payment page
    return render(request, 'core/book_slots.html', {'center': center})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, Payment

def payment_page(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    payment_success = False
    payment = None
    if request.method == 'POST':
        # Simulate a payment process
        amount = 500  # Example amount
        payment = Payment.objects.create(
            booking=booking,
            amount=amount,
            payment_status='Pending'
        )
        # Simulate a successful payment
        payment.payment_status = 'Success'
        payment.save()
        payment_success = True  # Payment was successful
        
        # Redirect to the dashboard with payment details
        return redirect('dashboard', payment_id=payment.id)

    return render(request, 'core/payment_page.html', {'booking': booking})

def dashboard(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    return render(request, 'core/dashboard.html', {'payment': payment})

from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirects to the login page



