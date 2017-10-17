import time
from notifier import Notifier

notifier = Notifier()

classes = [(8, 9, 'Afr'), (9, 11, 'Chemistry'), (10, 11, 'Eng'), (12, 13, 'Lunch')]

print(classes)


while True:
    for time_slot in range(24):
        print(time_slot)
        for time_slot_start, time_slot_end, class_name in classes:
            if time_slot_start == time_slot:
                #print('\t{} - Your {} class started lazy wtf'.format(time_slot_start, class_name))
                notifier.notify('Do somthing')
            
            if time_slot_end == time_slot:
                #print('\t{} - Your {} class is finished'.format(time_slot_end, class_name))
                notifier.notify('Do something else')
        
        time.sleep(1)
import time
classes = [ (8,9, 'Physics Class'),(9,10, 'Chem Class'),(10,11,'English Class'),(12,13, 'Lunch')]

while True:
    for time_slot in range(24):
        for time_start, time_end, class_name in classes:
            if time_start == time_slot:
                print('\t{} - tring {} start' .format(time_start, class_name))
            if time_end == time_slot:
                print('\t{} - tring {} is finished' .format(time_end, class_name))
        time.sleep(1)
        Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
        
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Ebubechukwu A Achonu/AppData/Local/Programs/Python/Python36-32/school_bell.py