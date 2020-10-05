import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from decimal import Decimal
import pandas as pd 
import numpy as np
%matplotlib inline

def plot_ma(data_path):
    IBM = pd.read_csv(data_path)
    IBM['MA35'] = IBM['Close'].rolling(window=35).mean()
    IBM["MA100"] = IBM['Close'].rolling(window=100).mean()
    IBM['Trade_date'] = pd.to_datetime(IBM['Date'],format="%Y-%m-%d")
    IBM.plot(x='Trade_date',y=['Close','MA35','MA100'],figsize=(20,10))


def check_log_returns(data_path):
    data = pd.read_csv(data_path)
    data['log_returns'] = np.log(data['Close'] / data['Close'].shift(1))
    data_log_returns = data['log_returns'].dropna()
    plt.subplot(121)
    plt.hist(data_log_returns, bins=100)
    plt.xlabel("return")
    plt.ylabel("days")
    plt.title("log_return")
    plt.subplot(122)
    stats.probplot(data_log_returns, dist="norm", plot=plt)
    plt.show()
    u = data_log_returns.mean()  # 计算均值
    std = data_log_returns.std()  # 计算标准差
    print(stats.kstest(data_log_returns, 'norm', (u, std)))


def stats_value(path):
    data = pd.read_csv(path)
    df = data[['Date', 'Close']]
    df.index = pd.to_datetime(df['Date'])
    df = df.drop('Date', axis=1)
    df_mean = Decimal(df['Close'].mean()).quantize(Decimal("0.0001"), rounding="ROUND_HALF_UP")
    df_variance = Decimal(df['Close'].std()).quantize(Decimal("0.0001"), rounding="ROUND_HALF_UP")
    df_skewness = Decimal(stats.skew(df['Close'])).quantize(Decimal("0.0001"), rounding="ROUND_HALF_UP")
    df_kurtosis = Decimal(stats.kurtosis(df['Close'])).quantize(Decimal("0.0001"), rounding="ROUND_HALF_UP")

    print('Sample mean:', df_mean)
    print('Sample variance:', df_variance)
    print('Sample Adjusted skewness:', df_skewness)
    print('Sample Adjusted excess kurtosis:', df_kurtosis)


plot_ma('IBM.csv')
check_log_returns('IBM.csv')
stats_value('IBM.csv')
