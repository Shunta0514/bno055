import sys
import time
import msvcrt
import serial
import datetime
import csv
import os

if __name__ == '__main__':
    COM = "COM6"
    bitRate = 115200
    valueNum = 15
    binary_dir = './imu_binary_data/'
    os.makedirs(binary_dir, exist_ok=True)

    status = 'f'
    start_record = False
    data = 0
    value =[]
    count = 0
    ser = serial.Serial(COM,bitRate) #ポートの情報を記入

    
    while(1):
        #キーボード押下時の処理
        if msvcrt.kbhit():
            
            status = msvcrt.getch()
            status = status.decode()
            
            if status == 's':
                
                start_record = True
                
                now = datetime.datetime.now()
                binaryFileName = binary_dir + now.strftime(('%Y%m%d_%H%M%S')) + '_' + 'Binary' + '.dat'
                                
                binaryf = open(binaryFileName, 'wb')
                
                print('記録開始')
            
            elif status == 'f':
                
                try:
                    binaryf.close()
                    print('記録終了')
                except:
                    pass
        
        if status == 'f':
            pass
        
        elif status == 's':
            
            if start_record:
                
                start_record = False
                judge_record = False
                """
                while(True):
                    data = float(ser.readline().decode('utf-8').rstrip('\n'))
                    print('data'+ str(data))
                    if float(data) > 1000:
                        judge_record = True
                    if judge_record:
                        for cnt in range(0,4):
                            ser.readline().decode('utf-8').rstrip('\n')
                        break
                        """
                      
            
            
    
                
            binaryf.write(ser.readline())
            #初期化
            value = [] 
            
    
        