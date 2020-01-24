import csv
import math



#this converts all numbers in the csv to floats and puts them in a list
def csv_to_list(csv_file):
    fulllist = list(csv_file)
    for list1 in fulllist:
        for value in list1:
            if value in "0123456789":
                fulllist[fulllist.index(list1)][list1.index(value)] = float(value)
    return fulllist

#for a matrix this function gives the vector length for each document as a dictionary
def list_to_vector(list):
    vector_dict = {}

    for x in range(1,len(list[0])):
        sum_of_squares = 0

        for y in range(1,len(list)):
            sum_of_squares += list[y][x]**2

        vector_dict[list[0][x]] = math.sqrt(sum_of_squares)
    return(vector_dict)

# for a query return the cosine similarity
def query_handeling(list,query):
    dict = {}
    for x in range(1, len(list[0])):
        product = 0
        for y in range(1, len(list)):
            for term in query:
                if term == list[y][0]:
                    product += list[y][x]
        vectorlengthdict = list_to_vector(list)
        vectorlength = vectorlengthdict[list[0][x]]
        cosinesim = product/(vectorlength*math.sqrt(len(query)))
        dict[list[0][x]] = cosinesim

    return(dict)



#This reads the csv file and makes it into a list
csv_file = csv.reader(open("ontwikkelmateriaal/recepten.csv"),delimiter = ";")
recepten_list = csv_to_list(csv_file)

query = ["appel","deeg"]
tempdict = query_handeling(recepten_list,query)
unranked = []
for x in tempdict:
    unranked.append([x,tempdict[x]])

ranked = sorted(unranked, key=lambda score : score[1], reverse=True)
print(ranked)


def add_file_to_termweightmatrix(filename,termweightmatrix):
    wordcountdict = {}
    text = open(filename,"r")
    text = text.read()
    text = text.split()
    for word in text:
        if word in wordcountdict:
            wordcountdict[word] += 1
        else:
            wordcountdict[word] = 1
    print(wordcountdict)

termweightmatrix=[]
test = add_file_to_termweightmatrix("ontwikkelmateriaal/test1.txt",termweightmatrix)
print(test)


