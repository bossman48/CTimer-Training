from ZTimer import Ztimer
from Master import *
import time 

zTimer = Ztimer()

masterObject = Master()

masterObject2 = Master()

zTimer._createScheduledEvent(subscriber=masterObject,eventName="eventTwoSecond",msTimePeriod=2000)

zTimer._subscribeScheduledEvent(subscriber=masterObject2,eventName="eventTwoSecond")

zTimer._createScheduledEvent(subscriber=masterObject,eventName="eventFiveSecond",msTimePeriod=5000)

time.sleep(2)

zTimer._removeSubscriberFromScheduledEvent(subscriber=masterObject2,eventName="eventTwoSecond")
zTimer._removeScheduledEvent(eventName="eventTwoSecond")