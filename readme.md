# Simple YouTube video downloader

## Can be run via command line arguments, or via Jupyter notebook inputs

### [main.py](https://github.com/KadeWalsh/YouTube-Downloader/blob/master/main.py)
#### Contains all code necessary to run downloader functions
- Checks for command-line arguments
    > If none found defaults to prompting for inputs
- If command-line arguments included when running code then checks arguments for valid options
    - Playlist filename must be valid
    - Playlist file is read into list of links and processed one by one
    - Download format must be either "--a" or "--v"
        - "--v" results in full video download (.mp4 file export)
        - "--a" returns audio only (.mp3 file export)

### [playlist.txt](https://github.com/KadeWalsh/YouTube-Downloader/blob/master/playlist.txt)
- Plain text file
- Contains a single link per line which is loaded into [main.py](https://github.com/KadeWalsh/YouTube-Downloader/blob/master/main.py)
- Links may have, but do not require, 'http' prefix
