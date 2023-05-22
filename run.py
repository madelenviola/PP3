date_input = input ("Please enter month and date of birth (MM/DD): ")

month, day = date_input.split('/')

interval_message = ""
key_pressed1 = ""
key_pressed2 = ""
key_pressed3 = ""

if (month == '03' and 21 <= int(day)) or (month == '04' and int(day) <=19):
    interval_message = "You're a Aries"
    key_pressed1 = "Best career match for Aries is:"
    key_pressed2 = "How to succeed as a Aries:"
    key_pressed3 = "Aries Celbrities:"
elif (month == '04' and 20 <= int(day)) or (month == '05' and int(day) <=20):
    interval_message = "You're a Taurus"
    key_pressed1 = "Best career match for Taurus is: Chef, Artist, Interior Designer, Architect, Construction, Politician, Fashion Designer, Botanist, Biologist. "
    key_pressed2 = "How to succeed as a Taurus: You are someone people can count on, and that is super important. At times when people don't follow through on things, you know and understand how crucial it is to keep your word. Your weaknesses of being very obstinate and overprotective can fall heavy on you. You can also be stubborn to the point of not compromising which is a major rule-breaker for success."
    key_pressed3 = "Taurus Celbrities: Elizabeth II, Adele, Robert Pattinson, The Rock, George Clooney, Tina Fey, Channing Tatum, Jessica Alba, Dev Patel to name a few"
elif (month == '05' and 21 <= int(day)) or (month == '06' and int(day) <=21):
    interval_message = "You're a Gemini"
    key_pressed1 = "Best career match for Gemini is:"
    key_pressed2 = "How to succeed as a Gemini:"
    key_pressed3 = "Gemini Celbrities:"
elif (month == '06' and 22 <= int(day)) or (month == '07' and int(day) <=22):
    interval_message = "You're a Cancer"
    key_pressed1 = "Best career match for Cancer is:"
    key_pressed2 = "How to succeed as a Cancer:"
    key_pressed3 = "Cancer Celbrities:"
elif (month == '07' and 23 <= int(day)) or (month == '08' and int(day) <=22):
    interval_message = "You're a Leo"
    key_pressed1 = "Best career match for Leo is:"
    key_pressed2 = "How to succeed as a Leo:"
    key_pressed3 = "Leo Celbrities:"
elif (month == '08' and 23 <= int(day)) or (month == '09' and int(day) <=22):
    interval_message = "You're a Virgo"
    key_pressed1 = "Best career match for Virgo is:"
    key_pressed2 = "How to succeed as a Virgo:"
    key_pressed3 = "Virgo Celbrities:"
elif (month == '09' and 23 <= int(day)) or (month == '10' and int(day) <=23):
    interval_message = "You're a Leo"
    key_pressed1 = "Best career match for leo is:"
    key_pressed2 = "How to succeed as a Leo:"
    key_pressed3 = "Leo Celbrities:"
elif (month == '10' and 24 <= int(day)) or (month == '11' and int(day) <=21):
    interval_message = "You're a Scorpio"
    key_pressed1 = "Best career match for Scorpio is:"
    key_pressed2 = "How to succeed as a Scporpio:"
    key_pressed3 = "Scorpio Celbrities:"
elif (month == '11' and 22 <= int(day)) or (month == '12' and int(day) <=21):
    interval_message = "You're a Sagittarius"
    key_pressed1 = "Best career match for Sagittarius is:"
    key_pressed2 = "How to succeed as a Sagittarius:"
    key_pressed3 = "Sagittarius Celbrities:"
elif (month == '12' and 22 <= int(day)) or (month == '01' and int(day) <=19):
    interval_message = "You're a Capricorn"
    key_pressed1 = "Best career match for Capricorn is:"
    key_pressed2 = "How to succeed as a Capricorn:"
    key_pressed3 = "Capricorn Celbrities:"
elif (month == '01' and 20 <= int(day)) or (month == '02' and int(day) <=18):
    interval_message = "You're a Aquarius"
    key_pressed1 = "Best career match for Aquarius is:"
    key_pressed2 = "How to succeed as a Aquarius:"
    key_pressed3 = "Aquarius Celbrities:"
elif (month == '02' and 19 <= int(day)) or (month == '03' and int(day) <=20):
    interval_message = "You're a Pisces"
    key_pressed1 = "Best career match for Pisces is:"
    key_pressed2 = "How to succeed as a Pisces:"
    key_pressed3 = "Pisces Celbrities:"

if interval_message:
    print(interval_message)

    key = input ("Press the key '1' for Best career match, key '2' for How to succeed or key '3' to see celebrities sharing your star sign: ")

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