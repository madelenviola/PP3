date_input = input ("Please enter month and date of birth (MM/DD): ")

month, day = date_input.split('/')

if (month == '03' and 21 <= int(day)) or (month == '04' and int(day) <=19):
    print("You are a Aries")
elif (month == '04' and 20 <= int(day)) or (month == '05' and int(day) <=20):
    print("You are a Taurus")
elif (month == '05' and 21 <= int(day)) or (month == '06' and int(day) <=21):
    print("You are a Gemini")
