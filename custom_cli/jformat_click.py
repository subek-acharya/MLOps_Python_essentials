import json
import click

def formatter(string, sort_keys=True, indent=4):
    # load incoming string into JSON
    loaded_json = json.loads(string)
    # dump as a string
    return json.dumps(loaded_json, sort_keys=sort_keys, indent=indent)

@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--sort', '-s', is_flag=True)
def main(path, sort):
    with open(path, 'r') as _f:
        print(formatter(_f.read(), sort_keys=sort))

if __name__ == "__main__":
    main()

## Command Line sample: python jformat.py examples/examples.json
