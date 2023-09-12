#pip install --upgrade google.api-client
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import googleapiclient.errors

API_KEY= "AIzaSyA6qssCuTl7gWHYSZ-VDKZoUQuG2SJ6nFQ"

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
API_KEY= "AIzaSyA6qssCuTl7gWHYSZ-VDKZoUQuG2SJ6nFQ"

#another api_key
API_KEY = 'AIzaSyDiDr_4GZ1BXYLfM77szhwxC3_9X4a47I8'
api_service_name = "youtube"
version = "v3"
#client_secrets_file = "credentials.json"
client_secrets_file = "client_secret.json"
yt = build(api_service_name,version,developerKey=API_KEY)


def get_channel_details(channel_id):
    channel_request = yt.channels().list(part="snippet,contentDetails,statistics",id=channel_id)
    channel_response = channel_request.execute()
    playlists_request = yt.playlists().list(part="snippet,contentDetails,id",channelId=channel_id,maxResults=20)
    playlists_response = playlists_request.execute()
    playlist_ids = []
    #ntoken = playlists_response['nextPageToken']
    playlist_list = playlists_response['items']
    plistresponse_list = []
    plistitem_list = []
    i = 0
    for item in playlist_list:
        #print('#'*50)
        if i== 3:
            break
        else:
            playlist_ids.append(item['id'])    
        i=i+1
    # while 'nextPageToken' in playlists_response:
    #     playlists_request = yt.playlists().list(part="snippet,contentDetails,id",pageToken = playlists_response['nextPageToken'],channelId=channel_id,maxResults=20)
    #     playlists_response = playlists_request.execute()
    #     for item in playlists_response['items']: 
    #         playlist_ids.append(item['id'])

    print("Now the play list array size is ", len(playlist_ids))
    for pid in playlist_ids:
        playlistitem_request = yt.playlistItems().list(part="id,snippet,contentDetails",playlistId=pid,maxResults=50)
        playlistitem_response = playlistitem_request.execute()
        plistitem_list.append(playlistitem_response)
        
        while 'nextPageToken' in playlistitem_response:
            playlistitem_request = yt.playlistItems().list(part="id,snippet,contentDetails",pageToken=playlistitem_response['nextPageToken'],playlistId=pid,maxResults=50)
            playlistitem_response = playlistitem_request.execute()
            plistitem_list.append(playlistitem_response)
    
    vid_list = []
    for vitems in plistitem_list:
        tmp_list = []    
        for it in vitems['items']:
            tmp_list.append(it['contentDetails']['videoId'])
        vid_list.append({it['snippet']['playlistId']:tmp_list})

    vlists=[]    
    comments_list = []
    
    for vitems in plistitem_list:
        tmp_list = []    
        for it in vitems['items']:
            video_id = it['contentDetails']['videoId']
            #for video_id in vid_list:
            #print(video_id[0])
            try:
                vidrequest = yt.videos().list(part="snippet,statistics,contentDetails",id=video_id,maxResults=50)
                vidres =vidrequest.execute()
                vidres['playlistID'] = it['snippet']['playlistId']
                vlists.append(vidres)
                commrequest = yt.commentThreads().list(part="id,snippet,replies",videoId=video_id,maxResults=50)
                commresponse = commrequest.execute()
                comments_list.append(commresponse)
                print('comment added....')
            except googleapiclient.errors.HttpError as e:
                if e.error_details[0]["reason"] == "videoNotFound":
                    print("Video not found.")


    data_dict = {'channel_details':channel_response,
                 'playlist_details':plistitem_list,
                 'videos_details':vlists,
                 'comments_details':comments_list}
    
    #print(data_dict)
    return data_dict
    
        

def get_channel_videos(channelid):
    
    
    if channelid == 'GHSS Rajamadam':
        chid = 'UCmZSDISaNWldtk6-6OnBdtQ'
    elif channelid == 'DBestech':
        chid = "UC8aiILPy0NO5wwLaYEzImbw"
    elif channelid =='CSK Team':
        chid = 'UC2J_VKrAzOEJuQvFFtj3KUw'
    #print('Now the channel id is : ', chid)
    request = yt.channels().list(part="snippet,contentDetails,statistics",id=chid)
    #TODO uncomment this if you want to use the search
    #request = yt.search().list(part="snippet,id", channelId=chid,type="channel,playlist,video", id=chid)
    playlist = yt.playlists().list(
     part="id,snippet",
     channelId=chid,
    )
    playlistres = playlist.execute()
    #print(playlistres)
    myvidlist = []
    for pid in playlistres['items']:
        playlistid = pid['id']
        viddict = {pid['id']:find_playlist_videos(playlistid)}
        myvidlist.append(viddict)
    playlistres['videos'] =  myvidlist
    response = request.execute()
    
    response['playlists'] = playlistres
    
    print("*"*60)
    #print(response)
    return response

def find_playlist_videos(playlistid):
    client_secrets_file = "credentials.json"
    yt = build(api_service_name,version,developerKey=API_KEY)
    #print(playlistid)
    request = yt.playlistItems().list(part="id,snippet",playlistId=playlistid,maxResults=50)
    response = request.execute() 

    for playlistitem in response['items']:
        #print(playlistitem)
        videoid = playlistitem['snippet']['resourceId']
        comlist = []
        commrequest = yt.commentThreads().list(part="id,snippet,replies",videoId=videoid['videoId'],maxResults=50)
        commres = commrequest.execute()
        vidrequest = yt.videos().list(part="snippet,contentDetails,statistics",id=videoid['videoId'],maxResults=50)
        vidresp = vidrequest.execute()
        vidstat = vidresp['items'][0]['statistics']
        playlistitem['totalViewCount'] = vidstat['viewCount']
        playlistitem['likeCount'] = vidstat['likeCount']
        #response['dislikeCount'] = vidstat['dislikeCount']
        playlistitem['favoriteCount'] = vidstat['favoriteCount']
        playlistitem['commentCount'] = vidstat['commentCount']
        #response['duration'] = vidstat['duration']
        
        #print("-"*60)
        #print(commres)
        response['comments'] = commres

    return response

if __name__ == '__main__':
    #get_channel_videos()
    get_channel_details()