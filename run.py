date_input = input ("Please enter month and date of birth (MM/DD): ")

month, day = date_input.split('/')

interval_message = ""
key_pressed1 = ""
key_pressed2 = ""
Key_pressed3 = ""

if (month == '03' and 21 <= int(day)) or (month == '04' and int(day) <=19):
    interval_message = "You're a Aries"
    key_pressed1 = "This is option 1"
    key_pressed2 = "This is option 2"
    key_pressed3 = "This is option 3"
elif (month == '04' and 20 <= int(day)) or (month == '05' and int(day) <=20):
    interval_message = "You're a Taurus"
    key_pressed1 = "Chef, Artist, Interior Designer, Architect, Construction, Politician, Fashion Designer, Botanist, Biologist. "
    key_pressed2 = "You are someone people can count on, and that is super important. At times when people don't follow through on things, you know and understand how crucial it is to keep your word. Your weaknesses of being very obstinate and overprotective can fall heavy on you. You can also be stubborn to the point of not compromising which is a major rule-breaker for success."
    key_pressed3 = "This is option 3"
elif (month == '05' and 21 <= int(day)) or (month == '06' and int(day) <=21):
    interval_message = "You're a Gemini"
    key_pressed1 = "This is option 1"
    key_pressed2 = "This is option 2"
    key_pressed3 = "This is option 3"
elif (month == '06' and 22 <= int(day)) or (month == '07' and int(day) <=22):
    interval_message = "You're a Cancer"
    key_pressed1 = "This is option 1"
    key_pressed2 = "This is option 2"
    key_pressed3 = "This is option 3"
elif (month == '07' and 23 <= int(day)) or (month == '08' and int(day) <=22):
    interval_message = "You're a Leo"
    key_pressed1 = "This is option 1"
    key_pressed2 = "This is option 2"
    key_pressed3 = "This is option 3"
elif (month == '08' and 23 <= int(day)) or (month == '09' and int(day) <=22):
    interval_message = "You're a Virgo"
    key_pressed1 = "This is option 1"
    key_pressed2 = "This is option 2"
    key_pressed3 = "This is option 3"
elif (month == '09' and 23 <= int(day)) or (month == '10' and int(day) <=23):
    interval_message = "You're a Leo"
    key_pressed1 = "This is option 1"
    key_pressed2 = "This is option 2"
    key_pressed3 = "This is option 3"
elif (month == '10' and 24 <= int(day)) or (month == '11' and int(day) <=21):
    interval_message = "You're a Scorpio"
    key_pressed1 = "This is option 1"
    key_pressed2 = "This is option 2"
    key_pressed3 = "This is option 3"
elif (month == '11' and 22 <= int(day)) or (month == '12' and int(day) <=21):
    interval_message = "You're a Sagittarius"
    key_pressed1 = "This is option 1"
    key_pressed2 = "This is option 2"
    key_pressed3 = "This is option 3"
elif (month == '12' and 22 <= int(day)) or (month == '01' and int(day) <=19):
    interval_message = "You're a Capricorn"
    key_pressed1 = "This is option 1"
    key_pressed2 = "This is option 2"
    key_pressed3 = "This is option 3"
elif (month == '01' and 20 <= int(day)) or (month == '02' and int(day) <=18):
    interval_message = "You're a Aquarius"
    key_pressed1 = "This is option 1"
    key_pressed2 = "This is option 2"
    key_pressed3 = "This is option 3"
elif (month == '02' and 19 <= int(day)) or (month == '03' and int(day) <=20):
    interval_message = "You're a Pisces"
    key_pressed1 = "This is option 1"
    key_pressed2 = "This is option 2"
    key_pressed3 = "This is option 3"

if interval_message:
    print(interval_message)

    key = input ("Press '1' for Best career match, or '2' for How to succeed: ")

    if key == '1':
        print(key_pressed1)
    elif key == '2':
        print(key_pressed2)
    elif key == '3':
        print(key_pressed3)
    else:
        print("Please press '1' or '2'. ")
else: 
    print("Invalid format please add birth month and date MM/DD")