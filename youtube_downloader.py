import yt_dlp

def download_youtube_video(url, resolution='2160'):
    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
        'outtmpl': '%(title)s.%(ext)s',  # Save video with its title as filename
        'merge_output_format': 'mp4',  # Merge video and audio into a single file
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from URL: {url}")
            ydl.download([url])
            print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace with the YouTube video URL you want to download
    video_url = input("Enter the YouTube video URL: ")
    resolution = input("Enter the desired resolution (e.g., 2160 for 4K, 1080 for Full HD): ")
    download_youtube_video(video_url, resolution)
