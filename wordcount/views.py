import operator

from django.http import HttpResponse
from django.shortcuts import render
import operator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO


# def homepage(request):
# return HttpResponse('Hello World')

def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)
    wordlist = fulltext.split()

    # Now we will check the most repeating words
    worddictionary = {}

    for word in wordlist:  # counting the repetition of words
        if word in worddictionary:
            # Increase the counting
            worddictionary[word] += 1  # If the word is already present in this dictionary then increment the count by 1
        else:
            worddictionary[word] = 1  # #If the word is not present in this dictionary then assign 1 as value of that
            # word in dictionary

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    # To show a Matplotlib Plot *************************************************************************
    # initialize list of lists
    data = [['tom', 10], ['nick', 15], ['juli', 14]]

    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns=['Name', 'Age'])

    print(df.head())

    fig = plt.figure()
    menstd = (2, 3, 4, 1, 2)
    menstd1 = (2, 3, 4, 1, 2)
    plt.bar(menstd1, menstd)
    # plot sth

    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    html = '<img src=\'data:image/png;base64,{}\'>'.format(encoded)
    # Plot Over(Return to HTML Page) *********************************************************************
    return render(request, 'count.html',
                  {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords, 'htmlgraph': html})


# Call to About US HTML PAge
def about(request):
    return render(request, 'about.html')
