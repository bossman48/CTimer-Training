from KTimer import KTimer
from Master import *
import time 

kTimer = KTimer()

masterObject = Master()

masterObject2 = Master()

kTimer._createScheduledEvent(subscriber=masterObject,eventName="eventTwoSecond",msTimePeriod=2000)

kTimer._subscribeScheduledEvent(subscriber=masterObject2,eventName="eventTwoSecond")

kTimer._createScheduledEvent(subscriber=masterObject,eventName="eventFiveSecond",msTimePeriod=5000)

time.sleep(2)

kTimer._removeSubscriberFromScheduledEvent(subscriber=masterObject2,eventName="eventTwoSecond")
kTimer._removeScheduledEvent(eventName="eventTwoSecond")