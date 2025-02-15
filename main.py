from utils import sc, spf, yt
import os

bases = ["https://soundcloud.com/", "https://www.youtube.com/", "https://open.spotify.com/", "https://spotify.com"]
spotdir = "./Downloads/Spotify"
scdir = "./Downloads/SoundCloud"
ytdir = "./Downloads/Youtube"
alldir = "./Downloads/All"

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
            
    if YouTube == False & SoundCloud == False & Spotify == False:
        print(f"Not a valid link, Skipping...")
    return YouTube, SoundCloud, Spotify

def download(url, useall=bool):
    YouTube, SoundCloud, Spotify = site(url)
    if useall == True:
        if YouTube:
            yt.Download(url, ytdir, alldir)
        if SoundCloud:
            sc.Download(url, scdir, alldir)
        if Spotify:
            spf.Download(url, spotdir, alldir)
    else:
        if YouTube:
            yt.Download(url, ytdir)
        if SoundCloud:
            sc.Download(url, scdir)
        if Spotify:
            spf.Download(url, spotdir)    

def download_custom_path(url, path):
    Youtube, SoundCloud, Spotify = site(url)
    if Youtube:
        yt.Download(url, path)
    if SoundCloud:
        sc.Download(url, path)
    if Spotify:
        spf.Download(url, path)

prompt = f"Enter Spotify / Soundcloud / Youtube link: "

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

active = True

if usedefaultpath == True:
    while active == True:
        url = input(f"\nEnter Spotify / Soundcloud / Youtube link: ")
        download(url, UseAllFolder)
        more = input(f"\nDownload more? [Y/N] ")
        if str(more).lower() == "y":
            active = True
            continue
        elif str(more).lower() == "n":
            active = False
            break
        else:
            print(f"[Y/N] - Not entered, program will shut down...")

if usedefaultpath == False:
    path = input(f"\nEnter the path to download files: ")
    os.makedirs(path, exist_ok=True)
    while active == True:
        url = input(f"\nEnter Spotify / Soundcloud / Youtube link: ")
        download_custom_path(url, path)
        more = input(f"\nDownload more? [Y/N] ")
        if str(more).lower() == "y":
            active = True
            continue
        elif str(more).lower() == "n":
            active = False
            break
        else:
            print(f"[Y/N] - Not entered, program will shut down...")

cho = input(f"Open Downloaded Path? [Y/N] ")
if cho.lower() == "y":
    if usedefaultpath == False:
        pat = path.replace('/', '\\')
        os.system(f"start {pat}")
    else:
        os.system(f"start Downloads")