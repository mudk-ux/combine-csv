import sys
import pandas as pd

def main():
    #list to hold all generated dataframes
    frames = []
    #iterate over command line arguments
    for arg in sys.argv[1:]:
        #split data into chunks to prevent memory errors
        for chunk in pd.read_csv(arg, chunksize=10**3):
            filename = arg.split('/')[-1]
            chunk['filename'] = filename
            frames.append(chunk)

    #append to csv in chunks
    for frame in frames:
        print(frame.to_csv(index=False, line_terminator='\n', chunksize=10**3), end='')


if __name__ == '__main__':
    main()
