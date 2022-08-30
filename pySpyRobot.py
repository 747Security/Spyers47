#Python code to write a robot file
#!/usr/bin/python3
import urllib.request
import io
website = input('Enter the Website to Look up:')
def GetRobots(url):
    if url.endswith("/"):
        path = url
    else:
        path = url + "/"
    requestingData = urllib.request.urlopen(path + "robots.txt", data=None)
    data = io.TextIOWrapper(requestingData, encoding="utf 8")
    return data.read()
print(GetRobots(f"{website}"))
print("Thank you for using Spyers47")