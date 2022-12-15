import csv
import os
from math import sqrt
import sys

import numpy as np
import pandas as pd
from numpy import vectorize
from scipy.sparse.linalg import svds
from sklearn.metrics import mean_squared_error
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.model_selection import train_test_split



def load_music_data(file_name):
    """Get reviews data, from local csv."""
    if os.path.exists(file_name):
        # print("-- " + file_name + " found locally")
        df = pd.read_csv(file_name)

    return df
def getSongbyIndex(index, song):
    a = 0
    for u in song:
        
        if(song[u]==index):
            a = u
    return a
def values_to_map_index(values):
    map_index = {}
    idx = 0
    for val in values:
        map_index[val] = idx
        idx += 1

    return map_index
if __name__ == "__main__":
    file = sys.argv[2]
    filedata = sys.argv[1]
    # print(idSong)
    song_data = load_music_data(filedata)
    user_idx = values_to_map_index(song_data.user_id.unique())
    
    song_idx = values_to_map_index(song_data.song_id.unique())
    # n_users = song_data.user_id.unique().shape[0]
    # n_items = song_data.song_id.unique().shape[0]
    # us = 0
    # # print(song_idx)
    # for u in user_idx:
        
    #     if(user_idx[u]==9):
    #         print(u)
    song=load_music_data(file)
    # print(song_idx)
    # print(song_idx[int(idSong)])

    for line in song.itertuples():
        
         # print(line)
        for i in line:
            print(getSongbyIndex(i, song_idx), end = ",")
        print()

        