import pandas as pd
import numpy as np
import requests
import csv
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import operator
import collections
import os


#/Simple Webscraping using BeautifulSoup/#
def soupify(textURL, numPara):
    directory0 = '/Users/joelaoto/Documents/scifindCHL'
    soup = BeautifulSoup(open(textURL), features="lxml")#from beautiful soup doc
    para = ""
    i = 0
    for i in range(numPara):
        para += soup.find_all('p')[i].get_text()

    return para
#/simple function used to count the words in each summary and create a dictionary
#/for each summary. simple counter from w3 schools
def para_count(str):
    count = dict()
    words = str.lower()
    wordz = words.split()

    for word in wordz:
        word.lower()
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

#/function to remove words with a single use, new dictionary only has words used
#/more than once, then sorts the dictionary from least uses to greatest.
def cleanDict(dictionary):
    new_dict = dict()
    for key,value in dictionary.items():
        if value > 1:
            new_dict[key] = value

    sorted_new = sorted(new_dict.items(),key=operator.itemgetter(1))
    sorted_dict = collections.OrderedDict(sorted_new)

    return sorted_dict

#/returns the words not used in the other summary
def anDict(dict1, dict2):
    new_dict = dict()
    for k1, v1 in dict1.items():
        for k2, v2 in dict2.items():
            if not k2 in dict1:
                new_dict[k2] = v2
    return new_dict

#/main function, used to call other functions and plot two figures of comparing
#bar graphs.
def main():
    x = dict()
    y = dict()
    b1_dict = dict()
    b2_dict = dict()
    uniB1_dict = dict()
    uniB2_dict = dict()

    book1 = soupify("Hp1SPARK.html", 4) #book 1 ch1 summary
    book2 = soupify("Hp2SPARK.html", 4) #book 2 ch1 summary

    x = para_count(book1)
    y = para_count(book2)

    b1_dict = cleanDict(x)
    b2_dict = cleanDict(y)

    fig = plt.figure(1)
    plt.subplot(211)
    plt.bar(range(len(b1_dict)), list(b1_dict.values()), align ='center')
    plt.xticks(range(len(b1_dict)), list(b1_dict.keys()), rotation=30, fontsize = 9)

    plt.subplot(212)
    plt.bar(range(len(b2_dict)), list(b2_dict.values()), align ='center')
    plt.xticks(range(len(b2_dict)), list(b2_dict.keys()), rotation=30, fontsize = 9)

    uniB1_dict = anDict(b1_dict, b2_dict)
    uniB2_dict = anDict(b2_dict, b1_dict)

    fig2 = plt.figure(2)
    plt.subplot(211)
    plt.bar(range(len(uniB1_dict)), list(uniB1_dict.values()), align ='center')
    plt.xticks(range(len(uniB1_dict)), list(uniB1_dict.keys()), rotation=30, fontsize = 9)

    plt.subplot(212)
    plt.bar(range(len(uniB2_dict)), list(uniB2_dict.values()), align ='center')
    plt.xticks(range(len(uniB2_dict)), list(uniB2_dict.keys()), rotation=30, fontsize = 9)

    plt.show()

#/calls the main funtion/#
main()
