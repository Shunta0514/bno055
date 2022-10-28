import msvcrt
import sys
import time
import serial
import datetime
import csv
import os

if __name__ == '__main__':
    
    a = ['a', 'b']
    COM = "COM6"
    positionTipes = 'pTipe1'
    roadTipes = 'carpet'
    runTimes = '1'
    eightsensorPosition = 'frontR'
    ninesensorPosition = 'backL'
    bitRate = 921600
    valueNum = 15
    csvColumn = ['時刻(ms)','相対方位(w)','相対方位(x)','相対方位(y)','相対方位(z)','角速度(x)','角速度(y)','角速度(z)','加速度-重力加速度(x)','加速度-重力加速度(y)','加速度-重力加速度(z)','Sys','Gyro','Accel','Mag']
    csv_dir = './imu_raw_data/'
    os.makedirs(csv_dir, exist_ok=True)
    
    ser = serial.Serial(COM,bitRate) #ポートの情報を記入
    
    status = 'f'
    start_record = False
    data = 0
    eightvalue =[]
    ninevalue = []
    count = 0
    
    while(True):
        
        #キーボード押下時の処理
        if msvcrt.kbhit():
            
            status = msvcrt.getch()
            status = status.decode()
            
            if status == 's':
                
                start_record = True
                
                now = datetime.datetime.now()
                eightcsvFileName = csv_dir + now.strftime(('%Y%m%d_%H%M%S')) + '_' + eightsensorPosition + '_' +positionTipes + '_' + roadTipes + '_' + runTimes + '.csv'
                ninecsvFileName = csv_dir + now.strftime(('%Y%m%d_%H%M%S')) + '_' + ninesensorPosition + '_' + positionTipes + '_' + roadTipes + '_' + runTimes  + '.csv'
                
                Eif = open(eightcsvFileName, 'w',newline="")
                Eifwriter = csv.writer(Eif)
                Eifwriter.writerow(csvColumn)
                        
                Nif = open(ninecsvFileName, 'w',newline="")
                Nifwriter = csv.writer(Nif)
                Nifwriter.writerow(csvColumn)
                
                print('記録開始')
            
            elif status == 'f':
                
                try:
                    Eif.close()
                    Nif.close()
                    print('記録終了')
                except:
                    pass
                

        if status == 'f':
            pass
        
        elif status == 's':
            
            if start_record:
                
                start_record = False
                judge_record = False
                
                while(True):
                    
                    data  = ser.readline().decode('utf-8').rstrip('\r\n')
                    count += 1
                    
                    if count%30 ==  1:
                        break
                            
            for data in range(0,valueNum):
                print(ser.readline().decode('utf-8').rstrip('\r\n'))
                if ser.readline().decode('utf-8').rstrip('\n') == '':
                    pass
                else:
                    eightvalue.append(float(ser.readline().decode('utf-8').rstrip('\r\n')))
                count += 1
            
            for data in range(0,valueNum):
                if ser.readline().decode('utf-8').rstrip('\n') == '':
                    pass
                else:
                    ninevalue.append(float(ser.readline().decode('utf-8').rstrip('\r\n')))
                count += 1
            
            Eifwriter.writerow(eightvalue)
            Nifwriter.writerow(ninevalue)
            
            eightvalue =[]
            ninevalue = []