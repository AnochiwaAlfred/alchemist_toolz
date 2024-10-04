import random
import string
from datetime import date
import math
import random


def randNumber(rand=4):
    import random
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(rand))
    return random_numbers


def shuffler(w1,w2,size=6,step=1):
    import math
    import random
    try:
        """
        This function requires 
        w1 = "myfirst leter"
        w2 = "second letter"
        size = "The length of the code generated"
        """
        full_word = f"{w1}{w2}"
        mt = math.pow(len(full_word), len(w1)) * 1000
        rd =  random.randint(a=0, b=mt)
        code = str(f"{full_word}{rd}").upper()
        f = list(code)
        random.shuffle(f)
        reshuffled = ''.join(f)
        return reshuffled[:size:step]
    except:
        pass


def generateUniqueId():
    # Generate 6 random numbers
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(6))
    # Generate 3 random capital alphabets
    random_alphabets = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    # Combine numbers and alphabets with a hyphen
    unique_id = f"{random_numbers}-{random_alphabets}"
    return unique_id


def generateStaffID():
    year = date.today().year
    brandInitials = "STL"
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
    staff_unique_id = f"{brandInitials}/{year}/S{random_numbers}"
    return staff_unique_id

def generateStudentRegistrationNumber(w1,w2,size=3,step=1):
    year = date.today().year
    brandInitials = "STL"

    full_word = f"{w1}{w2}"
    mt = len(full_word) ** len(w1) * 1000
    rd = random.randint(0, mt)
    code = str(f"{full_word}{rd}").upper()
    f = list(code)
    random.shuffle(f)
    reshuffled = ''.join(f)

    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
    student_unique_id = f"{brandInitials}/{year}/{str(reshuffled[:size:step]).upper()}/{random_numbers}".lower()
    return student_unique_id


def generateStaffID():
    year = date.today().year
    brandInitials = "STL"
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
    staff_unique_id = f"{brandInitials}/{year}/S{random_numbers}"
    return staff_unique_id


def generateStudentID():
    year = date.today().year
    brandInitials = "STL"
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
    student_unique_id = f"{brandInitials}/{year}/{random_numbers}"
    return student_unique_id

def generate_certificate_code(length=15):
    characters = string.ascii_lowercase + string.digits + '-'
    return ''.join(random.choice(characters) for _ in range(length))

