import enum

class StarSign(enum.Enum):
    ARIES = "Aries"
    TAURUS = "Taurus"
    GEMINI = "Gemini"
    CANCER = "Cancer"
    LEO = "Leo"
    VIRGO = "Virgo"
    LIBRA = "Libra"
    SCORPIO = "Scorpio"
    SAGITTARIUS = "Sagittarius"
    CAPRICORN = "Capricorn"
    AQUARIUS = "Aquarius"
    PISCES = "Pisces"

    @property
    def career_option(self):
        return STAR_SIGN_CAREER_MATCH[self]["career"]

    @property
    def celebrity_option(self):
        return STAR_SIGN_CAREER_MATCH[self]["celebrities"]

    @property
    def secret_option(self):
        return STAR_SIGN_CAREER_MATCH[self]["secret"]

STAR_SIGN_CAREER_MATCH = {
    StarSign.ARIES: {
        "career": "Best Job: Entrepreneur or journalist",
        "celebrities": "Seth Rogen, Lady Gaga, Eddie Murphy, Elton John",
        "secret": "Your secret weapon is: Strong, adamant, and forged in fire, it's fitting that Aries' secret weapon is iron, one of the strongest elements. Weld, cast, machine, forge, temper, harden, or anneal it, iron can take on a seemingly limitless range of shapes and qualities. For an Aries, an iron-rich diet can boost confidence and performance."
    },
StarSign.TAURUS: {
        "career": "Best Job: Stylist or designer",
        "celebrities": "Adele, Barbara Streisand, Queen Elizabeth II, Jerry Seinfeld",
        "secret": "Your secret weapon is: Willpower. Think of its symbol, the bull (or even a bulldozer), and you've got an idea of how Taurus gets things done. They push, roll over, and dominate whatever challenges they're facing until those challenges are history. They're also a model for perseverance—when a Bull decides to do something, they get it done."
    },
StarSign.GEMINI: {
        "career": "Best Job: Teacher or public relations",
        "celebrities": "Kanye West, Angelina Jolie, Clint Eastwood, Natalie Portman",
        "secret": "Your secret weapon is: Intelligence. Gemini is quick-witted and can read a room or situation in an almost supernatural way. Without saying very many words, a Gemini soon knows who has an agenda, who's a good ally, and who may need someone to bolster them up. Because of this, Gemini is an amazing friend."
    },
StarSign.CANCER: {
        "career": "Best Job: CEO or nutritionist",
        "celebrities": "Ariana Grande, Harrison Ford, Chris Pratt, Diana, Princess of Wales",
        "secret": "Your secret weapon is: Emotions. While many Cancer signs probably get the message to be less emotional, the huge range and depths of Cancers' emotions may in fact be their secret weapon. When this sign is happy, the world knows it; when they're unhappy, the world will work to shift their situation. "
    },
StarSign.LEO: {
        "career": "Best Job: Salesperson, hairstylist or actor",
        "celebrities": "Bill Clinton, Arnold Schwarzenegger, Barack Obama, Madonna",
        "secret": "Your secret weapon is: A giving nature. Most people assume that Lions are all about themselves. But appearances are deceiving. A Leo's secret weapon is his or her boundless capacity for love, affection, and generosity."
    },
StarSign.VIRGO: {
        "career": "Best Job: Sub-editor or technician",
        "celebrities": "Adam Sandler, Beyonce, Kobe Bryant, Zendaya",
        "secret": "Your secret weapon is: Incredibly hard working. When this sign wants something, they'll work for it. They're also good at making the most of things friends look to them to help them with a DIY project or redecorate their home. "
    },
StarSign.LIBRA: {
        "career": "Best Job: Lawyer, counsellor or make-up artist",
        "celebrities": "Avril Lavigne, Snoop Dogg, Cardi B, Kim Kardashian",
        "secret": "Your secret weapon is: Imagination. Librans' imagination is unmatched, and they can always come up with a new way of looking at an issue. Libra is also blessed with boundless creativity. "
    },
StarSign.SCORPIO: {
        "career": "Best Job: Surgeon, investigator or sex therapist",
        "celebrities": "Bill Gates, Leonardo DiCaprio, Hillary Clinton, Diego Maradona",
        "secret": "Your secret weapon is: Empathy. Also it may not seem this way at first glance, watchful Scorpio can read a room very quickly and can clue into how everyone else is feeling. "
    },
StarSign.SAGITTARIUS: {
        "career": "Best Job: Publisher or travel blogger",
        "celebrities": "Taylor Swift, Brad Pitt, Britney Spears, Steven Spielberg",
        "secret": "Your secret weapon is: Independence. Sags don't need other people's approval, opinions, or advice. A Sag loves hanging out with herself, and feels like doing things solo can only help her connect more to her deepest self. "
    },
StarSign.CAPRICORN: {
        "career": "Best Job: The Boss",
        "celebrities": "Anthony Hopkins, Kate Middleton, Tiger Woods, Bradley Cooper",
        "secret": "Your secret weapon is: Tenacity. They believe that they truly can do anything, and they will dig in and get it done, no matter how exhausting or tedious the task. "
    },
StarSign.AQUARIUS: {
        "career": "Best Job: Photographer, scientist or independent contractor",
        "celebrities": "Oprah Winfrey, Christian Bale, Cristiano Ronaldo, Ed Sheeran",
        "secret": "Your secret weapon is: A Belief in the innate goodness of people. An Aquarian will never doubt you, even when you doubt yourself. Their ability to see the best in all people, even if people don't see those qualities in themselves. "
    },
StarSign.PISCES: {
        "career": "Best Job: Nurse, artist or astrologer",
        "celebrities": "Adam Levine, Bon Jovi, Daniel Craig, Bruce Willis",
        "secret": "Your secret weapon is: The realization that life is so much more than what we see. Pisces sign is in tune with the magic of everyday existence and can find beauty in all situations, even ones that may cause tears. "
    },       
}

def _validate_birth_date(date_input):
    date_parts = date_input.split("/")
    if len(date_parts) == 2:
        month, day = date_parts

        if month.isdigit() and day.isdigit():
            month = int(month)
            day = int(day)

            if 1 <= month <= 12 and 1 <= day <= 31:
                return True

    return False

date_input = input("Please enter month and date of birth (MM/DD): ")

while not _validate_birth_date(date_input):
    if not date_input.replace('/', '').isdigit():
        print("Input not valid. Please enter a valid birth date in the format MM/DD")
        date_input = input("Enter month and date of birth in format (MM/DD): ")

month, day = date_input.split('/')

if (month == '03' and 21 <= int(day)) or (month == '04' and int(day) <=19):
    star_sign = StarSign.ARIES
elif (month == '04' and 20 <= int(day)) or (month == '05' and int(day) <=20):
    star_sign = StarSign.TAURUS
elif (month == '05' and 21 <= int(day)) or (month == '06' and int(day) <=21):
    star_sign = StarSign.GEMINI
elif (month == '06' and 22 <= int(day)) or (month == '07' and int(day) <=22):
    star_sign = StarSign.CANCER
elif (month == '07' and 23 <= int(day)) or (month == '08' and int(day) <=22):
    star_sign = StarSign.LEO
elif (month == '08' and 23 <= int(day)) or (month == '09' and int(day) <=22):
    star_sign = StarSign.VIRGO
elif (month == '09' and 23 <= int(day)) or (month == '10' and int(day) <=23):
    star_sign = StarSign.LIBRA
elif (month == '10' and 24 <= int(day)) or (month == '11' and int(day) <=21):
    star_sign = StarSign.SCORPIO
elif (month == '11' and 22 <= int(day)) or (month == '12' and int(day) <=21):
    star_sign = StarSign.SAGITTARIUS
elif (month == '12' and 22 <= int(day)) or (month == '01' and int(day) <=19):
    star_sign = StarSign.CAPRICORN
elif (month == '01' and 20 <= int(day)) or (month == '02' and int(day) <=18):
    star_sign = StarSign.AQUARIUS
elif (month == '02' and 19 <= int(day)) or (month == '03' and int(day) <=20):
    star_sign = StarSign.PISCES
    print("Star Sign: ", star_sign.value)


if star_sign:
    print("Star Sign: ", star_sign.value)

    key = input ("Press the key '1' for Best career match, key '2' for your signs secret weapon or press '3' to see celebrities sharing your star sign: ")

    if key == '1':
        print(star_sign.career_option)
    elif key == '2':
        print(star_sign.secret_option)
    elif key == '3':
        print(star_sign.celebrity_option)
    else:
        print("Please press '1', '2' or '3'. ")