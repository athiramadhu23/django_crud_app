from twilio.rest import Client
import random
otp = random.randint(1000, 9999)

a = "ACaef2b82556926724afffcb345d6267ab"

b = "22160875d22158c9289e24d61e2b8c49"

abc = Client(a, b)

abc.messages.create(from_="(209) 270-5686", to="+917994544534", body="Your verification code is - "+str(otp))

