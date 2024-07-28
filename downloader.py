import yt_dlp
import youtube_dl
import os

def download_vimeo_audio(video_url, output_path):
    """
    Downloads audio from a Vimeo video and saves it as an MP3 file.

    Parameters:
    video_url (str): The URL of the Vimeo video.
    output_path (str): The directory where the MP3 file will be saved.
    """
    try:
        # Define options for yt-dlp with HTTP headers to mimic a real browser
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
            },
            'extractor_args': {
                'vimeo': {
                    'impersonate': 'random'
                }
            }
        }

        # Try to download the audio from the video using yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

    except Exception as e:
        print(f"yt-dlp failed, trying youtube-dl. Error: {e}")

        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'http_headers': {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
                },
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
        
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    vimeo_url = input("Enter the Vimeo video URL: ")
    output_directory = input("Enter the output directory: ")

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Download the audio
    download_vimeo_audio(vimeo_url, output_directory)
    print("Download completed.")