date_input = input ("Please enter month and date of birth (MM/DD):")

month, day = date_input.split('/')

if (month == "03" and 21 <= int(day) <=31) or (month == "04" and 1 <= int(day) <=19):
    print("You are a Aries")