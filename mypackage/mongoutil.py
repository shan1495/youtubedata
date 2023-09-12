from pymongo import MongoClient
import mypackage.mysqlutil as sqlutil
import isodate

client = MongoClient('localhost', 27017)
db = client['youtubedata']
collection  = db["channelinfo"]

def save_data(document):
    # client = MongoClient('localhost', 27017)
    # db = client['youtubedata']
    # collection  = db["channelinfo"]
    print('Trying to insert data..')
    return collection.insert_many(document)
    


def select_channel_info(channel_id):
    query = {'channel_details.items.id':channel_id}
    docu = collection.find_one(query)
    return docu

def transform_data(responsedoc):
    channel_data = responsedoc['channel_details']['items'][0]
    stat = channel_data['statistics']
    chid = channel_data['id']
    title = channel_data['snippet']['title']
    views = stat['viewCount']
    desc = channel_data['snippet']['description']
    channelrec = (chid,title,'',views,desc,'AC')
    #sqlutil.insert_data(channelrec)
    playlist_data = responsedoc['playlist_details']
    playlist_data_array = []
    for playlist in playlist_data:
        for item in playlist['items']:
            pid = item['snippet']['playlistId']
            plistname = item['snippet']['title']
            record = (pid,chid,plistname)
            playlist_data_array.append(record)
    #sqlutil.insert_playlist(playlist_data_array)
    videos_data = responsedoc['videos_details']
    vdata_list = []
    for vido in videos_data:
        for item in vido['items']:
            vid = item['id']
            plid = vido['playlistID']
            vname = item['snippet']['title']
            dsc = item['snippet']['description']
            vpdate = item['snippet']['publishedAt']
            vpdate = vpdate[:vpdate.index('T')]
            viewcount = item['statistics']['viewCount']
            likecount = item['statistics']['likeCount']
            favcount = item['statistics']['favoriteCount']
            commcount = item['statistics']['commentCount']
            duration = item['contentDetails']['duration']
            duration = isodate.parse_duration(duration)
            durationsec = duration.total_seconds()
            print("Now the duration is ::: ",durationsec)
            caption = item['contentDetails']['caption']
            thumbnail = item['snippet']['thumbnails']['default']['url']
            record = (vid,plid,vname,dsc,vpdate,viewcount,likecount,0,favcount,commcount,durationsec,thumbnail ,caption)
            vdata_list.append(record)
    #sqlutil.insert_videos(vdata_list)
    #inserting comments
    comment_list=[]
    comments_data = responsedoc['comments_details']
    for cthread in comments_data:
        for item in cthread['items']:
            toplevelComment = item['snippet']['topLevelComment']
            vid = item['snippet']['videoId']
            commentId = toplevelComment['id']
            commentText = toplevelComment['snippet']['textDisplay']
            commentAuthor = toplevelComment['snippet']['authorDisplayName']
            commentDate = toplevelComment['snippet']['publishedAt']
            commentDate = commentDate[:commentDate.index('T')]
            record = (commentId,vid,commentText,commentAuthor,commentDate)
            comment_list.append(record)
    sqlutil.insert_comments(comment_list)


    
# if __name__ == '__main__':
#     save_data()