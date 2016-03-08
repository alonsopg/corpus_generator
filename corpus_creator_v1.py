#ToDo opcion para cambiar a txt utf8 todos los archivos del directorio

import glob, os, csv, argparse, sys


def retrive(directory):
    for filename in sorted(glob.glob(os.path.join(directory, '*.txt'))):
        with open(filename, 'r') as f:
            important_stuff = f.read().splitlines()
            oneline = [''.join(important_stuff)]
            yield filename.split('/')[-1] + ', ' +str(oneline).strip('[]"')


def corpus_writer(directory2):
    test = tuple(retrive(opts.DIR))
    with open('new_corpus.csv','w') as out:
        csv_out=csv.writer(out, delimiter='|')
        csv_out.writerow(['id','content'])
        for row in test:
            csv_out.writerow(row.split(', ', 1))


NAME='corpus_creator'
prefix='corpus'

if __name__ == "__main__":
    p = argparse.ArgumentParser(NAME)

    p.add_argument("DIR", default=None,
                   action="store", help="Inpunt corpus files")

    p.add_argument('-o', '--output', default=sys.stdout)

    opts = p.parse_args()
    retrive(opts.DIR)
    corpus_writer(opts.output)