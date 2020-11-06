#!/usr/bin/env python3

import sys
import os
import requests
import zipfile

def download_file(url, filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

login = input('Login: ')
token = input('Token: ')
curator_id = input('ID: ')
url = 'https://gql.twitch.tv/gql'
headers = {'Authorization': 'OAuth ' + token}
payload = '[{"operationName":"ClipsManagerTable_User","variables":{"login":"' + login + '","limit":20,"criteria":{"sort":"CREATED_AT_DESC","period":"ALL_TIME","curatorID":"' + curator_id + '"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"0bc0fef26eb0739611d8ac1aa754ed44630d96a87854525bf38520ffe26460d4"}}}]'

r = requests.post(url, headers=headers, data=payload)

edges = r.json()[0]['data']['user']['clips']['edges']

cursor = edges[-1]['cursor']

while cursor != None:
    payload = '[{"operationName":"ClipsManagerTable_User","variables":{"login":"' + login + '","limit":20,"criteria":{"sort":"CREATED_AT_DESC","period":"ALL_TIME","curatorID":"' + curator_id + '"},"cursor":"' + cursor + '"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"0bc0fef26eb0739611d8ac1aa754ed44630d96a87854525bf38520ffe26460d4"}}}]'
    r = requests.post(url, headers=headers, data=payload)
    new_edges = r.json()[0]['data']['user']['clips']['edges']
    edges += new_edges
    cursor = new_edges[-1]['cursor']

urls = []

for clip in edges:
    urls.append((clip['node']['title'], clip['node']['videoQualities'][0]['sourceURL']))

clips_num = len(urls)

with zipfile.ZipFile('clips.zip', 'a') as zfile:
    i = 1
    for clip in urls:
        clip_title = "".join(x for x in clip[0] if (x.isalnum() or x in "._- ")) + ".mp4"
        # clip_title = shlex.quote(clip_title)
        clip_url = clip[1]
        # print('{0} === {1}'.format(clip_title, clip_url))

        # os.system('wget {0} -O \'{1}\''.format(clip_url, clip_title))
        print('[{0}/{1}] Downloading {2} '.format(i, clips_num, clip_title), end='', flush=True)
        download_file(clip_url, clip_title)
        zfile.write(clip_title)
        # os.system('rm \'{0}\''.format(clip_title))
        os.remove(clip_title)
        # print('=====\nDownloaded {0}/{1}\n=====\n'.format(i, clips_num))
        print('Done')
        i += 1
