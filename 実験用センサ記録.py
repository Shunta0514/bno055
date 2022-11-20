import sys
import time
import msvcrt
import serial
import datetime
import csv
import os
import codecs
import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt

def judge_time_data():
    
    while(True):
        
        try:
            data = float(ser.readline().decode('utf-8').rstrip('\r\n'))
            
            if data > 1000:
                
                return data
            
        except:
            pass
        
class dataFileManager:
    def __init__ (self, csv_name, csv_location):
        self.df = self.read_csv(csv_name)
        self.location = csv_location
    
    def read_csv(self, csv_name):
        with codecs.open(csv_name, "r", "Shift-JIS", "ignore") as file:
            df = pd.read_table(file, delimiter=",",header = 1)
        return df
    def pick_3column(self, head_num):
        y = []
        for num in range(head_num, head_num +3):
            y.append(self.df.iloc[:,num])
        return y[0],y[1],y[2]
    
    def pick_4column(self, head_num):
        y = []
        for num in range(head_num, head_num +4):
            y.append(self.df.iloc[:,num])
        return y[0],y[1],y[2],y[3]
    
            
    def make_picture(self):
        mpl.rc('font',family = 'BIZ UDGothic')#日本語設定
        x = self.df.iloc[:,0] #0列を指定
        """相対方位の描画"""
        for sensor_num in range(0,5):
            head_num = 1+14*sensor_num
            y1,y2,y3,y4 = self.pick_4column(head_num)
            c1,c2,c3,c4 = 'black','red','green','blue'
            l1,l2,l3,l4 = 'w','x','y','z'
            
            fig, ax = plt.subplots()
            ax.set_xlabel('経過時間 [ms]')  # x軸ラベル
            ax.set_ylabel('クォータニオン')  # y軸ラベル
            ax.set_title(str(sensor_num) +'_相対方位角') # グラフタイトル
            # ax.set_aspect('equal') # スケールを揃える
            ax.grid()            # 罫線
            #ax.set_xlim([-10, 10]) # x方向の描画範囲を指定
            #ax.set_ylim([0, 1])    # y方向の描画範囲を指定
            ax.plot(x, y1, color=c1, label=l1)
            ax.plot(x, y2, color=c2, label=l2)
            ax.plot(x, y3, color=c3, label=l3)
            ax.plot(x, y4, color=c4, label=l4)
            ax.legend(loc=0)    # 凡例
            fig.tight_layout()  # レイアウトの設定
            plt.savefig(self.location +'/センサ'+str(sensor_num) + '_' + '相対方位角') # 画像の保存
            plt.clf()
            plt.close()
            
        """角速度の描画"""
        for sensor_num in range(0,5):
            head_num = 5 + 14 * sensor_num
            y1,y2,y3 = self.pick_3column(head_num)
            c1,c2,c3 = 'red','green','blue'
            l1,l2,l3 = 'x','y','z'
            
            fig, ax = plt.subplots()
            ax.set_xlabel('経過時間 [ms]')  # x軸ラベル
            ax.set_ylabel('角速度 [rad/s]')  # y軸ラベル
            ax.set_title(str(sensor_num) + '_角速度') # グラフタイトル
            # ax.set_aspect('equal') # スケールを揃える
            ax.grid()            # 罫線
            #ax.set_xlim([-10, 10]) # x方向の描画範囲を指定
            #ax.set_ylim([0, 1])    # y方向の描画範囲を指定
            ax.plot(x, y1, color=c1, label=l1)
            ax.plot(x, y2, color=c2, label=l2)
            ax.plot(x, y3, color=c3, label=l3)
            ax.legend(loc=0)    # 凡例
            fig.tight_layout()  # レイアウトの設定
            plt.savefig(self.location +'/センサ'+str(sensor_num) + '_' + '角速度') # 画像の保存
            plt.clf()
            plt.close()
        """線形加速度の描画"""
        for sensor_num in range(0,5):
            head_num = 8 + 14 * sensor_num
            y1,y2,y3 = self.pick_3column(head_num)
            c1,c2,c3 = 'red','green','blue'
            l1,l2,l3 = 'x','y','z'
            
            fig, ax = plt.subplots()
            ax.set_xlabel('経過時間 [ms]')  # x軸ラベル
            ax.set_ylabel('線形加速度 [m/s^2]')  # y軸ラベル
            ax.set_title(str(sensor_num) + '_線形加速度') # グラフタイトル
            # ax.set_aspect('equal') # スケールを揃える
            ax.grid()            # 罫線
            #ax.set_xlim([-10, 10]) # x方向の描画範囲を指定
            #ax.set_ylim([0, 1])    # y方向の描画範囲を指定
            ax.plot(x, y1, color=c1, label=l1)
            ax.plot(x, y2, color=c2, label=l2)
            ax.plot(x, y3, color=c3, label=l3)
            ax.legend(loc=0)    # 凡例
            fig.tight_layout()  # レイアウトの設定
            plt.savefig(self.location +'/センサ'+str(sensor_num) + '_' + '線形加速度') # 画像の保存
            plt.clf()
            plt.close()
    
def calibration_mode(DATA_LENGTH):
    calibration_value = []
    system_tag = '\033[31m'+'system'+'\033[0m'
    gyro_tag = '\033[31m'+'gyro'+'\033[0m'
    accel_tag = '\033[31m'+'accel'+'\033[0m'
    magnet_tag = '\033[31m'+'mag'+'\033[0m'
    try: 
        time_data = judge_time_data()
        #print(time_data)
        calibration_value.append(time_data)
        
        for num in range(DATA_LENGTH-1):
            calibration_value.append(float(ser.readline().decode('utf-8').rstrip('\r\n')))
        #print(calibration_value)
        if calibration_value[11] ==3.0 and calibration_value[25] == 3.0 and calibration_value[39] == 3.0 and calibration_value[53] == 3.0 and calibration_value[67]  == 3.0:
            system_tag = '\033[32m'+'system'+'\033[0m'
        if calibration_value[12] ==3.0 and calibration_value[26] == 3.0 and calibration_value[40] == 3.0 and calibration_value[54] == 3.0 and calibration_value[68]  == 3.0:
            gyro_tag = '\033[32m'+'gyro'+'\033[0m'    
        if calibration_value[13] ==3.0 and calibration_value[27] == 3.0 and calibration_value[41] == 3.0 and calibration_value[55] == 3.0 and calibration_value[69]  == 3.0:
            accel_tag = '\033[32m'+'accel'+'\033[0m'
        if calibration_value[14] ==3.0 and calibration_value[28] == 3.0 and calibration_value[42] == 3.0 and calibration_value[56] == 3.0 and calibration_value[70]  == 3.0:
            magnet_tag = '\033[32m'+'mag'+'\033[0m'
                
        print('['+ system_tag +','+ gyro_tag +',' + accel_tag +',' + magnet_tag +']') 
        calibration_value = []
    except:
        print('読み込みエラー')

    


if __name__ == '__main__':
    
    COM = "COM6"
    bitRate = 921600
    valueNum = 71 #1+14*5
    csvColumn1 = ['','sensor0','','','','','','','','','','','','','','sensor1','','','','','','','','','','','','','','sensor2','','','','','','','','','','','','','','sensor3','','','','','','','','','','','','','','sensor4']
    csvColumn2 = ['相対方位(w)','相対方位(x)','相対方位(y)','相対方位(z)','角速度(x)','角速度(y)','角速度(z)','加速度-重力加速度(x)','加速度-重力加速度(y)','加速度-重力加速度(z)','Sys','Gyro','Accel','Mag']
    csvColumn3 = ['時刻(ms)']
    for sensor_num in range(5):
        csvColumn3 += csvColumn2
    csv_dir = './imu_raw_data/'
    os.makedirs(csv_dir, exist_ok=True)

    status = 'f'
    data = 0
    value =[]
    DATA_LENGTH = valueNum
    count = 0
    ser = serial.Serial(COM,bitRate) #ポートの情報を記入
    
    while(1):
        #キーボード押下時の処理
        if msvcrt.kbhit():
            
            status = msvcrt.getch()
            
            if (status.decode() == 's') or (status.decode() == 'f'):
                status = status.decode()
            
            if status == 's':
                #ファイル名作成
                roadtypes =input('走行路面')
                walktracks = input('直進or蛇行')
                runspeed = input('歩行速度')
                runTimes =input('走行回数')
                now = datetime.datetime.now()
                if(roadtypes == 'キャリブレーション'):
                    pass
                else:
                    #ファイル作成
                    os.makedirs(csv_dir + now.strftime('%Y%m%d_%H%M%S'),exist_ok = True)
                    csvFileName = csv_dir + '/'+ now.strftime(('%Y%m%d_%H%M%S')) +'/' +roadtypes + '_' +walktracks + '_' + runspeed + '_' + runTimes + '.csv'
                    #ファイル展開      
                    csvf = open(csvFileName, 'w',newline="")
                    fwriter = csv.writer(csvf)
                    fwriter.writerow(csvColumn1)
                    fwriter.writerow(csvColumn3)                
                    print('記録中：', csvFileName)
                    
                    #31行分を無視
                    for initial_num in range(0,29):
                        try:
                            
                            time_data = judge_time_data()
                            #print(time_data)
                            
                        except:
                            print('読み込みエラー')
            
            elif status == 'f':
                if roadtypes == 'キャリブレーション':
                    print('キャリブレーション画面を閉じました')
                    pass
                else:
                    try:
                        csvf.close()
                        print('記録終了')
                        '''図を作成するコード'''
                        df_manager = dataFileManager(csvFileName, csv_dir + '/'+ now.strftime(('%Y%m%d_%H%M%S')) +'/')
                        df_manager.make_picture()
                    except:
                        pass
        
        if status == 'f':
            pass
        
        elif status == 's':
            if roadtypes == 'キャリブレーション':
                calibration_mode(DATA_LENGTH)
                
            else:
                try:
                    
                    time_data = judge_time_data()
                    #print(time_data)
                    value.append(time_data)
                    
                    for data_num in range(DATA_LENGTH-1):
                        value.append(float(ser.readline().decode('utf-8').rstrip('\r\n')))
                
                except:
                    print('読み込みエラー')
                
                print(value)
                fwriter.writerow(value)
                value = []