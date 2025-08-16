import os
import sys
import json

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
    path, no_sort_str = sys.argv[-2:]
    no_sort = no_sort_str.lower() == 'true'
    main(path, no_sort)

## Command Line sample: python jformat.py examples/examples.json true