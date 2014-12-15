"""
scotter plot functions

Author: Jianming Zhou (jz1584)

"""
import matplotlib.pyplot as plt
import warnings




def recode_civilLevel(df):
    """
    recodes all the corresponding civil title,
    and returns a new Dataframe with two columns named "Level" and "Salary Range"

    Argument
    =======
    DataFrame

    Return
    ======
    DataFrame
    """

    df = df[df['Salary Frequency'] == 'Annual']                 #limited to full-time positions
    df = df[['Level', 'Salary Range From', 'Salary Range To']]  #extract the columns we needed
    df["Median Salary"] = (df["Salary Range From"]+df["Salary Range To"])/2
    mSalary = df[['Level', 'Median Salary']]
    mSalary['Level'] = mSalary['Level'].map({'M1': 1, 'M2': 2, 'M3': 3, 'M4': 4, 'M5': 5,
                                             'M6': 6, 'M7': 7, 'M8': 8, 'M9': 9, '00': 0, '01': 1, '02': 2, '03': 3,
                                             '04': 4, '3A': 3, '3B': 3, '4A': 4, '4B': 4})
    return mSalary
    



def plot_scatter(df):
    """
    generate a scatter plot and the associated mean line
    of median salary and job title level

    Argument
    ========
    Dataframe

    """
    warnings.filterwarnings('ignore')
    fig = plt.figure(2, figsize=(10, 8))
    mSalary = recode_civilLevel(df)
    mSalary = mSalary
    x = mSalary.Level
    y = mSalary['Median Salary']/1000                             # convert to salary in $K unit
    plt.scatter(x, y, s=200, c='lightblue', alpha=0.5)

    #plot a additional line that shows the median salary for each title level
    meanSalary_byLevel = mSalary.groupby('Level').mean()


    #above calculating the mean salary for each job level 
    meanSalary_byLevel['Median Salary'] = meanSalary_byLevel['Median Salary'].astype('int')
    #change the datatype of Salary to integer for later plotting
    joblevel = meanSalary_byLevel.index
    MeanSalary = meanSalary_byLevel['Median Salary']/1000         # convert to salary in $K unit
    ax = fig.add_subplot(111)
    for i, j in zip(joblevel, MeanSalary):
        ax.annotate('$'+str(j)+'K', xy=(i, j))
    plt.plot(joblevel, MeanSalary, c='red')
        
    plt.title('Median Salary Distribution by Civil Service Title ', fontsize=15)
    plt.ylabel("Median Salary $$$")
    plt.xlabel('Civil Service Title Level (range from 0 through 9)', fontsize=12)
    
    plt.show()

