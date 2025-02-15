import os

def Download(url, location, location2=None):
    os.system(f"cd {location} && scdl -l {url}")
    if location2:
        os.system(f"cd {location2} && scdl -l {url}")

if __name__ == "__main__":
    link = input("Enter Soundcloud link: ")
    Download(link, "./")