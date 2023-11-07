from random import choices
from django.db import models
import datetime
class Account(models.Model):
    name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=12,default=None)
    paid = models.BooleanField(default=False)
    class months(models.TextChoices):
        zero = "1", "1"
        one = "2", "2"
        Two = "3", "3"
        Three = "4", "4"
        four = "5", "5"
        five = "6", "6"
        six = "7", "7"
        seven = "8", "8"
        eight = "9", "9"
        nine = "10", "10"
        ten = "11", "11"
        eleven = "12", "12"

    class years(models.TextChoices):
        zero = "2022", "2022"
        one = "2023", "2023"
        two = "2024", "2024"

    month =  models.TextField(max_length=3, choices=months.choices,default=months.zero)
    year =  models.TextField(max_length=5, choices=years.choices,default=years.zero)

    class boxes(models.TextChoices):
        zero = "0", "enter a box"
        one = "1", "HFC"
        Two = "2", "بهيج كريم"
        Three = "3", "د بسام"
        four = "4", "مكي"
        five = "5", "احمر 1"
        six = "6", "احمر 2"
        seven = "7", "الصيدلية"
        eight = "8", "ام ربيع المقداد"
        nine = "9", "انور"
        ten = "10", "بربيش"
        eleven = "11", "ابوحسين حمية"
        twelve = "12", "ابو طلال"
        thirteen = "13", "الخياط"
        fourteen = "14", "الفوال"
        fifteen = "15", "المصلى"
        sixteen = "16", "النادي"
        seventeen = "17", "بناية يسام"
        eighteen = "18", "بناية مكة"
        ninteen = "19", "شميس"
        twenty = "20", "فهمي حمية"
        twentyone = "21", "محمود الماي"
        twentytwo = "22", "مزنر"
        twentythree = "23", "هاني الحلاق"
        twentyfour = "24", "بيت مهدي"
        twentyfive = "25", "حسن فروج"
        twentysix = "26", "حسين مهدي"
        twentyseven = "27", "دكان هنا"
        twentyeight = "28", "زين الدين"
        twentynine = "29", "علي عبدالله"
        thirty = "30", "عزو"
        thirtyone = "31", "عقل"
        thirtytwo = "32", "غيث"
        thirtythree = "33", "كرم"
        thirtyfour = "34", "نادي حمزة"
        thirtyfive = "35", "دكان هاني"
        thirtysix = "36", "هزيمة"
        thirtyseven = "37", "احمر 3"
        thirtyeight = "38", "المستوصف"
        thirtynine = "39", "نمرة"
        fourty = "40", "حي عبدالساتر"
        fourtyone = "41", "غزال"
        fourtytwo = "42", "دكان جابر"
        fourtythree = "43", "شحرور"
        fourtyfour = "44", "شمص"
        fourtyfive = "45", "عوض"
        fourtysix = "46", "فارس"
        fourtyseven = "47", "قاسم"
        fourtyeight = "48", "كموني"
        fourtynine = "49", "يزبك"

    box =  models.CharField(max_length=12, choices=boxes.choices,default=boxes.zero)

    paid = models.BooleanField(default=False)

    active = models.BooleanField(default=True)
    
    def get_paid(self):
        if (int(self.year)+int(self.month)) >= (int(datetime.datetime.now().year)+int(datetime.datetime.now().month)):
            return True
        else:
            return False

    def save(self, *args, **kwargs):
        self.paid = self.get_paid()
        super(Account, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.paid = self.get_paid()
        super(Account, self).update(*args, **kwargs)


    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.username