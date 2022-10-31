

#バイナリファイルとして読み込んでないから別の情報？
#with open('D:\UserData\Desktop\sbw\bno055\imu_binary_data\20221030_234617_Binary.dat','r',encoding='') as f:
#    data = f.read()
#    print(type(data))
#    print(data)
#f.close()

#print('\n'+'next'+'\n')

#この下にBinaryファイルを入力
from base64 import decode


while(1):
    filename = input('fileName')
    with open('./imu_binary_data/'+ filename + '.dat','rb') as fb:
        data = fb.read()
        print(type(data))
        print(data)
    fb.close()
    
    with open('./imu_binary_data/'+ filename + '.dat','r',encoding='UTF-8') as f:
        List = f.readlines()
        FloatList = [float(n) for n in List]
        print(FloatList)
    f.close()
    
    