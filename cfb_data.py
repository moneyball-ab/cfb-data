#import dependencies
import sys #This is used to set the sys path for importing the module
#sys.path.append('./college_football_data_class') #This is where the module resides
#from __init__ import Schedule #This is the module with classes related to cfb data
import college_football_data_class as cfb_data #This is the module with classes related to cfb data

import warnings
warnings.filterwarnings("ignore")

import pandas as pd

from datetime import datetime as dt

import smtplib # used to send mail (which can be used for ATT service to send
               # text messages as well using 10digitnumber@txt.att.net as the
               # email address)

#import more email functions
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders




time_now = dt.now()

team_list = ['Wake Forest','Florida State','Northwestern']

body_str = """
"""

for team_item in team_list:
    #Run process on Wednesday morning only
    #if ((time_now.weekday() == 2) & (time_now.hour <= 11)):
    #    print("run this process on Wed AM only")

    #Set the properties to be used
    #team1 = "Wake Forest"
    team1 = team_item
    game_yr = 2019
    num_past_years = 5
    #game_wk = 15 # optional param for get_game_wk_info(), default is 1

    now_time = dt.now()

    #initialize an object with class Schedule
    schedule = cfb_data.Schedule(team1, game_yr, num_past_years)# game_wk is optional param for get_game_wk_info(), default is 1

    # populate the properties of the object
    schedule.find_last_completed_game_info() # filter information from schedule for last completed game info
    schedule.find_next_game_info()
    schedule.find_series_range_record(schedule.nextgameinfoframe.opponent)
    schedule.summarize_opponent_record(schedule.nextgameinfoframe.opponent, schedule.seriesrangerecordsummaryframe.year)
    schedule.summarize_team_record(schedule.seriesrangerecordsummaryframe.year)
    schedule.combine_series_and_record_info()

    print('\n' + team_item + ': NEXT GAME INFO FRAME\n')
    body_str = body_str + '</br></br><b>' + '\n' + team_item + ': NEXT GAME INFO FRAME\n' +'\n' + '</b>'

    df_nextgame = pd.DataFrame(schedule.nextgameinfoframe[['opponent','start_time','venue']]).transpose()
    col_name = 'rec_last_' + str(num_past_years) + '_yrs'
    df_nextgame[col_name] = schedule.seriesrangerecordsummary
    print(df_nextgame)
    body_str = body_str + df_nextgame.to_html(index=False, index_names=False) + '\n'

    print('\n' + team_item + ': SERIES AND RECORD FRAME, LAST ' + str(num_past_years) + ' YEARS:\n')
    body_str = body_str + '</br></br><b>'  + '\n' + team_item + ': SERIES AND RECORD FRAME, LAST ' + str(num_past_years) + ' YEARS:\n' + '\n' + '</b></br></br>'
    
    df_seriesinfo = schedule.seriesandrecordframe[['year','week','venue','winner','team_rec','opp_rec']]
    print(df_seriesinfo)
    body_str = body_str + df_seriesinfo.to_html(index=False, index_names=False) + '\n' + '</br></br>'

    
print('\n\n\n --- --- --- \n\n\n')
