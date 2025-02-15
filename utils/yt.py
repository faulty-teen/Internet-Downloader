from pytubefix import YouTube

def Download(url, location, location2=None):
    Obj = YouTube(url)
    Obj = Obj.streams.get_highest_resolution()
    try:
        Obj.download(output_path=location)
    except Exception as e:
        print(f"An error has occured: {e}")
    if location2:
        try:
            Obj.download(output_path=location2)
        except Exception as e:
            print(f"An error has occured: {e}")

if __name__ == "__main__":
    link = input(f"Enter YT link: ")
    Download(link, "./")