#!/usr/bin/python3
import requests
import json
import sys
#主播mid
roomid = 20848957
#保存视频的名字
name = 3
#####
#####
#####
#得到真实的房间号
room_url = 'https://api.live.bilibili.com/room/v1/Room/getRoomInfoOld?mid={}'.format(roomid)
room_url_jieguo = requests.get(url=room_url).json()
room_url_id = room_url_jieguo['data']['roomid']
#得到播放地址
palyer_url  = 'https://api.live.bilibili.com/room/v1/Room/playUrl?cid={}'.format(room_url_id)
palyer_url_jieguo = requests.get(url=palyer_url).json()
palyer_url_down = palyer_url_jieguo['data']['durl'][0]['url']
#下载
size = 0
r = requests.get(palyer_url_down, headers={'Referer': 'https://live.bilibili.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}, stream=True, verify=False)
with open(f'{name}.mp4', "wb") as file:
     for data in r.iter_content(chunk_size =1024*1024):
         file.write(data)
         size += len(data)
         file.flush()
         sys.stdout.write('  [下载进度]:%.2fMB' % float(size /1024/1024 ) + '\r')

print("下载结束")
