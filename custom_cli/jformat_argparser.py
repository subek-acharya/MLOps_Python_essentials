import os
import sys
import json
import argparse

def formatter(string, sort_keys=True, indent=4):
    loaded_json = json.loads(string)
    return json.dumps(loaded_json, sort_keys=sort_keys, indent=indent)

def main(path, no_sort):
    if no_sort:
        sort_keys = False
    else:
        sort_keys = True
    with open(path, 'r') as _f:
        print(formatter(_f.read(), sort_keys=sort_keys))

print(sys.argv)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "This is a jformat tool")
    parser.add_argument("--sort", action="store_true", help ="set the sorting")
    parser.add_argument("path", help="path to the JSON file")
    args = parser.parse_args()
    main(args.path, args.sort)

