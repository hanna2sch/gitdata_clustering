import os
from genericpath import isfile
from ntpath import join
import pandas as pd

path = os.path.dirname(os.path.realpath(__file__))
datapath = os.path.dirname(os.path.realpath(__file__)) + "\\data\\test" 
def get_filenames(path):
    return os.listdir(path)
filenames=get_filenames(path + "\\data\\gitdata")
datanames = (get_filenames(datapath))
def make_new_folder(path, foldername):
    if not os.path.exists(path+"\\"+foldername):
        os.mkdir(path+"\\"+foldername)
        print(foldername)
for folder in filenames:
    localpath = path + "\\data\\gitdata\\"+folder+"\\"
    files = get_filenames(localpath)
    for file in files:
        
        df = pd.read_parquet(localpath+file)
        make_new_folder(path+"\\data\\result", folder)
        df.to_csv(path + "\\data\\result\\"+folder+"\\"+file+".csv")