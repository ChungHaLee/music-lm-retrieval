import os
import sys
from os import rename, listdir

for (path, dir, files) in os.walk("/Users/lifeofpy/Documents/musiclm-2023/audioset/"):
    for filename in files:
        # print(filename)
        preid = os.path.splitext(filename)[0]
        ytid = preid[1:11]


for (path, dir, files) in os.walk("/Users/lifeofpy/Documents/musiclm-2023/audioset/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        # if ext == '.m4a':
        #     print('옴')
        #     print("%s/%s" % (path, filename))
        #     replaced = filename.replace("m4a", "webm")
        #     rename(path+'/'+filename, path+'/'+replaced)
        #     print(filename,' -> ',replaced)
        #     print('변환 완료')