import argparse
import math
import numpy as np
import shutil
import pygame
import sounddevice as sd
from datetime import datetime

startTime = datetime.now()

def main():
    def IntOrStr(text):
        try:
            return int(text)
        except ValueError:
            return text
        
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-l', '--list-devices', action='store_true',
                    help='\nlist audio devices')
    parser.add_argument('-d', '--device', type=IntOrStr,
                    help='input device (numeric ID or substring)')
    
    args = parser.parse_args()
    samplerate = sd.query_devices(args.device, 'input')['default_samplerate']
    
    print (sd.query_devices(args.device, 'input')['max_input_channels'])

    def callback(indata, frames, time, status):
        print (type(indata), type(frames), type(time), type(status))
    

    inSpream = sd.InputStream(device = args.device, channels = 1, callback = callback, blocksize = int(samplerate * args.block_duration / 1000), samplerate = samplerate)

    
if __name__ == "__main__":
	main()
    print(datetime.now()-startTime)
