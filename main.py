from CTimer import Ctimer
from Master import *
import time 

cTimer = Ctimer()

masterObject = Master()

masterObject2 = Master()

cTimer._createScheduledEvent(subscriber=masterObject,eventName="eventTwoSecond",msTimePeriod=2000)

cTimer._subscribeScheduledEvent(subscriber=masterObject2,eventName="eventTwoSecond")

cTimer._createScheduledEvent(subscriber=masterObject,eventName="eventFiveSecond",msTimePeriod=5000)

time.sleep(2)

cTimer._removeSubscriberFromScheduledEvent(subscriber=masterObject2,eventName="eventTwoSecond")
cTimer._removeScheduledEvent(eventName="eventTwoSecond")