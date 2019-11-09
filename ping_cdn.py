import json
import os
import re
import numpy as np
import matplotlib.pyplot as plt

def pingCache(video_url):
    try:
        ydl = os.popen("youtube-dl -g " + video_url).read()
        cache_ip = re.search("sn-.{5,20}?&", ydl).group(0)[:-1]
        cache_url = re.search("r\d---", ydl).group(0) + cache_ip + ".googlevideo.com"
        print(cache_url)
        ping = os.popen("ping -c6 " + cache_url).read()
        pings = re.findall("time=\d+\.?\d?", ping)        
        pings = [float(ping.split("=")[1]) for ping in pings]
        return np.mean(pings), np.std(pings)
    except:
        return -1, -1            


mostPopular = open("mostpopularresults.txt", "r").read()
ids = re.findall("u'id': u'(.{1,15})'}", mostPopular)
urls = ["https://www.youtube.com/watch?v="+id for id in ids]
results = []
for url in urls:
    mean, std = pingCache(url)
    print(mean)
    if (mean > -1):
        results.append(mean)

results = np.array(results)
results = results[~np.isnan(results)]
f = open("pings.txt", "w")
f.write(str(results))
f.close()
fig, ax = plt.subplots()
ax.plot(np.arange(len(results)), results)
fig.savefig("means", format="png")