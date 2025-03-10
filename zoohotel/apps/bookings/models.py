from django.db import models

class Booking(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    pricing = models.ForeignKey(HotelPricing, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected')])
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

class Accommodation(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
