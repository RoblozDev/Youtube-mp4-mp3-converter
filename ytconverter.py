import yt_dlp
import os

def print_ascii_banner():
    print(r"""
·······························································
:██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗:
:╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝:
: ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝█████╗  :
:  ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝  :
:   ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗:
:   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝:
:                                                             :
:████████╗ ██████╗                                            :
:╚══██╔══╝██╔═══██╗                                           :
:   ██║   ██║   ██║                                           :
:   ██║   ██║   ██║                                           :
:   ██║   ╚██████╔╝                                           :
:   ╚═╝    ╚═════╝                                            :
:                                                             :
:███╗   ███╗██████╗ ██╗  ██╗    ██╗███╗   ███╗██████╗ ██████╗ :
:████╗ ████║██╔══██╗██║  ██║   ██╔╝████╗ ████║██╔══██╗╚════██╗:
:██╔████╔██║██████╔╝███████║  ██╔╝ ██╔████╔██║██████╔╝ █████╔╝:
:██║╚██╔╝██║██╔═══╝ ╚════██║ ██╔╝  ██║╚██╔╝██║██╔═══╝  ╚═══██╗:
:██║ ╚═╝ ██║██║          ██║██╔╝   ██║ ╚═╝ ██║██║     ██████╔╝:
:╚═╝     ╚═╝╚═╝          ╚═╝╚═╝    ╚═╝     ╚═╝╚═╝     ╚═════╝ :
·······························································
YouTube Video Downloader and Converter
Supports MP4 and MP3 formats
          
          """)

print_ascii_banner()

def download(url, format_choice):
    output_dir = "downloads"
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    }

    if format_choice == 'mp3':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    elif format_choice == 'mp4':
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
        })
    else:
        print("Invalid format! Choose 'mp3' or 'mp4'")
        return

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"Downloaded video as {format_choice}")

def main():
    url = input("Enter YouTube video URL: ").strip()
    fmt = input("Choose format (mp4/mp3): ").strip().lower()
    download(url, fmt)

if __name__ == "__main__":
    main()