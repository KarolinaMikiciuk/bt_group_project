import pandas as pd
from nltk import tokenize
import nltk
nltk.download('punkt')


from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


def readcsv(filepath, start=None, stop=None):
    """reads in a csv file, and outputs a pandas dataframe"""
    if start is not None and stop is not None:
        skiprows = start
        nrows = stop - skiprows
    else:
        skiprows = None
        nrows = None
    return pd.read_csv(filepath, skiprows=range(1, skiprows), nrows=nrows)

def readtxt(txtpath):
    #reading from a text file
    with open(txtpath, 'r') as file:
        text = file.read()
    return text

def df_retrieve_content(df):
    content = df.content
    text = ''
    for entry in content:
        text += str(entry)
    return text


def wordfrequency(text):
    tokens = tokenize.word_tokenize(text)
    wordcloud = WordCloud().generate(text)
    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig("bt_wordcloud.png", dpi=400)


def iterative_read_csv(path, chunksize=500):
    # Get number of lines in file
    with open(path, "r", encoding="utf-8") as fh:
        count = 0
        for line in fh:
            count += 1
    text = ""
    for i in range(count // chunksize):
        start = (i * chunksize) + 1
        stop = (i + 1) * chunksize
        text += df_retrieve_content(readcsv(path, start=start, stop=stop))

    text += df_retrieve_content(readcsv(path, start=(count // chunksize) * chunksize, stop=count))
    return text


if __name__ == '__main__':
    text = ''
    for i in range(1, 81):
        file = '../data/data_file_{}.csv'.format(i)
        text += iterative_read_csv(file)
    wordfrequency(text)
