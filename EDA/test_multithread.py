import multiprocessing
import os
import subprocess
import time


def uncompress(file):
    subprocess.run(f"C:/Windows/flac.exe -df --delete-input-file --preserve-modtime --keep-foreign-metadata D:/SonarData/flat/{file}", shell=True, capture_output=True)
    return True


def main():
    start = time.time()
    pool = multiprocessing.Pool(7)
    files = os.listdir("D:/SonarData/flat")
    # for file in messing_files:
    #     uncompress(file)
    # step = int(len(messing_files) / 6)
    # hold = [messing_files[j: j + step] for j in [i for i in range(0, len(messing_files), step)]]
    r = pool.map_async(uncompress, files)
    r.wait()
    pool.close()
    end = time.time()
    print(f"Time elapsed: {end - start}")
    # 59.13787841796875
    # 210.7


if __name__ == "__main__":
    main()
