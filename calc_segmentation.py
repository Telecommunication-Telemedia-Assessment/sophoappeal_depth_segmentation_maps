#!/usr/bin/env python3

import argparse
import sys
import multiprocessing
import json

from PIL import Image
import numpy as np
import seaborn as sns


def analyze_segmentation(segmentation_map):
    with Image.open(segmentation_map) as im:

        values = np.array(im)
        #alpha = values[:, :, 1]
        v = np.zeros(values.shape[0:2])
        values_map = {}
        i = 0
        for row in range(values.shape[0]):
            for col in range(values.shape[1]):
                key = str(values[row, col][0]) + "," + str(values[row, col][1]) + "," + str(values[row, col][2])
                if key not in values_map:
                    values_map[key] = i
                    i += 1
                v[row, col] = values_map[key]

        result = {
            "image": segmentation_map,
            "number_segmentation": i,
            "std_segmentation": v.std(),
            "mean_segmentation": v.mean(),
        }
        return result



def main(_):
    # argument parsing
    parser = argparse.ArgumentParser(description='extracts segmentation information from segmentation map',
                                     epilog="stg7 2021",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("segmentation_map", type=str, nargs="+", help="image of the segmentation map, that has been extracted before")
    parser.add_argument('--cpu_count', type=int, default=multiprocessing.cpu_count() // 2, help='thread/cpu count')
    parser.add_argument("--result_file", type=str, default="segmentations.json", help="file where all results are stored")

    a = vars(parser.parse_args())

    pool = multiprocessing.Pool(multiprocessing.cpu_count())

    result = pool.map(analyze_segmentation, a["segmentation_map"])

    with open(a["result_file"], "w") as rfp:
        json.dump(result, rfp, indent=4, sort_keys=True)





if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

