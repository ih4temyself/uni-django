import datetime

from django.http import HttpResponse
from django.shortcuts import render


def christmas_checker(request):
    today = datetime.date.today()
    christmas = today.day == 13 and today.month == 9
    data = {"today": christmas}
    return render(request, "home.html", data)


if __name__ == "__main__":
    today = datetime.date.today()
    print(today.month)
    print(today.day)
    print(today.day == 13 and today.month == 9)
