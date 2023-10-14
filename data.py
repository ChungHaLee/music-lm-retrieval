import pandas as pd
import os
import sys
from os import rename, listdir

musiccaps = pd.read_csv('./musiccaps-public.csv')
id = musiccaps['ytid'].values
id_lst = set(id.tolist())


ytid_lst = []
for (path, dir, files) in os.walk("/Users/lifeofpy/Documents/musiclm-2023/audioset/"):
    for filename in files:
        # print(filename)
        preid = os.path.splitext(filename)[0]
        ytid = preid[0:11]
        # print(ytid)
        ytid_lst.append(ytid)

ytid_lst = set(ytid_lst)

same_lst = id_lst & ytid_lst
print(len(same_lst))

