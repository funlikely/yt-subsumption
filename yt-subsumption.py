import subprocess
import sys
import os


def download_videos(input_file, output_dir):
    with open(input_file, 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        if url:
            download_video(url, output_dir)


def download_video(url, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    command = ['yt-dlp.exe', '-f', 'bestvideo+bestaudio',
               '--merge-output-format', 'mp4', url,
               '-o', f'{output_dir}/%(uploader)s - %(title)s [%(id)s].%(ext)s']

    try:
        subprocess.run(command, check=True)
        print(f'Successfully downloaded: {url}')
    except subprocess.CalledProcessError as e:
        print(f'Error downloading {url}: {e}')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_dir yt_dlp_path")
        sys.exit(1)

    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    download_videos(input_file, output_dir)
