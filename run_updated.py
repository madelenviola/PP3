
import enum

class StarSign(enum.Enum):
    ARIES: "Aries"

    @property
    def career_option(self):
        return STAR_SIGN_CAREER_MATCH[self]['career']

STAR_SIGN_CAREER_MATCH = {
    StarSign.ARIES: {
        "career": "something",
        "celebrities": ""
    }
}



# STAR_SIGN_CAREER_MATCH = {
#     "Aries": "something"
# }

# STAR_SIGN_CAREER_MATCH = {
#     "Aries": "something"
# }



def _get_user_birth_date():
    """_summary_

    Returns:
        _type_: _description_
    """
    return input("Please enter month and date of birth (MM/DD): ")

def _validate_birth_date(date_input):
    date_parts = date_input.split("/")
    if len(date_parts) == 2:
        month, date = date_parts

        month = int(month)
        if month >= 1 and month <= 12
            return True

    return False


def _compute_user_star_sign(birth_date):
    month, day = birth_date.split("/")
    interval_message = ""
    key_pressed1 = ""
    key_pressed2 = ""
    key_pressed3 = ""

    if (month == "03" and 21 <= int(day)) or (month == "04" and int(day) <= 19):
        return StarSign.ARIES
        interval_message = "You're a Aries"
        key_pressed1 = "Best career match for Aries is:"
        key_pressed2 = "How to succeed as a Aries:"
        key_pressed3 = "Aries Celbrities:"
    elif (month == "04" and 20 <= int(day)) or (month == "05" and int(day) <= 20):
        interval_message = "You're a Taurus"
        key_pressed1 = "Best career match for Taurus is: Chef, Artist, Interior Designer, Architect, Construction, Politician, Fashion Designer, Botanist, Biologist. "
        key_pressed2 = "How to succeed as a Taurus: You are someone people can count on, and that is super important. At times when people don't follow through on things, you know and understand how crucial it is to keep your word. Your weaknesses of being very obstinate and overprotective can fall heavy on you. You can also be stubborn to the point of not compromising which is a major rule-breaker for success."
        key_pressed3 = "Taurus Celbrities: Elizabeth II, Adele, Robert Pattinson, The Rock, George Clooney, Tina Fey, Channing Tatum, Jessica Alba, Dev Patel to name a few"
    elif (month == "05" and 21 <= int(day)) or (month == "06" and int(day) <= 21):
        interval_message = "You're a Gemini"
        key_pressed1 = "Best career match for Gemini is:"
        key_pressed2 = "How to succeed as a Gemini:"
        key_pressed3 = "Gemini Celbrities:"
    elif (month == "06" and 22 <= int(day)) or (month == "07" and int(day) <= 22):
        interval_message = "You're a Cancer"
        key_pressed1 = "Best career match for Cancer is:"
        key_pressed2 = "How to succeed as a Cancer:"
        key_pressed3 = "Cancer Celbrities:"
    elif (month == "07" and 23 <= int(day)) or (month == "08" and int(day) <= 22):
        interval_message = "You're a Leo"
        key_pressed1 = "Best career match for Leo is:"
        key_pressed2 = "How to succeed as a Leo:"
        key_pressed3 = "Leo Celbrities:"
    elif (month == "08" and 23 <= int(day)) or (month == "09" and int(day) <= 22):
        interval_message = "You're a Virgo"
        key_pressed1 = "Best career match for Virgo is:"
        key_pressed2 = "How to succeed as a Virgo:"
        key_pressed3 = "Virgo Celbrities:"
    elif (month == "09" and 23 <= int(day)) or (month == "10" and int(day) <= 23):
        interval_message = "You're a Leo"
        key_pressed1 = "Best career match for leo is:"
        key_pressed2 = "How to succeed as a Leo:"
        key_pressed3 = "Leo Celbrities:"
    elif (month == "10" and 24 <= int(day)) or (month == "11" and int(day) <= 21):
        interval_message = "You're a Scorpio"
        key_pressed1 = "Best career match for Scorpio is:"
        key_pressed2 = "How to succeed as a Scporpio:"
        key_pressed3 = "Scorpio Celbrities:"
    elif (month == "11" and 22 <= int(day)) or (month == "12" and int(day) <= 21):
        interval_message = "You're a Sagittarius"
        key_pressed1 = "Best career match for Sagittarius is:"
        key_pressed2 = "How to succeed as a Sagittarius:"
        key_pressed3 = "Sagittarius Celbrities:"
    elif (month == "12" and 22 <= int(day)) or (month == "01" and int(day) <= 19):
        interval_message = "You're a Capricorn"
        key_pressed1 = "Best career match for Capricorn is:"
        key_pressed2 = "How to succeed as a Capricorn:"
        key_pressed3 = "Capricorn Celbrities:"
    elif (month == "01" and 20 <= int(day)) or (month == "02" and int(day) <= 18):
        interval_message = "You're a Aquarius"
        key_pressed1 = "Best career match for Aquarius is:"
        key_pressed2 = "How to succeed as a Aquarius:"
        key_pressed3 = "Aquarius Celbrities:"
    elif (month == "02" and 19 <= int(day)) or (month == "03" and int(day) <= 20):
        interval_message = "You're a Pisces"
        key_pressed1 = "Best career match for Pisces is:"
        key_pressed2 = "How to succeed as a Pisces:"
        key_pressed3 = "Pisces Celbrities:"

    if interval_message:
        print(interval_message)

        key = input(
            STAR_SIGN_OPTIONS
        )

        if key == "1":
            print(key_pressed1)
        elif key == "2":
            print(key_pressed2)
        elif key == "3":
            print(key_pressed3)
        else:
            print("Please press key '1', '2' or '3'. ")
    else:
        print("Invalid format please add birth month and date MM/DD")

STAR_SIGN_OPTIONS = """
"Press the 
    key '1' for Best career match, 
    key '2' for How to succeed or 
    key '3' to see celebrities sharing your star sign: "
"""

INSTRUCTION_MSG = """
Welcome to check yo8ur star sign
Select options:
  1. Get your star sign based on birth date.
  2. Show user stats
  3. Exit
"""
def start_start_sign_calculation():
    valid = False
    while not valid:
        birth_date_input = _get_user_birth_date()
        valid = _validate_birth_date(birth_date_input)

    star_sign = _compute_user_star_sign(birth_date_input)
    _show_further_options(star_sign)
    _update_stats(star_sign)

def _update_stats(star_sign):
    # Total visits in a day
    # Total visits so far
    # Visits by star sign
    # Most visited option - star sign menu
    # main menu

    # Load the worksheet
    # 


def start_app():
    while True:
        user_input = input(INSTRUCTION_MSG)
        if user_input == "1":
            start_start_sign_calculation()
        elif user_input == "2":
            show_stats()
        elif user_input == "3":
            sys.exit()
        else:
            print("Invalid input. Please try again.")




    # Output the star sign based on user input
    # Show some options to get more details about star sign
    # Repeat


if __name__ == "__main__":
    start_app()