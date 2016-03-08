#ToDo opcion para cambiar a txt utf8 todos los archivos del directorio

import glob, os, csv, argparse, sys


def retrive(directory):
    for filename in sorted(glob.glob(os.path.join(directory, '*.txt'))):
        with open(filename, 'r') as f:
            important_stuff = f.read().splitlines()
            oneline = [''.join(important_stuff)]
            yield filename.split('/')[-1] + ', ' +str(oneline).strip('[]"')

def corpus_writer(directory2):
    test = tuple(retrive(opts.input))
    with open(opts.output,'w') as out:
        csv_out=csv.writer(out, delimiter='|')
        csv_out.writerow(['id','content'])
        for row in test:
            csv_out.writerow(row.split(', ', 1))


NAME='corpus_creator'
prefix='corpus'

if __name__ == "__main__":
    p = argparse.ArgumentParser(NAME)

    p.add_argument('-input_directory:', '--input', default=sys.stdin)

    p.add_argument('-output_corpus:', '--output', default=sys.stdout)

    opts = p.parse_args()
    retrive(opts.input)
    corpus_writer(opts.output)
