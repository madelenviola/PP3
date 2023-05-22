date_input = input ("Please enter month and date of birth (MM/DD): ")

month, day = date_input.split('/')

interval_message = ""
key_pressed1 = ""
key_pressed2 = ""

if (month == '03' and 21 <= int(day)) or (month == '04' and int(day) <=19):
    interval_message "You're a Aries"
    key_pressed1 = "This is option 1"
    key_pressed2 = "This is option 2"
elif (month == '04' and 20 <= int(day)) or (month == '05' and int(day) <=20):
    interval_message "You're a Taurus"
    key_pressed1 = "This is option 1"
    key_pressed2 = "This is option 2"
elif (month == '05' and 21 <= int(day)) or (month == '06' and int(day) <=21):
    interval_message "You're a Gemini"
    key_pressed1 = "This is option 1"
    key_pressed2 = "This is option 2"
elif (month == '06' and 22 <= int(day)) or (month == '07' and int(day) <=22):
    interval_message "You're a Cancer"
    key_pressed1 = "This is option 1"
    key_pressed2 = "This is option 2"
elif (month == '07' and 23 <= int(day)) or (month == '08' and int(day) <=22):
    interval_message "You're a Leo"
    key_pressed1 = "This is option 1"
    key_pressed2 = "This is option 2"
elif (month == '08' and 23 <= int(day)) or (month == '09' and int(day) <=22):
    interval_message "You're a Virgo"
    key_pressed1 = "This is option 1"
    key_pressed2 = "This is option 2"
elif (month == '09' and 23 <= int(day)) or (month == '10' and int(day) <=23):
    print("You are a Leo")
    interval_message "You're a Leo"
    key_pressed1 = "This is option 1"
    key_pressed2 = "This is option 2"
elif (month == '10' and 24 <= int(day)) or (month == '11' and int(day) <=21):
    print("You are a Scorpio")
elif (month == '11' and 22 <= int(day)) or (month == '12' and int(day) <=21):
    print("You are a Sagittarius")
elif (month == '12' and 22 <= int(day)) or (month == '01' and int(day) <=19):
    print("You are a Capricorn")
elif (month == '01' and 20 <= int(day)) or (month == '02' and int(day) <=18):
    print("You are a Aquarius")
elif (month == '02' and 19 <= int(day)) or (month == '03' and int(day) <=20):
    print("You are a Pisces")
else: 
    print("Invalid format please add birth month and date MM/DD")