from utils import sc, spf, yt
import os

bases = ["https://soundcloud.com/", "https://www.youtube.com/", "https://open.spotify.com/", "https://spotify.com"]
spotdir = "./Downloads/Spotify"
scdir = "./Downloads/SoundCloud"
ytdir = "./Downloads/Youtube"
alldir = "./Downloads/All"
path = ""

UseAllFolder = False
usedefaultpath = True

def site(url):
    YouTube = False
    SoundCloud = False
    Spotify = False
    baseurls = bases
    for ur in baseurls:
        if str(url).startswith(ur):
            if "soundcloud.com" in ur:
                SoundCloud = True
                print(f"SoundCloud link detected.")
            elif "youtube.com" in ur:
                YouTube = True
                print(f"Youtube link detected.")
            elif "spotify.com" in ur:
                Spotify = True
                print(f"Spotify link detected.")
            
            else:
                print(f"Not a valid link, Skipping...")
    return YouTube, SoundCloud, Spotify

def download(url, useall=bool, path=None):
    YouTube, SoundCloud, Spotify = site(url)
    if useall == True:
        if path:
            if YouTube:
                yt.Download(url, path)
            if SoundCloud:
                sc.Download(url, path)
            if Spotify:
                spf.Download(url, path)
        else:
            if YouTube:
                yt.Download(url, ytdir, alldir)
            if SoundCloud:
                sc.Download(url, scdir, alldir)
            if Spotify:
                spf.Download(url, spotdir, alldir)
    else:
        if path:
            if YouTube:
                yt.Download(url, path)
            if SoundCloud:
                sc.Download(url, path)
            if Spotify:
                spf.Download(url, path)
        else:
            if YouTube:
                yt.Download(url, ytdir)
            if SoundCloud:
                sc.Download(url, scdir)
            if Spotify:
                spf.Download(url, spotdir)

print("""
            ---INTERNET DOWNLOADER---
             CURRENTLY IMPLEMENTED:
                   SPOTIFY
                   SOUNDCLOUD
                   YOUTUBE

    ~~[SPOTIFY IS SLOWER THAN THE OTHERS]~~\n\n
""")


choice = input(f"Use default Downloads path? [./Downloads] [Y/N] ")
if choice.lower() == "y":
    usedefaultpath = True
    print(f"Using default download path...\n")
elif choice.lower() == "n":
    usedefaultpath = False
    print(f"Using custom download path...\n")
else:
    usedefaultpath = True
    print(f"INVALID INPUT - using default download path...\n")


if usedefaultpath == True:
    choose = input(f"Use 'ALL' folder? [Downloads each song twice, Turn off for Playlists / Albums to save time.] [Y/N] ")
    if choose.lower() == "y":
        UseAllFolder = True
        print(f"Using 'All' folder, will take longer...\n")
    elif choose.lower() == "n":
        UseAllFolder = False
        print(f"Not using 'All' folder, will be faster...\n")
    else:
        UseAllFolder = True
        print(f"INVALID INPUT - using 'All' folder by default...\n")

listfile = "./list.txt"

def processfile(file, download, UseAllFolder):
    print(f"\nReading list.txt file...\n")
    with open(file, 'r') as lfile:
        lines = lfile.readlines()
    print(f"\nRead file sucessfully.\n")
    i = 1
    ia = len(lines)
    for url in lines:
        url = url.strip()
        print(f"\n\nDownloading URL [{i} / {ia}]\n\n")
        download(url, UseAllFolder)
        i += 1

def processfilecustom(file, download, path):
    print(f"\nReading list.txt file...\n")
    with open(file, 'r') as lfile:
        lines = lfile.readlines()
    print(f"\nRead file sucessfully.\n")
    i = 1
    ia = len(lines)
    for url in lines:
        url = url.strip()
        print(f"\n\nDownloading URL [{i} / {ia}]\n\n")
        download(url, UseAllFolder, path)
        i += 1

if usedefaultpath == True:
    processfile(listfile, download, UseAllFolder)
else:
    paths =  input(f"Enter the path to download files to: ")
    os.makedirs(paths, exist_ok=True)
    processfilecustom(listfile, download, paths)


cho = input(f"Open Downloaded Path? [Y/N] ")
if cho.lower() == "y":
    if usedefaultpath == False:
        pat = paths.replace('/', '\\')
        os.system(f"start {pat}")
    else:
        os.system(f"start Downloads")