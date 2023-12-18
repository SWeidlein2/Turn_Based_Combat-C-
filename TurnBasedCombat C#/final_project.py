#Sarah Weidlein
#Final Project
#This program creates a delivery system utilizing the scheduled arrival time along with accounting for possible delays and redirects 


#City list source: https://www.britannica.com/topic/list-of-cities-and-towns-in-the-United-States-2023068

from datetime import datetime,timedelta
from random import choice,randint

        
#Reports what the delay is along with how many minutes/hours till delivery
class time:
    def __init__(self,issue='',eta=0,sat=0,hours=0,update=''):
        self.issue=issue
        self.issue=issue
        self.eta=eta
        self.sat=sat
        self.hours=hours
        self.update=update

    def print_time(self):
        return time_update


#Class redirects driver to site refusal as a result of being delayed
class refusal(time):
    def __init__(self,site='',reason=''):
        time.__init__(self, issue='', eta=0,sat=00.00,hours=0)
        self.site=site
        self.reason=reason

    def standby(self):
        cities = open('cities.txt','r')
        my_city=cities.readlines()
        cities.close()
        print(f'Redirect created: {delivery}->{choice(my_city)} \nArrival: {time_sat.hour}:{time_sat.minute}')
        return choice(my_city)
      

while True:
    try: 
        vehicle_type= int(input('Please enter your vehicle type (53 ft truck or a 26 ft boxtruck): '))
        error_message=(f'Please enter either 53 or 26')

        if vehicle_type != 26 and vehicle_type != 53:
            raise ZeroDivisionError

        break

    except ZeroDivisionError as error_message:
        print(error_message)
        continue
    except ValueError:
        print('Error: a non-numerical number was inputted')
        continue

domicile_list=[
            'Los Angelas',
            'Austin',
            'Phoenix',
            'New York City',
            'Seattle'
        ]

while True:

    
        for city in domicile_list:
            print(f'{city}', end = ', 'if city != 'Seattle' else '')

        domicile=(input("\nFrom the provided list please provide your starting point or domicile: ")).lower()
        
        if domicile not in [city.lower() for city in domicile_list]:
            print(f'This is not a value in the list please enter: {domicile_list}')
            continue
        
        break
    


#Trailer list
trailer_list=[
    'V1234',
    'V5678',
    'V9875',
    'V4567',
    'V2977',
    'V2777',
    'V8976'
]

#Shows current time
schedule=datetime.now()
#Random selection from trailer list
trailer= randint(0,len(trailer_list)-1)
preload=trailer_list[trailer]
#Random selection between 200-1000 for distance
distance=choice(range(200,1000))
delivery=choice(domicile_list)


 #If-else statements to display SAT,Trailer, and distance along with ensuring the selected domicile isn't used for delivery location
if (vehicle_type == 53 and  domicile not in domicile_list):
    print(f'-----------------------------------------------------------')
    print(f"Scheduled arrival time: {schedule.month}/{schedule.day}/{schedule.year} at {schedule.hour}:{schedule.minute}")
    print(f'Driver is expected to pickup preloaded trailer: {preload}')
    print(f'Driver is to deliver trailer to: {delivery}')
    print(f'Distance to delivery is: {distance} miles')
    print(f'-----------------------------------------------------------')
elif(vehicle_type == 26 and domicile not in domicile_list):
    print(f'----------------------------------------------------------------------')
    print(f"Scheduled arrival time: {schedule.month}/{schedule.day}/{schedule.year} at {schedule.hour}:{schedule.minute}")
    print(f'Driver is expected to bring their own boxtruck to be live loaded')
    print(f'Driver is to deliver trailer to {delivery}')
    print(f'Distance to delivery is {distance} miles')
    print(f'-----------------------------------------------------------')
else:
    print(f'{error_message}')




while True:
        try:

            #Class Input
             time_issue=input(f'The driver is late to delivery please update the reason for delay (traffic,flat tire,etc): ')
             time_eta=int(input(f'Sorry to hear that {time_issue} occurred please enter the drivers ETA (10,30,40,100 minutes) : '))
             time_hours=int(input(f'Please input the hours you will be late from {time_issue}: '))
             time_sat=schedule + timedelta(hours=time_hours,minutes=time_eta)
             time_update=(f"The new ETA for delivery is: {time_sat.strftime('%H:%M')}")
             print(f'-----------------------------------------------------------')
             time_class= time(time_issue,time_eta,time_sat,time_hours,time_update)
             print(time_update)
             print(f'It looks like the {delivery} site is refusing to accept the load due to the late arrival of: {time_sat.hour}:{time_sat.minute} \nPlease standby as redirect is generated...')
             print(f'-----------------------------------------------------------')
             update=refusal()
             update.standby()
             break
        except ValueError:
            print('Error: a non-numerical number was inputted')
            continue


