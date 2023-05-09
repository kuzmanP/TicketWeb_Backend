from django.db import models


class Seat(models.Model):
    seat_number = models.CharField(max_length=20)
    venue = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.seat_number} ({self.venue})"


class Ticket(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.seat} for {self.event}-{self.ticket_id}"


class Event(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class EventManager(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    events = models.ManyToManyField(Event, blank=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    ticket_id = models.UUIDField()
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticket} paid {self.amount_paid} at {self.timestamp}"
