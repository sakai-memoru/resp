#coding:utf-8

#import wiringpi as wp
import time
import logging.config

## pin setting
PIN_LED = 23
PIN_SW = 24
TIME_INTERVAL = 1
COUNT_TIMER = 5 #60*3

def initializeGpio():
    wp.wiringPiSetGpio()
    wp.pinMode(PIN_LED, pi.OUTPUT)
    wp.pinMode(PIN_SW, pi.INPUT)
    pi.pullUpDnControl(PIN_SW, pi.PUD_UP)


def operateLed(pi_num, time_interval):
    logger.debug('LED ON')
    # wp.digitalWrite(pin_num, pi.HIGH)
    time.sleep(time_interval)
    logger.debug('LED OFF')
    # wp.digitalWrite(pin_num, pi.LOW)
    time.sleep(time_interval)

def onOffLed(flag):
    if flag:
        operateLed(PIN_LED, TIME_INTERVAL)

def getSwitchStatus():
    time.sleep(0.1)
    #status = wp.digitalRead(pin_num)
    status = 1
    #if state==pi.LOW:
    if status==1:
        return True
    else:
        return False

def countUp(timer):
    cnt = timer
    while cnt:
        time.sleep(1.0)
        cnt -= 1
        logger.debug(cnt)
        

def process(arg):
    logger.info('--------- process start <<')
    logger.debug('--------- arg={}'.format(arg))
    
    # initialize()
    
    while True:
        status = getSwitchStatus()
    
        if status:
            countUp(COUNT_TIMER)
            break
        
    is_led_on = True
    logger.debug(getSwitchStatus())
    while is_led_on:
        onOffLed(is_led_on)
        break
    
    logger.info('--------- process end   >>')

if __name__ == '__main__':
    logging.config.fileConfig('logging_debug.conf')
    logger = logging.getLogger(__name__)
    args = {}
    process(args)
