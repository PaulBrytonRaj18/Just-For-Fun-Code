import os
import sys
import json
import dotenv
from googleapiclient.discovery import build

# Load environment variables from .env file
dotenv.load_dotenv(dotenv_path=".env", override=True)

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
            maxResults=10,  # Get only the top result
            type='video'   # Search only for videos
        ).execute()
        
        # Extract the video ID from the search results
        if search_response['items']:
            video_id = search_response['items'][0]['id']['videoId']
            video_title = search_response['items'][0]['snippet']['title']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            
            return video_url, video_title
        else:
            return None, None
            
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

def is_correct_video(video_title: str, song_name: str) :
    input(f'Is the video title "{video_title}" a correct match for the song name "{song_name}"? (y/n)')
    
    while input().lower() not in ['y', 'n']:
        print("Please enter 'y' for yes or 'n' for no.")
        input(f'Is the video title "{video_title}" a correct match for the song name "{song_name}"? (y/n)')
        
    if input().lower() == 'y':
        return True
    
    i = 1
    while input().lower() == 'n':
        video_title = search_response['items'][i]['snippet']['title']
        input(f'Is the video title "{video_title}" a correct match for the song name "{song_name}"? (y/n)')
        i += 1
        

def download_video(video_url) -> None:
    """
    Download a YouTube video using yt-dlp
    
    Args:
        video_url (str): Full YouTube URL of the video to download
    """
    
    
    try:
        # Construct the yt-dlp command
        command = f'cd "{os.getenv("YOUR_DOWNLOAD_DIRECTORY")}" && yt-dlp -x --audio-format mp3 "{video_url}"'
        
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
    
    if video_url:
        print(f"\n✓ Found: {video_title}")
        print(f"URL: {video_url}")
        is_correct_video(video_title, song_name)
        download_video(video_url)
        
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