import sys
import pandas as pd
from io import StringIO



#print(sys.argv[1:])
#fucntion to concatenate dataframe along axis=0
def merge_frames(dataframes):
    return dd.concat(dataframes, axis=0)

def main():
    frames = []
    #need stringIO to prevent output in console from changing format of df
    output = StringIO()

    #read in arguments which are filepaths
    for arg in sys.argv[1:]:
        for chunk in pd.read_csv(arg, chunksize=10**3):
            filename = arg.split('/')[-1]
            chunk['filename'] = filename
            frames.append(chunk)



    for frame in frames:
        print(frame.to_csv(index=False, line_terminator='\n', chunksize=10**3), end='')
    
    #df.to_csv('combined.csv')

if __name__ == '__main__':
    main()
