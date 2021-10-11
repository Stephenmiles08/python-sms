import os
from twilio.rest import Client

def cls():
  os.system("cls")
class smsd:
  def __init__(self):
      self.from_num = input("Messages from what phone number: ")
      self.to_num = input("Messaegs to what phone number: ")
      self.country_code = input("What is your country code: ")
      self.message = input("What message would you like to send to {self.country_code}{self.to_num[1:]}
      cls()
      self.meg()
      
  def personalinfo(self):
      account_sid = "Enter your account_sid (from twilio)"
      auth_token = "Enter your auth_token"
      
      self.client = Client(account_sid, auth_token)
      
  def meg(self):
    self.personalinfo()
    message = self.client \ 
                          .create(
                              body=f"{self.message}",
                              from_=f"{self.from_num},
                              to=f"self.to_num")
    print("Message successfully delivered!")
check = smsd()
