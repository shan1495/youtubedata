import mysql.connector

def create_connection():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",database='research'
    )

def insert_data(data):
    mydb = create_connection()
    mycursor = mydb.cursor()
    insert_query = '''insert into channel values (%s,%s,%s,%s,%s,%s)'''
    mycursor.execute(insert_query,data)   
    mydb.commit()
    mycursor.close()

def insert_playlist(data):
    mydb = create_connection()
    mycursor = mydb.cursor()
    playlist_query = '''insert into playlist values(%s,%s,%s)'''
    mycursor.executemany(playlist_query,data)
    mydb.commit()
    mycursor.close()
    mydb.close()

def insert_videos(data_list):
    mydb = create_connection()
    mycursor = mydb.cursor()
    video_query = '''insert into video_info values(%s,%s,%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s)'''
    mycursor.executemany(video_query,data_list)
    mydb.commit()
    mycursor.close()
    mydb.close()

def insert_comments(data):
    mydb = create_connection()
    mycursor = mydb.cursor()
    insert_query = '''insert into comments_info values (%s,%s,%s,%s,%s)'''
    mycursor.executemany(insert_query,data)   
    mydb.commit()
    mycursor.close()

def select_channel(channelid):
    mydb = create_connection()
    mycursor = mydb.cursor()
    mycursor.execute('''select * from channel''')
