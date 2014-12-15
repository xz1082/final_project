"""
bar plot functions

Author: Jianming Zhou (jz1584)

"""



import pandas as pd
import matplotlib.pyplot as plt


def plot_numPosition(df):
    """
    plots the number of open positions of the top 10 Agencies hiring the most in recent years 
    based on the given dataframe

    Argument
    ========
    df: Dataframe

    """
    df['Posting Date'] = pd.to_datetime(df['Posting Date'])   # converted to 'date' type
    postTime = df['Posting Date']
    df = df.drop_duplicates(cols=['Job ID'])                    # remove duplicate
    AgenPositions = df[['Agency', '# Of Positions']]

    #add up the total number of open position by agency
    positionCounts = AgenPositions.groupby(AgenPositions.Agency).sum()
    sorted_Counts = positionCounts.sort_index(by=['# Of Positions'], ascending=False)
    sorted_Counts.head(10).plot(kind='barh' ,fontsize=12,title='Top Agencies hiring the most \n (Date between %s and %s) '%(postTime.min(),postTime.max()))
    plt.show()
    



def plot_NumJob_byDate(df):
    """
    plots the total number of open positions by months of the most recent year ( 2013-2014) base on a given dataframe

    Argument
    ========
    df: Dataframe

    """
    df=df[['Posting Date','# Of Positions']]            #extract the necessary columns to form a new dataframes
    NewDf=df.set_index('Posting Date')
    oneYearDf=NewDf['20131001':'20141031']              #set up the time interval 
    jobCountsDf=oneYearDf.groupby([lambda x: x.year, lambda x: x.month]).sum()
    jobCountsDf.plot(title='Total Number of Open Positions by month in the most recent year \n(2013-11-01 and 2014-10-01)')
    plt.show()
    



def plot_DemandJob(df):
    """
    plots top 10 most In-Demand jobs in recent years 
    based on the given dataframe

    Argument
    ========
    df: Dataframe

    """
    df['Posting Date']=pd.to_datetime(df['Posting Date'])   #converted to 'date' type
    postTime = df['Posting Date']
    TitlePositions = df[['Civil Service Title','# Of Positions']]
    positionCounts = TitlePositions.groupby(TitlePositions['Civil Service Title']).sum()#add up the total number of open position by agency
    sorted_Counts=positionCounts.sort_index(by=['# Of Positions'],ascending=False)
    sorted_Counts.head(10).plot(kind='barh' ,fontsize=12,title='Top 10 Most In-Demand Positions \n (Date between %s and %s) '%(postTime.min(),postTime.max()))#plot top 10 position
    plt.show()




def show_salary_range(df):
    """
    takes the kwd(keyword), df(dataframe) as input and 
    plots the salary range of full-time positions

    Argument
    ========
    kwd: String
    df: Dataframe

    """
    df=df[df['Salary Frequency'] == 'Annual']                             #limited to full-time positions
    df=df[['Business Title','Salary Range From', 'Salary Range To']]      #extract the columns we needed
    salary=df.sort_index(by=['Salary Range From', 'Salary Range To'])
    salary=salary.set_index('Business Title')
    salary[['Salary Range From','Salary Range To']].plot(kind='barh',label=['hell', 'hsdf'],fontsize=11,title='Salary Range of each position based on search results')
    plt.xticks(rotation=30)
    plt.xlable='$ Full-time Salary'
    plt.ylabel='Position Title'
    plt.show()



