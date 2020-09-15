import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def check_log_returns(data_path):
    data = pd.read_csv(data_path)
    data['log_returns'] = np.log(data['Close'] / data['Close'].shift(1))
    data_log_returns = data['log_returns'].dropna()
    # plt.subplot(121)
    # plt.hist(data_log_returns, bins=100)
    # plt.xlabel("return")
    # plt.ylabel("days")
    # plt.title("log_return")
    # plt.subplot(122)
    # stats.probplot(data_log_returns, dist="norm", plot=plt)
    # plt.show()
    u = data_log_returns.mean()  # 计算均值
    std = data_log_returns.std()  # 计算标准差
    print(stats.kstest(data_log_returns, 'norm', (u, std)))


check_log_returns('IBM.csv')
