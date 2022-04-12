"""
Language Modeling Project
Name:
Roll No:
"""

import language_tests as test
#from collections import Counter

project = "Language" # don't edit this

### WEEK 1 ###

'''
loadBook(filename)
#1 [Check6-1]
Parameters: str
Returns: 2D list of strs
'''
def loadBook(filename):
    list=[]
    file=open(filename,"r")
    content=file.read()
    sentences=content.split("\n")
    #print(len(content_split))
    for i in range(len(sentences)):
        #for j in range(len(content_split[i])):
        x=sentences[i].split()
        if x: #here it returns a boolen value,only when the content is present, it appends  
            list.append(x)
    return list



'''
getCorpusLength(corpus)
#2 [Check6-1]
Parameters: 2D list of strs
Returns: int
'''
def getCorpusLength(corpus):
    sum=0
    # count=0
    # for i in range (len(corpus)):
    #     count+=len(corpus[i])
    # return count 
    dict={}
    #print(len(corpus))
    for i in range(len(corpus)):
        for j in range(len(corpus[i])):
            if corpus[i][j] not in dict:
                dict[corpus[i][j]]=1
            else:
                dict[corpus[i][j]]+=1
    s=dict.values()
    for k in s:
        sum=sum+k
    #print(sum)
    return sum


'''
buildVocabulary(corpus)
#3 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def buildVocabulary(corpus):
    dict={}
    list=[]
    for i in range(len(corpus)):
        for j in range(len(corpus[i])):
            if corpus[i][j] not in dict:
                dict[corpus[i][j]]=1
            else:
                dict[corpus[i][j]]+=1
    s=dict.keys()
    for k in s:
        list.append(k)
    #print(list)
    return list 


'''
countUnigrams(corpus)
#4 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countUnigrams(corpus):
    dict={}
    for i in range(len(corpus)):
        for j in range(len(corpus[i])):
            if corpus[i][j] not in dict:
                dict[corpus[i][j]]=1
            else:
                dict[corpus[i][j]]+=1
    return dict


'''
getStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def getStartWords(corpus):
    list=[]
    result=[]
    dict={}
    for i in range(len(corpus)):
        #for j in range(len(corpus[i])):
        list.append(corpus[i][0])
    for i in range(len(list)):
        if list[i] not in dict:
            dict[list[i]]=1
        else:
            dict[list[i]]+=1
    #print(dict)
    s=dict.keys()
    for k in s:
        result.append(k)
    #print(list)
    return result


'''
countStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countStartWords(corpus):
    list=[]
    dict={}
    for i in range(len(corpus)):
        #for j in range(len(corpus[i])):
        list.append(corpus[i][0])
    for i in range(len(list)):
        if list[i] not in dict:
            dict[list[i]]=1
        else:
            dict[list[i]]+=1
    #print(dict)
    return dict


'''
countBigrams(corpus)
#6 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to (dicts mapping strs to ints)
'''
def countBigrams(corpus):
    #print(corpus)
    dict={}
    for i in range(len(corpus)):
        for j in range(0,len(corpus[i])-1):
            #print(corpus[i][j],corpus[i][j+1])
            if corpus[i][j] not in dict:
                dict[corpus[i][j]]={}
                dict[corpus[i][j]][corpus[i][j+1]]=1
            else:
                if corpus[i][j+1] not in dict[corpus[i][j]]:
                    dict[corpus[i][j]][corpus[i][j+1]]=1
                else:
                    dict[corpus[i][j]][corpus[i][j+1]]+=1
                #dict[corpus[i][j]][corpus[i][j+1]]+=1
        #print(dict)

    #print(dict)
    return dict


### WEEK 2 ###

'''
buildUniformProbs(unigrams)
#1 [Check6-2]
Parameters: list of strs
Returns: list of floats
'''
def buildUniformProbs(unigrams):
    #dict={}
    list=[]
    #print(len(unigrams))
    for i in range(len(unigrams)):
        list.append(1/len(unigrams))
    return list 


    #    if unigrams[i] not in dict:
    #        dict[unigrams[i]]=1
    #s=dict.values()
    #for k in s:
    #    print(k/len(unigrams))


    return


'''
buildUnigramProbs(unigrams, unigramCounts, totalCount)
#2 [Check6-2]
Parameters: list of strs ; dict mapping strs to ints ; int
Returns: list of floats
'''
def buildUnigramProbs(unigrams, unigramCounts, totalCount):
    # list=[]
    # list1=[]
    # s=unigramCounts.values()
    # for k in s:
    #     list1.append(k)
    # #print(len(s))
    # for i in range(len(list1)):
    #     list.append(list1[i]/totalCount)
    # #print(list)
    # return list
    list=[]
    for i in unigrams:
        if i in unigramCounts:
            list.append(unigramCounts[i]/totalCount)
        else:
            list.append(0)
    return list



'''
buildBigramProbs(unigramCounts, bigramCounts)
#3 [Check6-2]
Parameters: dict mapping strs to ints ; dict mapping strs to (dicts mapping strs to ints)
Returns: dict mapping strs to (dicts mapping strs to (lists of values))
'''
def buildBigramProbs(unigramCounts, bigramCounts):
    dict={}
    for prevWord in bigramCounts:
        #print(bigramCounts[prevWord])
        keys_list=[]
        probs_list=[]
        for key,value in bigramCounts[prevWord].items():
            keys_list.append(key)
            #print(keys_list)
            #probs_list.append(value)
        #print(probs_list)
            probs_list.append(value/unigramCounts[prevWord])
            #print(keys_list,probs_list)
            temporary={}
            temporary["words"]=keys_list
            temporary["probs"]=probs_list
            #print(temporary)
        dict[prevWord]=temporary
    #print(dict)
    return dict



'''
getTopWords(count, words, probs, ignoreList)
#4 [Check6-2]
Parameters: int ; list of strs ; list of floats ; list of strs
Returns: dict mapping strs to floats
'''
def getTopWords(count, words, probs, ignoreList):
    dict={}
    dict1={}
    for i in range(len(words)):
        if words[i] not in ignoreList:
            dict[words[i]]=probs[i]
    #print(dict)
    #x=Counter(dict)
    sort=sorted(dict.items(),key=lambda k: -k[1])
    #print(sort)-it is a list
    i=0
    while(i<count):
        #if sort[i][0] not in ignoreList:
        dict1[sort[i][0]]=sort[i][1]
        i=i+1
    #print(dict1)
    return dict1 

#assert(getTopWords(2, [ "hello", "world", "again"], [2/5, 2/5, 1/5], []) == \
#        { "hello" : 2/5, "world" : 2/5 })
'''
generateTextFromUnigrams(count, words, probs)
#5 [Check6-2]
Parameters: int ; list of strs ; list of floats
Returns: str
'''
from random import choices
def generateTextFromUnigrams(count, words, probs):
    sentence=""
    i=0
    while(i<count):
        s=choices(words,weights=probs)
        sentence=sentence+" "+s[0]
        i=i+1
    #print(sentence)
    #print(len(sentence))
    return sentence


'''
generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs)
#6 [Check6-2]
Parameters: int ; list of strs ; list of floats ; dict mapping strs to (dicts mapping strs to (lists of values))
Returns: str
'''
def generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs):
    return


### WEEK 3 ###

ignore = [ ",", ".", "?", "'", '"', "-", "!", ":", ";", "by", "around", "over",
           "a", "on", "be", "in", "the", "is", "on", "and", "to", "of", "it",
           "as", "an", "but", "at", "if", "so", "was", "were", "for", "this",
           "that", "onto", "from", "not", "into" ]

'''
graphTop50Words(corpus)
#3 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTop50Words(corpus):
    return


'''
graphTopStartWords(corpus)
#4 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTopStartWords(corpus):
    return


'''
graphTopNextWords(corpus, word)
#5 [Hw6]
Parameters: 2D list of strs ; str
Returns: None
'''
def graphTopNextWords(corpus, word):
    return


'''
setupChartData(corpus1, corpus2, topWordCount)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int
Returns: dict mapping strs to (lists of values)
'''
def setupChartData(corpus1, corpus2, topWordCount):
    return


'''
graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; str ; 2D list of strs ; str ; int ; str
Returns: None
'''
def graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title):
    return


'''
graphTopWordsInScatterplot(corpus1, corpus2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int ; str
Returns: None
'''
def graphTopWordsInScatterplot(corpus1, corpus2, numWords, title):
    return


### WEEK 3 PROVIDED CODE ###

"""
Expects a dictionary of words as keys with probabilities as values, and a title
Plots the words on the x axis, probabilities as the y axis and puts a title on top.
"""
def barPlot(dict, title):
    import matplotlib.pyplot as plt

    names = []
    values = []
    for k in dict:
        names.append(k)
        values.append(dict[k])

    plt.bar(names, values)

    plt.xticks(rotation='vertical')
    plt.title(title)

    plt.show()

"""
Expects 3 lists - one of x values, and two of values such that the index of a name
corresponds to a value at the same index in both lists. Category1 and Category2
are the labels for the different colors in the graph. For example, you may use
it to graph two categories of probabilities side by side to look at the differences.
"""
def sideBySideBarPlots(xValues, values1, values2, category1, category2, title):
    import matplotlib.pyplot as plt

    w = 0.35  # the width of the bars

    plt.bar(xValues, values1, width=-w, align='edge', label=category1)
    plt.bar(xValues, values2, width= w, align='edge', label=category2)

    plt.xticks(rotation="vertical")
    plt.legend()
    plt.title(title)

    plt.show()

"""
Expects two lists of probabilities and a list of labels (words) all the same length
and plots the probabilities of x and y, labels each point, and puts a title on top.
Note that this limits the graph to go from 0x0 to 0.02 x 0.02.
"""
def scatterPlot(xs, ys, labels, title):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()

    plt.scatter(xs, ys)

    # make labels for the points
    for i in range(len(labels)):
        plt.annotate(labels[i], # this is the text
                    (xs[i], ys[i]), # this is the point to label
                    textcoords="offset points", # how to position the text
                    xytext=(0, 10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

    plt.title(title)
    plt.xlim(0, 0.02)
    plt.ylim(0, 0.02)

    # a bit of advanced code to draw a y=x line
    ax.plot([0, 1], [0, 1], color='black', transform=ax.transAxes)

    plt.show()


### RUN CODE ###

# This code runs the test cases to check your work

if __name__ == "__main__":
    print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    test.week1Tests()
    print("\n" + "#"*15 + " WEEK 1 OUTPUT " + "#" * 15 + "\n")
    test.runWeek1()

    ## Uncomment these for Week 2 ##

    print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    test.week2Tests()
    print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
    test.runWeek2()


    ## Uncomment these for Week 3 ##
"""
    print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    test.runWeek3()
"""