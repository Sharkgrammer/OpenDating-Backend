import random
import string
import time
from django.utils import timezone
from datetime import timedelta


def get_today():
    return timezone.now()


def get_days_ago(days):
    today = get_today()

    return today - timedelta(days=days)


def get_mins_ago(mins):
    today = get_today()

    return today - timedelta(minutes=mins)


def generate_random_string(n=10):
    return ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=n))


def wait_random_amount():
    randTime = random.uniform(0.2, 1)
    print("Waiting {} seconds...".format(randTime))

    time.sleep(randTime)
