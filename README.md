# youtubedata
This is a simple project that uses Youtube Data APIs to get the youtube data and store it MongoDB database (datalake). And from mongodb fetch the unstructured date and transform it to a structured data and store it in RDBMS (MySQL in this project). Once this process is one, using streamlit we can view the data in the required way. 

SQL Query Output need to displayed as table in Streamlit Application:
1. What are the names of all the videos and their corresponding channels?
2. Which channels have the most number of videos, and how many videos do  they have?
3. What are the top 10 most viewed videos and their respective channels?
4. How many comments were made on each video, and what are their corresponding video names?
5. Which videos have the highest number of likes, and what are their corresponding channel names?
6. What is the total number of likes and dislikes for each video, and what are their corresponding video names?
7. What is the total number of views for each channel, and what are their corresponding channel names?
8. What are the names of all the channels that have published videos in the year  2022?
9. What is the average duration of all videos in each channel, and what are their corresponding channel names?
10. Which videos have the highest number of comments, and what are their corresponding channel names?

Results: 
This project aims to develop a user-friendly Streamlit application that utilizes the Google API to extract information on a YouTube channel, stores it in a MongoDB database, migrates it to a SQL data warehouse, and enables users to search for channel details and join tables to view data in the Streamlit app.


Tech spec:
Python 3
Streamlit
MongoDB
MySQL
VS (IDE)

Steps to run:
Clone the project
navigate to the project folder
execute 'streamlit run Home.py'
Prerequieste: Before executing this, get the youTube API client credentials and API code. Place the file in that project folder. 

linkedin post: https://www.linkedin.com/posts/shanmugam-palani-5a103418_youtube-data-harvesting-with-streamlit-demo-activity-7118117232479547393-FoOj?utm_source=share&utm_medium=member_desktop
Youtube Demo:
https://lnkd.in/dPBWNrF4
https://lnkd.in/dRnTypS6

