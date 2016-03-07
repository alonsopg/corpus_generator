# Corpus generator
This script transforms a directory full of .txt files (typically opinions) to a `.csv` file. This could be useful for sentiment analysis tasks.
**usage**
In the terminal just:

`$python corpus_creator_v1.py /directory/of/opinions`

It will generate a .csv file where each instance will be a line, followed by it's id or name. For instance:
```
id|content
opinion_1.txt|I am an amateur photographer and own three DSLR ...
opinion_2.txt|This my second Sony Digital Camera. The first ...
opinion_3.txt|"'I ordered this camera with high hopes ...
```

This is the version 1, I will fix some bugs later...

