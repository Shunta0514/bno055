

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
        sData = data.decode('utf-8').rsplit('\r\n')
        print(sData)
        fData = []
        """
        for list in range(16, len(sData)):
            fData.append(float(sData[list]))
            print(fData)
        """
    fb.close()
    
    
    