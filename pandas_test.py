import pandas as pd
from matplotlib import pyplot as plt
import codecs

if __name__ == '__main__':
    f_name = './imu_raw_data//20221105_181951/配置１_カーペット_１.csv'
    with codecs.open(f_name, "r", "Shift-JIS", "ignore") as file:
        df = pd.read_table(file, delimiter=",",header = 1)
    x = df.iloc[:,0]
    y = df.iloc[:,1]
    plt.plot(x,y)
    plt.show()