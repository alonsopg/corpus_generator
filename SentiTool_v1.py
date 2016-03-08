#!/usr/bin/env python
# -*- coding: utf-8

#Todo agregar el corpus generator con las otras opciones

import glob, os, csv, argparse, sys, numpy
from sklearn.cross_validation import KFold
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn import cross_validation
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.metrics import precision_score, recall_score, confusion_matrix, classification_report, accuracy_score, f1_score

#para ver los arreglos completos usar:
def fullprint(*args, **kwargs):
  from pprint import pprint
  import numpy
  opt = numpy.get_printoptions()
  numpy.set_printoptions(threshold='nan')
  pprint(*args, **kwargs)
  numpy.set_printoptions(**opt)

def perform_classification(corpus, labels):
    df_content = pd.read_csv(corpus).dropna()
    df_labels = pd.read_csv(labels).dropna()
    #Vectorizer:
    count_vect = CountVectorizer()
    #vectorizamos el texto
    X = count_vect.fit_transform(df_content['content'].values)
    y = df_labels['label'].values

    #revisamos el corpus
    print '\n corpus \n',X.toarray()
    #revisamos las labels
    print '\n etiquetas \n',y
    #revisamos la dimension del numero de columnas
    num_columnas_del_df = df_labels.shape[0]
    print '\n count col\n',num_columnas_del_df

    #Hacemos validacion cruzada
    kf = KFold(n=num_columnas_del_df, n_folds=10, shuffle=True, random_state=False)
    print '\n\n........Cross validating........\n\n'
    for train_index, test_index in kf:
        print "\nEntrenó con las opiniones que tienen como indice:\n", train_index, \
        "\nProbó con las opiniones que tiene como indice:\n", test_index
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

    y_=[ ]
    prediction_=[ ]


    clf = SVC(kernel='linear', C=1).fit(X_train, y_train)

    #Cross validation metrics, checar esto
    acc_scores = cross_validation.cross_val_score(clf, X_train, y_train, cv=10)
    # f1_scores = cross_validation.cross_val_score(clf, X_train, y_train, cv=10,average='f1_weighted')
    # recall_scores = cross_validation.cross_val_score(clf, X_train, y_train, cv=10,average='recall')

    print '\nacc_scores como arreglo:\n',acc_scores
    # print '\nacc_scores como arreglo:\n',f1_scores
    # print '\nacc_scores como arreglo:\n',recall_scores

    print("\nAccuracy: %0.2f (+/- %0.2f)" % (acc_scores.mean(), acc_scores.std() * 2))

    prediction = clf.predict(X_test)
    y_.extend(y_test)
    prediction_.extend(prediction)


    #Esto se refiere a las clases:
    target_names = [set(y)]
    print '\n categorias o etiquetas que contiene el dataset:',target_names

    # Calculando desempeño
    #Hay que ver lo del average
    print 'Accuracy              :', accuracy_score(y_, prediction_)
    print 'Precision             :', precision_score(y_, prediction_,average='weighted')
    print 'Recall                :', recall_score(y_, prediction_,average='weighted')
    print 'F-score               :', f1_score(y_, prediction_,average='weighted')
    print '\nClasification report:\n', classification_report(y_,prediction_)
    print '\nConfussion matrix   :\n',confusion_matrix(y_, prediction_)


NAME='senti_tool'
prefix='sentitool'

if __name__ == '__main__':
    #corpus dos...


    p = argparse.ArgumentParser(NAME)

    p.add_argument('-d', '--input_data', default=sys.stdin)
    p.add_argument('-l', '--input_labels', default=sys.stdin)

    opts = p.parse_args()
    # retrive(opts.DIR)
    # corpus_writer(opts.output)


    # data_2 = '/Users/user/PycharmProjects/SentimentAnalysisNegCues/CORPORA/corregidos/positivos/sust_adj.csv'
    # labels_2= '/Users/user/PycharmProjects/SentimentAnalysisNegCues/CORPORA/corregidos/positivos/sust_adj.csv'

    #Recibe (datos, etiquetas)
    perform_classification(opts.input_data, opts.input_labels)