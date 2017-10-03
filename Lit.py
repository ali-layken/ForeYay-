import argparse
import numpy as np
import sounddevice as sd
import serial
import time

#Connect to Arduino
ser = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(3)

def main():
    #Parser Function
    def IntOrStr(text):
        try:
            return int(text)
        except ValueError:
            return text

    #Getting Command Line Arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-l', '--list-devices', action='store_true',
                        help='\nlist audio devices')
    parser.add_argument('-d', '--device', type=IntOrStr,
                        help='input device (numeric ID or substring)')
    parser.add_argument('-b', '--block-size', type=float,
                        metavar='Latency', default=50,
                        help='block size (default %(default)s milliseconds)')
    args = parser.parse_args()

    #Fast Pre-Formatted Data for Arduino Pipe
    outByte = {0: 'o'.encode(),
               1: 'r'.encode(),
               2: 'g'.encode(),
               3: 'y'.encode(),
               4: 'b'.encode(),
               5: 'p'.encode(),
               6: 't'.encode(),
               7: 'w'.encode(),
               }

    #List devices if -l argument
    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)
    samplerate = sd.query_devices(args.device, 'input')['default_samplerate']


    #Callback function of the audio stream
    def callback(indata, frames, time, status):
        if status:
            print(status)
        if any(indata):
            colorAdd = [0,0,0]
            magnitude = np.abs(np.fft.rfft(indata[:, 0], n= 44100))
            for index, i in enumerate(magnitude[20:2000], start = 0):
                index += 20
                if index < 250 and i > 100:
                    colorAdd[0] = 1
                if index > 250 and index < 750 and i > 50:
                    colorAdd[1] = 2
                if index > 750 and i > 20:
                    colorAdd[2] = 4

            ser.write(outByte[sum(colorAdd)])
        else:
            print("No Input")

    print('connection established')

    #Audio Stream Function
    with sd.InputStream(device= args.device, channels= 1, callback= callback, blocksize= int(samplerate * args.block_size/ 1000), samplerate= samplerate):
        while True:
            response = input()
            if response in ('', 'q', 'Q'):
                break

if __name__ == "__main__":
	main()
