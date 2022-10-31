import sys
import time
import msvcrt
import serial
import datetime
import csv
import os

#使用するIDE:quaternionOne.ino
#処理したいエラー
#Traceback (most recent call last):
  #File "d:\UserData\Desktop\sbw\bno055\NEW_csvWritter.py", line 67, in <module>
    #data = float(ser.readline().decode('utf-8').rstrip('\r\n'))
#ValueError: could not convert string to float: ''


if __name__ == '__main__':
    COM = "COM6"
    positionTipes = 'pTipe1'
    roadTipes = 'carpet'
    runTimes = '3'
    sensorPosition = 'front_R'
    bitRate = 115200
    valueNum = 15
    csvColumn = ['時刻(ms)','相対方位(w)','相対方位(x)','相対方位(y)','相対方位(z)','角速度(x)','角速度(y)','角速度(z)','加速度-重力加速度(x)','加速度-重力加速度(y)','加速度-重力加速度(z)','Sys','Gyro','Accel','Mag']
    csv_dir = './imu_raw_data/'
    os.makedirs(csv_dir, exist_ok=True)

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
                csvFileName = csv_dir + now.strftime(('%Y%m%d_%H%M%S')) + '_' + sensorPosition + '_' +positionTipes + '_' + roadTipes + '_' + runTimes + '.csv'
                                
                csvf = open(csvFileName, 'w',newline="")
                fwriter = csv.writer(csvf)
                fwriter.writerow(csvColumn)
                
                print('記録開始')
            
            elif status == 'f':
                
                try:
                    csvf.close()
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
                    data = float(ser.readline().decode('utf-8').rstrip('\r\n'))
                    print('data'+ str(data))
                    """
                    ここではfloat変換だけ行ってprintしている．何度か''によるエラーが発生するが，起動し続けると「data○○」とfloat変換した値が確認できる
                    dataの後ろの数が4桁のものがあるためその上4つの数字がキャリブレーションと分かる．
                    float型変換しただけではキャリブレーションの値は全て0.0～3.0で認識していることが確認できた．
                    記録開始
					data-0.08
					data0.0
					data0.03
					data0.0
					data3.0
					data1.0
					data0.0
					data2661.0
                    """
                    if float(data) > 1000:
                        judge_record = True
                    if judge_record:
                        for cnt in range(0,7):
                            print(ser.readline().decode('utf-8').rstrip('\r\n'))
                        break
                      
            
            for data in range(0,valueNum):
                #print(ser.readline().decode('utf-8').rstrip('\n'))
                if ser.readline().decode('utf-8').rstrip('\r\n') == '':
                    value.append('NUN')
                    pass
                else:
                    value.append(float(ser.readline().decode('utf-8').rstrip('\r\n')))
                count += 1
                
                """
                次にfloat型に変換できないエラーを解消するため''を認識でき次第排除した
                この時にシリアル通信をfloat型に変換するとキャリブレーションの値が
                [7.18, 0.0, 1.0, 9964.0, -0.3142, 0.5353, 507.31, -28.2, -0.97, 3.0, 3.0, 0.608, 0.4986, -3.56, -139.5]
				[-4.95, 0.0, 1.0, 9984.0, -0.321, 0.5181, -106.69, 7.7, -0.36, 3.0, 3.0, 0.6205, 0.4919, -7.88, 29.69]
				[-6.64, 0.0, 1.0, 10003.0, -0.321, 0.5195, 46.88, -10.74, -0.51, 3.0, 3.0, 0.6164, 0.4961, 66.25, 14.88]
				[-14.28, 0.0, 1.0, 10023.0, -0.2995, 0.5092, -195.5, -13.2, -2.91, 3.0, 3.0, 0.6649, 0.4763, 163.13, -182.38]
				[12.17, 0.0, 1.0, 10044.0, -0.2839, 0.5005, -321.0, 9.69, -1.08, 3.0, 3.0, 0.6829, 0.4555, -93.62, -19.69]
				[-3.08, 0.0, 1.0, 10063.0, -0.2711, 0.5156, -44.19, 10.49, -0.11, 3.0, 3.0, 0.6819, 0.4424, 36.5, 64.94]
				と非常に大きくなったり負の値になることが分かった．
				このことからシリアル通信の読み込みで''を消すと正しい値が認識出来ないと考えられる．

                """
            print(value)
    
                
            fwriter.writerow(value)
            #初期化
            value = [] 
            
    
        