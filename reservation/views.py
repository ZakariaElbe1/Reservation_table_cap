from django.shortcuts import render
import datetime
from rest_framework import generics, viewsets
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.

def index(request):
    current_year = datetime.datetime.now().year
    return render(request, 'index.html', {'current_year': current_year})


class MenuItemsView(generics.ListCreateAPIView):

    queryset= Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset= Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated] 
    





