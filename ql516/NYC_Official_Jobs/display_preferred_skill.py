"""
function used to get the most demanded skills

Author: Ke Ye (ky822)

"""

import pandas as pd
from input_filter import filter_the_job
from Dataloading import Clean_df


def display_preferred_skill(df):
    """
    Display preferred skills of a job dataframe. The skills are listed from the most preferred to the least preferred.
    Return a list of preferred skills.

    Argument
    ========
    df: a job dataframe

    Return
    ======
    a list
    """
    #Obtain a list of high frequent skills used to filter the preferred skills.
    with open('NYC_Official_Jobs/skill_set', 'r') as f:
        Skill_List = [line.rstrip('\n') for line in f]
    PreferredSkill_List  = []

    for jobID in df['Job ID']:
    #Get the preferred skills description for each job of the dataframe and turn them into strings.
        skill = df[df['Job ID']==jobID]['Preferred Skills']
        skill = str(skill.tolist())
        #Obtain a preferred skill list of a certain job.
        ContainedSkill = []
        ContainedSkill_List = []
        for word in Skill_List:
            if (word in skill)==1:
                ContainedSkill = [word]
                ContainedSkill_List.extend(ContainedSkill)
        PreferredSkill_List.extend(set(ContainedSkill))
    #Obtain a whole preferred skill list of the given job dataframe and sort it from the toppest.
    PreferredSkill_List = sorted(set(PreferredSkill_List), reverse=True)
    
    if len(PreferredSkill_List)==0:
        print "Sorry, there isn't any popular demanded skill can be found!"
    else:
        #Obtain a whole preferred skill list of the given job dataframe and sort it from the toppest.
        PreferredSkill_List = sorted(set(PreferredSkill_List), reverse=True)
        return PreferredSkill_List[:15]
