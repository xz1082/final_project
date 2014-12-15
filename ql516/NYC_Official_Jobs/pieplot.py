"""
pie plot

Author: Jianming Zhou (jz1584)

"""

import matplotlib.pyplot as plt

def plot_educationLevel(df):
    """
    Function takes dataframe as input,
    plot a pie of

    Argument
    ========
    DataFrame

    """

    degree=degreeDict(df)
    bach=degree['Bachelor']
    master=degree['Master']
    others=degree['High School or others non-degree']
    labels = 'At least \n a Bachelor degree', 'At least\n   A Master \n degree','Others:\nHigh school \nDiploma or \nSome experiences '
    fracs = [bach, master, others]
    plt.figure(figsize=(12,8))
    explode = (0.05, 0.05, 0.05)
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    plt.pie(fracs,explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.legend(labels,loc="lower right")
    plt.title('Minimum Degree Requirement', fontsize=20)
    plt.show()





def degreeDict(dataframe):
    """
    takes the dataframe as input,
    returns a dictionary  with key: Degree,  Values: total number of available jobs

    Argumrnt
    ========
    dataframe

    Return
    ======
    a dictionary

    """

    df=dataframe.set_index('Job ID')                        #set the Job ID be the index of dataframe
    df1=df['Minimum Qual Requirements'].dropna()            #remove null value
    position = df['# Of Positions']
    degree={}
    #initialize degree dictionary
    degree['Bachelor']=0
    degree['Master']=0
    degree['High School or others non-degree']=0

    for jobid in df1.index:
        wordList=df1[jobid].rstrip().split()
        wordList=map(lambda x: x.lower(), wordList)
        #the following calculates the number of positions that needs a certain degree at least
        #cumulate the corresponding number of positions to generate the value of a specific key( education level)
        if 'baccalaureate' in wordList or 'bachelor' in wordList:
            if 'high' not in wordList:
                numPositions1=position.get(jobid)
                degree['Bachelor']+=1*numPositions1         #at least a bachelor degree
        if "master's" in wordList:
            if 'baccalaureate' not in wordList or 'bachelor' not in wordList:
                numPositions2=position.get(jobid)
                degree['Master']+=1*numPositions2           #at least a master degree
    degree['High School or others non-degree']=position.sum()-degree['Master']-degree['Bachelor']

    return degree
