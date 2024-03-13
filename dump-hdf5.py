#!/usr/bin/env python3

import sys
import h5py
import argparse


def display(item, all, space=""):
    if not hasattr(item, "keys"):
        return

    for k in item.keys():
        it = item[k]
        print(space, k, " ", it)
        if all:
            for i in it:
                print(i)
        display(it, all, space=space + "  ")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file_name", type=str, help="File name of hdf5 to dump")
    parser.add_argument("-a", "--all", action="store_true")

    args = parser.parse_args()
    if args.file_name is None:
        print("No filename given")
        sys.exit(0)

    with h5py.File(args.file_name) as hf:
        display(hf, args.all)
