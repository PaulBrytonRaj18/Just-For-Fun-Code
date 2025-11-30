import os
import sys
import json
import dotenv
from googleapiclient.discovery import build
from flask import Flask, request, jsonify, render_template 


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("Youtube_Video_Downloder.html")

# Load environment variables from .env file
dotenv.load_dotenv(dotenv_path=".env", override=True)

max_results = 10

def search_youtube_song(song_name) -> tuple[str, str]:
    """
    Search for a song on YouTube and return the URL of the best match
    
    Args:
        song_name (str): Name of the song to search for
        
    Returns:
        str: Full YouTube URL of the first matching video
    """
    try:
        # Build the YouTube API client
        youtube = build('youtube', 'v3', developerKey=os.getenv("USE_YOUR_OWN_API_KEY_DA_NON_SENSE"))
        
        # Search for the song
        search_response = youtube.search().list(
            q=song_name,
            part='id,snippet',
            maxResults=max_results,  # Get only the top result
            type='video'   # Search only for videos
        ).execute()
        
        # Extract the video ID from the search results
        for i in range(max_results):
            video_id = search_response['items'][i]['id']['videoId']
            video_title = search_response['items'][i]['snippet']['title']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            print(f"{i+1}. {video_title} - {video_url}")
            print("Which one is correct? Enter the number or '0' to skip:")
            choice = int(input().strip())
            if choice == 0:
                continue
            elif 1 <= choice <= max_results:
                selected_video = search_response['items'][choice - 1]
                video_id = selected_video['id']['videoId']
                video_title = selected_video['snippet']['title']
                video_url = f"https://www.youtube.com/watch?v={video_id}"
        
            
            return video_url, video_title
        else:
            return None, None
            
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


def download_video(video_url) -> None:
    """
    Download a YouTube video using yt-dlp
    
    Args:
        video_url (str): Full YouTube URL of the video to download
    """
    
    
    try:
        # Construct the yt-dlp command
        command = f'cd "{os.getenv("YOUR_VIDEO_DOWNLOAD_DIRECTORY")}" && yt-dlp "{video_url}"'
        
        # Execute the command
        os.system(command)
        
        print("Download completed successfully.")
        
    except Exception as e:
        print(f"An error occurred during download: {e}")

def download_music(video_url) -> None:
    """
    Download a YouTube video using yt-dlp
    
    Args:
        video_url (str): Full YouTube URL of the video to download
    """
    
    
    try:
        # Construct the yt-dlp command
        command = f'cd "{os.getenv("YOUR_MUSIC_DOWNLOAD_DIRECTORY")}" && yt-dlp -x --audio-format mp3 "{video_url}"'
        
        # Execute the command
        os.system(command)
        
        print("Download completed successfully.")
        
    except Exception as e:
        print(f"An error occurred during download: {e}")


def main():
    # Get user input
    print("=" * 50)
    print("YouTube Song Search")
    print("=" * 50)
    song_name = input("\nEnter the song name: ").strip()
    
    if not song_name:
        print("Please enter a valid song name!")
        return
    
    print(f"\nSearching for '{song_name}'...")
    
    # Search for the song
    video_url, video_title = search_youtube_song(song_name)
    
        
    print("=" * 50) 
    
    if video_url:
        print(f"\n✓ Found: {video_title}")
        print(f"URL: {video_url}")
         # Download the video if found
    if video_url:
        download_video(video_url)        
        print("=" * 50)
        
        
    else:
        print("\n✗ No results found. Please try a different search term.")

if __name__ == "__main__":
    
    
    def checking_api_key(song_name) -> None:
        '''# Build the YouTube API client
        youtube = build('youtube', 'v3', developerKey=os.getenv("USE_YOUR_OWN_API_KEY_DA_NON_SENSE"))
        
        # Search for the song
        search_response = youtube.search().list(
            q=song_name,
            part='id,snippet',
            maxResults=10,  # Get only the top result
            type='video'   # Search only for videos
        ).execute()
        print(json.dumps(search_response, indent=2))
    checking_api_key("Sad Tamil Songs")'''
    
    main()