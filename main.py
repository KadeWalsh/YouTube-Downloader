from pytube import YouTube
import sys
import os


def make_safe_filename(video_title):
    # Replace spaces with underscores
    video_title = video_title.replace(" ", "_")
    # Define list of symbols to remove
    replace_symbols = ["\'", "\"" "@", "#", "%", ".", ",", "(", ")", "/", "\\"]
    # Check for each symbol in list
    for symbol in replace_symbols:
        # Remove any instance of symbol
        video_title = video_title.replace(symbol, "")

    # Return cleaned filename string
    return video_title


def download(url, audio_only):
    yt = YouTube(url)
    yt_stream = yt.streams
    video_title = make_safe_filename(yt.title)
    if audio_only is True:
        video_stream = yt_stream.get_audio_only()
        filename = f"{video_title}.mp3"

    else:
        video_stream = yt_stream.get_highest_resolution()
        filename = f"{video_title}.mp4"

    video_stream.download(filename=filename, output_path="")


def download_songs(playlist, audio_only):
    for song in playlist:
        song = song.strip()

        download(song, audio_only)


def command_line_downloader():
    if len(sys.argv) != 3:
        print("Usage: python main.py <source> <download_format>")
        print("<source> accepts path to .txt file")
        print("<download_format> accepts --a for audio only,", end=" ")
        print("or --v for full video")
        exit(1)

    if sys.argv[2].lower() not in ["--v", "--a"]:
        print("Please include --a or --v to indicate audio only,", end=" ")
        print("or full video download")
        exit(1)

    format = sys.argv[2].lower().removeprefix("--")
    source = sys.argv[1]

    if ".txt" not in source:
        print("Invalid playlist file format")
        exit(1)

    else:
        if os.path.exists(source):
            playlist = open(source, 'r').readlines()
        else:
            print("Invalid playist file")
            exit(1)

    if format == "a":
        audio_only = True

    else:
        audio_only = False

    download_songs(playlist, audio_only)


def alternate_downloader(source, output_format):
    if os.path.exists(source):
        playlist = open(source, 'r').readlines()
    else:
        print("Invalid playist file")
        exit(1)

    download_songs(playlist, format)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        command_line_downloader()

    else:
        print("Do you want to download the (v)ideo, or only the (a)udio?")

        while True:
            download_format = input("Enter 'v' or 'a' to continue:  ").lower()
            if download_format not in "av":
                print(download_format)
                continue
            else:
                format = download_format == 'a'
                break

        alternate_downloader(input("playlist filename:  "), format)
