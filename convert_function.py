

import csv
import math
import pandas as pd
import os
import sys
sys.dont_write_bytecode = True

def calling(a,b):


    with open('Output.csv', mode='w') as f:
        csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['Index', 'Name'])

        for i in range(len(b)):
            curr = b.iloc[i]
            filename = curr['Text']
            
            
            
            # if b[b['Text'].str.match(filename)]:
            #   print(filename,file)
            list1 = ['FAQ', 'Fruits', 'Vegetables', 'Grains', 'Protein Foods', 'Dairy', 'Healthy/Beauty', 'Cooking', 'Recipes', 'Beverage']

            for l in range(10):
                    
                name = list1[l]
                # print(name)
                a.dropna()   
                for j in range(len(a[name])):
                
                    rd = a.iloc[j]

                    file = rd[name]

                    
                    if file == '' or (isinstance(file, float) and  math.isnan(file)):
                            continue
                    else:

                        
                        if file in filename:
                        # print(i+2, list1[l])
                            csv_writer.writerow([i+2,list1[l]])



    ########## intermediate output #################
    df = pd.read_csv('Output.csv')
    df = df.groupby(["Index"])["Name"].agg(lambda x: ','.join(x.astype(str)))


    ######### Final output saved in the file_output.csv file###########
    df.to_csv('file_output.csv', header=False, index=True) 


    exam = pd.read_csv('file_output.csv')


    from collections import Counter

    words = ['FAQ', 'Fruits', 'Vegetables', 'Grains', 'Protein Foods', 'Dairy', 'Healthy/Beauty', 'Cooking', 'Recipes', 'Beverage']


    import operator



    with open('Food_output.csv', mode='w') as f:
        csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['Index', 'Name'])

        for i in range(len(exam)):
            curr = exam.iloc[i]
            filename = curr[1]
            words_list = (filename.split(','))

            count_l = [1, 8, 9, 7, 11, 10, 2, 6, 5, 4]

            cnt1 = cnt2 = cnt3 = cnt4 = cnt5 = cnt6 = cnt7 = cnt8 = cnt9 = cnt10 = 0
            for l in range(len(words_list)):
                        
                if words_list[l] == words[0]:
                    cnt1 = cnt1 + 1
                if words_list[l] == words[1]:
                    cnt2 = cnt2 + 1
                if words_list[l] == words[2]:
                    cnt3 = cnt3 + 1
                if words_list[l] == words[3]:
                    cnt4 = cnt4 + 1
                if words_list[l] == words[4]:
                    cnt5 = cnt5 + 1
                if words_list[l] == words[5]:
                    cnt6 = cnt6 + 1
                if words_list[l] == words[6]:
                    cnt7 = cnt7 + 1
                if words_list[l] == words[7]:
                    cnt8 = cnt8 + 1
                if words_list[l] == words[8]:
                    cnt9 = cnt9 + 1
                if words_list[l] == words[9]:
                    cnt10 = cnt10 + 1
                
            list_f = [cnt1, cnt2, cnt3, cnt4, cnt5, cnt6, cnt7, cnt8, cnt9, cnt10]
            
            final = [a*b for a,b in zip(count_l,list_f)]

            
            index, value = max(enumerate(final), key=operator.itemgetter(1))
            
            wrd = words[index]
            csv_writer.writerow([i+2,words[index]])
            # print(word_list)
            # words_to_count = (word for word in word_list if word[:1].isupper())
            # c = Counter(words_to_count)
            # print c.most_common(1)
            # for k in range(len(word_list))
            #     list1 = ['FAQ', 'Fruits', 'Vegetables', 'Grains', 'Protein Foods', 'Dairy', 'Healthy/Beauty', 'Cooking', 'Recipes', 'Beverage']

    os.remove("Output.csv")
    os.remove("file_output.csv")
    

