from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


# Table booking API: GET /api/bookings/, POST /api/bookings/,
# GET/PUT/PATCH/DELETE /api/bookings/<id>/
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


# Menu API: GET /api/menu-items/ and POST /api/menu-items/
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


# GET/PUT/PATCH/DELETE /api/menu-items/<id>/
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
