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
        "celebrities": "text here",
        "secret": "Your secret weapon is: Strong, adamant, and forged in fire, it's fitting that Aries' secret weapon is iron, one of the strongest elements. Weld, cast, machine, forge, temper, harden, or anneal it, iron can take on a seemingly limitless range of shapes and qualities. For an Aries, an iron-rich diet can boost confidence and performance."
    },
StarSign.TAURUS: {
        "career": "Best Job: Stylist or designer",
        "celebrities": "text here",
        "secret": "Your secret weapon is: Willpower. Think of its symbol, the bull (or even a bulldozer), and you've got an idea of how Taurus gets things done. They push, roll over, and dominate whatever challenges they're facing until those challenges are history. They're also a model for perseverance—when a Bull decides to do something, they get it done."
    },
StarSign.GEMINI: {
        "career": "Best Job: Teacher or public relations",
        "celebrities": "text here",
        "secret": "Your secret weapon is: Intelligence. Gemini is quick-witted and can read a room or situation in an almost supernatural way. Without saying very many words, a Gemini soon knows who has an agenda, who's a good ally, and who may need someone to bolster them up. Because of this, Gemini is an amazing friend."
    },
StarSign.CANCER: {
        "career": "Best Job: CEO or nutritionist",
        "celebrities": "text here",
        "secret": "Your secret weapon is: Emotions. While many Cancer signs probably get the message to be less emotional, the huge range and depths of Cancers' emotions may in fact be their secret weapon. When this sign is happy, the world knows it; when they're unhappy, the world will work to shift their situation. "
    },
StarSign.LEO: {
        "career": "Best Job: Salesperson, hairstylist or actor",
        "celebrities": "text here",
        "secret": "Your secret weapon is: A giving nature. Most people assume that Lions are all about themselves. But appearances are deceiving. A Leo's secret weapon is his or her boundless capacity for love, affection, and generosity."
    },
StarSign.VIRGO: {
        "career": "Best Job: Sub-editor or technician",
        "celebrities": "text here",
        "secret": "Your secret weapon is: Incredibly hard working. When this sign wants something, they'll work for it. They're also good at making the most of things friends look to them to help them with a DIY project or redecorate their home. "
    },
StarSign.LIBRA: {
        "career": "Best Job: Lawyer, counsellor or make-up artist",
        "celebrities": "text here",
        "secret": "Your secret weapon is: Imagination. Librans' imagination is unmatched, and they can always come up with a new way of looking at an issue. Libra is also blessed with boundless creativity. "
    },
StarSign.SCORPIO: {
        "career": "Best Job: Surgeon, investigator or sex therapist",
        "celebrities": "text here",
        "secret": "Your secret weapon is: Empathy. Also it may not seem this way at first glance, watchful Scorpio can read a room very quickly and can clue into how everyone else is feeling. "
    },
StarSign.SAGITTARIUS: {
        "career": "Best Job: Publisher or travel blogger",
        "celebrities": "text here",
        "secret": "Your secret weapon is: Independence. Sags don't need other people's approval, opinions, or advice. A Sag loves hanging out with herself, and feels like doing things solo can only help her connect more to her deepest self. "
    },
StarSign.CAPRICORN: {
        "career": "Best Job: The Boss",
        "celebrities": "text here",
        "secret": "Your secret weapon is: Tenacity. They believe that they truly can do anything, and they will dig in and get it done, no matter how exhausting or tedious the task. "
    },
StarSign.AQUARIUS: {
        "career": "Best Job: Photographer, scientist or independent contractor",
        "celebrities": "text here",
        "secret": "Your secret weapon is: A Belief in the innate goodness of people. An Aquarian will never doubt you, even when you doubt yourself. Their ability to see the best in all people, even if people don't see those qualities in themselves. "
    },
StarSign.PISCES: {
        "career": "Best Job: Nurse, artist or astrologer",
        "celebrities": "text here",
        "secret": "Your secret weapon is: The realization that life is so much more than what we see. Pisces sign is in tune with the magic of everyday existence and can find beauty in all situations, even ones that may cause tears. "
    },       
}

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
    star_sign = StarSign.TAURUS
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
