import os , django , random , string , sys
from datetime import timedelta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'customermgmt.settings')
django.setup()

from faker import Faker

from customeractivity.models import UserDetails , UserActivityPeriod

def createUser(n):
    '''
    Create User Data 
    Input : n Number of Record to be created
    '''
    fake = Faker()
    for _ in range(int(n)):
        user_id = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k = 6))
        name = fake.name()
        country = fake.country()
        city = fake.city()
        UserDetails.objects.create(
            user_id= user_id,
            name= name,
            country= country,
            city= city
        )

def createActivityData(n):
      '''
    Create User  Activity Data 
    Input : n Number of Record to be created
    '''

    fake = Faker()
    idList = UserDetails.objects.all().values_list('user_id',flat=True)
    for _ in range(n):
        userid = UserDetails.objects.get(user_id=random.choice(idList))
        # to make sure end date not less than start date
        enddate = fake.date_time_between(start_date='-1y')
        startdate = enddate - timedelta(hours=3,minutes= 5)
        UserActivityPeriod.objects.create(
            userid=userid,
            start_date=startdate,
            end_date=enddate
        )

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])