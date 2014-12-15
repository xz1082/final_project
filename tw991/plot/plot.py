"""
Creator: Wenxi Lei

Contributor: Sylvia Zhao, Tian Wang
"""

import matplotlib.pyplot as plt

def plot_stock(dataframe):
    price=dataframe.drop('Volume', 1)  # drop 'volume' column to make a subplot
    volume=dataframe['Volume']  
    fig=plt.figure()
    price_fig=fig.add_subplot(211)
    for i in price.columns:
        price_fig.plot(price.index, price[i], label=i, picker=1)  # make time series plot of stock prices in different columns
    plt.title('Price & Volume Trend')
    plt.ylabel('Price')
    plt.legend(loc='lower right', fontsize='x-small')
    volume_fig=fig.add_subplot(212, sharex=price_fig)  # make barplot of volume with the same index as price plot
    volume_fig.bar(volume.index, volume.values, label='Volume', picker=True)
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.legend(loc='upper right', fontsize='x-small')
    return fig, price_fig, volume_fig

