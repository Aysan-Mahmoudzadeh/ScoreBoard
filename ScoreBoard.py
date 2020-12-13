# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 12:14:39 2020

@author: AysanMahmoudzadeh
"""

import os.path
import pandas as pd
import numpy as np

    
def _show():
    if(os.path.isfile('ScoreBoard.csv') == False): 
        f= open("ScoreBoard.csv","a")
        player = ''
        score = ''
        df_data = list(zip(*[player, score]))
        df = pd.DataFrame(df_data, columns=['Player', 'Score'])
        df.to_csv('ScoreBoard.csv', mode='a', index=False)
    else:
        print('Please Open the ScoreBoard.txt\n')
    
#_show()
        
def _add(player, score_new):
    name = player
    score = score_new
    
    if(os.path.isfile('ScoreBoard.csv') == False): 
        f= open("ScoreBoard.csv","a")
        
        df = pd.DataFrame({"Player":[name], "Score":[score]})
        df.to_csv('ScoreBoard.csv', mode='a', index=False)
    else:
        df_sb = pd.read_csv('ScoreBoard.csv')
        df1 = pd.DataFrame({"Player":df_sb['Player'], 
                         "Score":df_sb['Score']})
        if player in df1.values : 
            ind = df1.isin([name])
            select_indices = list(np.where(ind == True)[0])
            df = df1.drop(select_indices)
            df2 = pd.DataFrame({"Player":[name], "Score":[score]})   
            df = df.append(df2)
            df = df.sort_values(by=['Score'], ascending=False)
            df.to_csv('ScoreBoard.csv', mode='w', index=False)
        else : 
            df2 = pd.DataFrame({"Player":[name], "Score":[score]})   
            df = df1.append(df2)
            df = df.sort_values(by=['Score'], ascending=False)
            df.to_csv('ScoreBoard.csv', mode='w', index=False)    
    
#_add()
 
def _delete(player):
    df_sb = pd.read_csv('ScoreBoard.csv')
    df1 = pd.DataFrame({"Player":df_sb['Player'], "Score":df_sb['Score']})
    if player in df1.values : 
        ind = df1.isin([player])
        select_indices = list(np.where(ind == True)[0])
        df = df1.drop(select_indices)
        df.to_csv('ScoreBoard.csv', mode='w', index=False)  
    else : 
        print("\nThis Player does not exists in ScoreBoard") 
    

def main():
    value = input('Please Enter Number 1: Show Players and Scores, 2: Add Player, 3: Delete Player\n')
    value = int(value)
    if(value == 1):
        _show()
    elif(value == 2):
        player = input('Please Enter Name of Player\n')
        score = input('Please Enter Score of Player\n')
        player = str(player)
        score = int(score)
        _add(player, score)
    elif(value == 3):
        player = input('Please Enter Name of Player\n')
        player = str(player)
        _delete(player)
    else:
        print('The Number is Out of Range\n')
    
main()