import os

def Download(url, location, location2=None):
    os.system(f"cd {location} && spotdl {url}")
    if location2:
        os.system(f"cd {location2} && spotdl {url}")

if __name__ == "__main__":
    link = input(f"Enter Spotify link: ")
    Download(link, "./")