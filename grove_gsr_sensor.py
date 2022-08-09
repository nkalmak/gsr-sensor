import math
import sys
import time
import datetime
from grove.adc import ADC
import csv
 
 
class GroveGSRSensor:
 
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()
 
    @property
    def GSR(self):
        value = self.adc.read(self.channel)
        return value
 
Grove = GroveGSRSensor
 
def write_csv(data):
    with open('../../data/input_data.csv', 'a') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(data)

def main():
    if len(sys.argv) < 2:
        print('Usage: {} adc_channel'.format(sys.argv[0]))
        sys.exit(1)
 
    sensor = GroveGSRSensor(int(sys.argv[1]))
 
    print('Detecting...')
    while True:
        write_csv((datetime.datetime.now(),sensor.GSR))
        print('GSR value: {0}'.format(sensor.GSR))
        time.sleep(1)
 
if __name__ == '__main__':
    main()
