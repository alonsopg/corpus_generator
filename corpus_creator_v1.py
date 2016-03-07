#ToDo opcion para especificar donde colocar el archivo de salida o corpus
#ToDo opcion para cambiar a txt utf8 todos los archivos del directorio

import glob, os, csv, argparse

def retrive(directory):
    for filename in sorted(glob.glob(os.path.join(directory, '*.txt'))):
        with open(filename, 'r') as f:
            important_stuff = f.read().splitlines()
            oneline = [''.join(important_stuff)]
            yield filename.split('/')[-1] + ', ' +str(oneline).strip('[]"')

NAME='ef_ngrams'
prefix='1grams'

if __name__ == "__main__":
    p = argparse.ArgumentParser(NAME)

    p.add_argument("DIR",default=None,
        action="store", help="Directory with corpus with json")
    opts = p.parse_args()
    test = tuple(retrive(opts.DIR))
    with open('/Users/user/Downloads/corpus.csv','w') as out:
        csv_out=csv.writer(out, delimiter='|')
        csv_out.writerow(['id','content'])
        for row in test:
            csv_out.writerow(row.split(', ', 1))
