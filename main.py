import yt_dlp

def download_mp3(video_url, output_path='./'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path + '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def download_multiple_videos(video_urls, output_path='./'):
    for video_url in video_urls:
        print(f"Downloading {video_url}")
        download_mp3(video_url, output_path)
        print(f"Downloaded {video_url}")

if __name__ == '__main__':
    video_links = [
        'https://www.youtube.com/watch?v=yiLXNmPcEzw',
        # Add your links here

    ]
    
    output_directory = './downloads/'
    download_multiple_videos(video_links, output_directory)
