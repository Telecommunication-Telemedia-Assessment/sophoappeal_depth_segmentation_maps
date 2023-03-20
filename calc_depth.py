#!/usr/bin/env python3

import argparse
import sys
import multiprocessing
import json

from PIL import Image
import numpy as np
import seaborn as sns


def analyze_depth_map(depth_map):
    with Image.open(depth_map) as im:
        values = np.array(im)

        result = {
            "image": depth_map,
            "mean_depth": values.mean(),
            "std_depth": values.std()
        }
        return result



def main(_):
    # argument parsing
    parser = argparse.ArgumentParser(description='extracts depth information from depth map',
                                     epilog="stg7 2021",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("depth_map", type=str, nargs="+", help="image of the depth map, that has been extracted before")
    parser.add_argument('--cpu_count', type=int, default=multiprocessing.cpu_count() // 2, help='thread/cpu count')
    parser.add_argument("--result_file", type=str, default="depths.json", help="file where all results are stored")

    a = vars(parser.parse_args())

    pool = multiprocessing.Pool(multiprocessing.cpu_count())

    result = pool.map(analyze_depth_map, a["depth_map"])

    with open(a["result_file"], "w") as rfp:
        json.dump(result, rfp, indent=4, sort_keys=True)





if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

