import subprocess
import sys


def download_videos(input_file, output_dir, yt_dlp_path):
    with open(input_file, 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        if url:
            download_video(url, output_dir, yt_dlp_path)


def download_video(url, output_dir, yt_dlp_path):
    command = [yt_dlp_path, '-f', 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/bv*+ba/b', url, '-o',
               f'{output_dir}/%(title)s.%(ext)s']

    try:
        subprocess.run(command, check=True)
        print(f'Successfully downloaded: {url}')
    except subprocess.CalledProcessError as e:
        print(f'Error downloading {url}: {e}')


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py input_file output_dir yt_dlp_path")
        sys.exit(1)

    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    yt_dlp_path = sys.argv[3]

    download_videos(input_file, output_dir, yt_dlp_path)
