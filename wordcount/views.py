import operator

from django.http import HttpResponse
from django.shortcuts import render
import operator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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

    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    plt.plot(t, s)

    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.savefig("C:/Users/EW682YF/PycharmProjects/wordcount-project/templates/test.png")

    # Plot Over(Return to HTML Page) *********************************************************************
    return render(request, 'count.html',
                  {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords, })


# Call to About US HTML PAge
def about(request):
    return render(request, 'about.html')
