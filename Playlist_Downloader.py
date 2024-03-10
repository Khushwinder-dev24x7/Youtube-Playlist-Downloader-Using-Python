# First install python on your system and Run this below command
# python -m pip install git+https://github.com/nficano/pytube 

from pytube import Playlist

path= "D:\Youtube Downloaded"  #here you can add your download folder


link = input("Enter YouTube Playlist URL: ")

yt_playlist = Playlist(link)

ind = 1
for video in yt_playlist.videos:

    st = "S_No. "  

    pre = st+str(ind)+"  "
        
    video.streams.get_highest_resolution().download(path,"", pre )
    
    print("Video Downloaded: ", video.title)
   
    ind +=1
    
print("\nAll videos are downloaded.")
