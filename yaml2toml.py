import toml
import os, sys

def yaml2toml(dirname):
    """
    Convert all .yml files in the given directory into .toml files,
    recursively.
    """
    import yaml
    for cwd, dir_, fnames in os.walk(dirname):
        for fname in fnames:
            if fname.endswith('.yml'):
                path = os.path.join(cwd, fname)
                with open(path) as source:
                    dic = yaml.safe_load(source.read())
                with open(path[:-3] + 'toml', 'w') as target:
                    toml.dump(dic, target)
                print('Saved %s' % target.name)


if __name__ == '__main__':
    input_dir = sys.argv[1]
    yaml2toml(input_dir)