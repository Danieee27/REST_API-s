from django.db import models
from django.utils import timezone
from datetime import timedelta


# Create your models here.
class UserAccount(models.Model):
    Firstname = models.CharField(max_length = 50)
    Lastname = models.CharField(max_length = 50)
    Phone = models.IntegerField(default = 0)
    date_joined = models.DateTimeField(auto_now_add = True)

    


    def __str__(self):
        return self.Firstname + " " + self.Lastname
    
class OTP(models.Model):
    Phone = UserAccount.Phone
    OTP = models.IntegerField(default = 0)

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=5)

    def __str__(self):
        return str(self.Phone)
    

class Conversation(models.Model):
    sender = models.ForeignKey(UserAccount, on_delete = models.CASCADE, related_name = "sent_messages")
    receiver = models.ForeignKey(UserAccount, on_delete = models.CASCADE, related_name = "received_messages")
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Conversation between {self.sender} and {self.receiver}"

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete = models.CASCADE)
    sent_by = models.ForeignKey(UserAccount, on_delete = models.CASCADE) 
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)  

    def __str__(self):
        return f"Message in {self.conversation} at {self.timestamp}"   

