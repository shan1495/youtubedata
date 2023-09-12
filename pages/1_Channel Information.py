#pip install --upgrade google.api-client
import streamlit as st
import pandas as pd
import numpy as np
import requests
from googleapiclient.discovery import build
import mypackage.utilities as util
import mypackage.mongoutil as mongoutil
# def process_my_response(response):
    
#     for item in response['items']:
        
#         playlist = response['playlists']['items']
        
#         pid = playlist[0]['id']
#         print("The Playlist id = ", pid)
#         videos = response['playlists']['videos']
#         vdolist = []
        
#         print("The length of the videos === ", len(videos))
#         print('-'*20)
#         video_list = []
#         for vid in videos:

#             for vvid in vid:
                
#                 obj = vid[vvid]
#                 #print(obj)
#                 for vitem in obj['items']:
#                     print(vitem)
#                     video = vitem['snippet']['resourceId']
#                     #comment = vitem['snippet']['topLevelComment']['snippet']['textDisplay']
#                     #replycount = item['snippet']['totalReplyCount']

#                     video_dict = {video['videoId']:{
#                     "Video_Id":video['videoId'],
#                     "Video_Name":vitem['snippet']['title'],
#                     "Video_Description":vitem['snippet']['description'],
#                     "tags":"",
#                     "PublishedAt":vitem['snippet']['publishedAt'],
#                     "View_Count":vitem['totalViewCount'],
#                     "Like_Count":vitem['likeCount'],
#                     "Dislike_Count":"0",
#                     "Favorite_Count":vitem['favoriteCount'],
#                     "Comment_Count":vitem['commentCount'],
#                     "Duration":""
#                     }}
#                     video_list.append(video_dict)
            
#         mongo_doc = {item['snippet']['title']:{
#             "Channel_Id":item['id'],
#             "Subscription_Count":item['statistics']['subscriberCount'],
#             "Channel_Views":item['statistics']['viewCount'],
#             "Channel_Description":item['snippet']['description'],
#             "Playlist_Id":pid
#         },}
#         #print(video_list)
#         i = 0
#         while i< len(video_list):
#             vido_id_list = list(video_list[i].keys())
#             print(vido_id_list)
#             mongo_doc[item['snippet']['title']][vido_id_list[0]] = video_list[i][vido_id_list[0]]
#             #mongo_doc[vido_id_list[0]] = 
#             i= i+1
#         print(">>"*50)
#         return mongo_doc
st.set_page_config(layout='wide',page_title='Get Channel Information')

channellist = [ 'DBestech', 'CSK Team', 'GHSS Rajamadam']
with st.form(key='channel-form'):
    #choice = st.selectbox(label='Select the Channel for to extract data',options=channellist,placeholder="Select the Channel Name")
    choice = st.text_input(label='Enter the channel ID')
    btn = st.form_submit_button(label='View and Save data')
    if btn:
         #response = util.get_channel_videos(choice)
         response = util.get_channel_details(choice)
         #mon_d = process_my_response(response)
         st.write(response)
         info = mongoutil.save_data([response])
         st.info("Document Inserted successfully!")
              