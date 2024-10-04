# YouTube MP3 Downloader

This Python script allows you to download audio from YouTube videos and convert them into MP3 format using the `yt-dlp` library and `FFmpeg`. You can download single videos or multiple videos at once by providing their URLs.

## Features
- Download the best available audio from a YouTube video.
- Automatically convert the downloaded audio to MP3 format.
- Customize the output directory for the downloaded files.
- Support for downloading multiple videos in a single run.

## Requirements

Before running the script, make sure you have the following dependencies installed:

### Python Packages:
- `yt-dlp`: You can install it using pip:
  ```bash
  pip install yt-dlp
  ```

### External Requirements:
- **FFmpeg**: This script requires `FFmpeg` to extract and convert the audio to MP3. You can download it from [FFmpeg's official website](https://ffmpeg.org/download.html) and follow the installation instructions.

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/youtube-mp3-downloader.git
   cd youtube-mp3-downloader
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Edit the script:

   - Add your YouTube video links to the `video_links` list in `main.py`.
   - Change the `output_directory` variable to specify where you want the MP3 files to be saved (default is `./downloads/`).

4. Run the script:
   ```bash
   python main.py
   ```

## Example

```python
video_links = [
    'https://www.youtube.com/watch?v=yiLXNmPcEzw',
    'https://www.youtube.com/watch?v=example_link_2'
]
output_directory = './downloads/'
download_multiple_videos(video_links, output_directory)
```

## Contributing
Feel free to open a pull request or an issue if you encounter any bugs or have suggestions for improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
