import pandas as pd
import csv
import math
import os
import sys
sys.dont_write_bytecode = True

def calling2(b):
    ll = []
    str1 = []
    l2 = []
    str2 = []
    for i in range(len(b)):
        
          curr = b.iloc[i]
          filename = curr['Text']
          
          list1 = (filename.split('-'))
        #   df = pd.read_csv('output_one.csv')
        
          for j in range(len(list1)):
            if 'UPC' in list1[j]:
                val = curr[0]
                val1 = val.item()

                if val1 in ll:
                    continue
                else:
                    ll.append(val1)
                  
                    str1.append(list1[j])

    sd = pd.read_csv('CB All Brand Complaints Weekly_280.csv')
    list2 = ll
    count = 0
    list3 = []

    with open('UPC.csv', mode='w') as f:
        csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['Index', 'UPC_final'])
        for i in range(len(sd)):
            if i in ll:
                val = i
                # print(str1[count])
                str12 = str1[count]
                str12 = str12.replace('UPC#:', '')
                str12 = str12.replace(' ', '')
                
                # print(i,str1[count])
                count = count+1
                # print(k,list2[k])
            else:
                str121 = sd.iloc[i]
                str12 = str121['UPC']
                
                val = i
            
            csv_writer.writerow([val,str12])

    




def calling3(b):
    ll = []
    str1 = []
    for i in range(len(b)):
        
          curr = b.iloc[i]
          filename = curr['Text']
          
          list1 = (filename.split('-'))
          
          for j in range(len(list1)):
            
              if 'Problem with product' in list1[j]:
                  val = curr[0]
                  val1 = val.item()
                  if val1 in ll:
                      continue
                  else:
                      
                      ll.append(val1)
                      str1.append(list1[j])

    str2 = []
    for l in range(len(str1)):
        filename = str1[l].split(':')
        str2.append(filename[1])
    
    count = 0
    sd = pd.read_csv('CB All Brand Complaints Weekly_280.csv')
    with open('Text.csv', mode='w') as f:
        csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['Index', 'Text_final'])
        for i in range(len(sd)):
            if i in ll:
                val = i
                str12 = str2[count]
                # print(i,str1[count])
                count = count+1
                # print(k,list2[k])
            else:
                str121 = sd.iloc[i]
                str12 = str121['Text']
                val = i

            csv_writer.writerow([val,str12])
    

    

    a1 = pd.read_csv('UPC.csv')
    a2 = pd.read_csv('Text.csv')
    merged = a1.merge(a2)
    merged.to_csv("out1.csv", index=False)

    a3 = pd.read_csv('out1.csv')
    
    
    # sd['UPC'] = a1['UPC_final'].values
    # sd['Text'] = a2['Text_final'].values
    # print(sd['UPC'])
    # sd = sd.drop('UPC', 1)
    # print(sd['UPC'])

    df3 = pd.concat([sd, a3], axis=1)
    df3.drop('Index', axis=1)
    df3.to_csv('text_cleaning_output.csv', index=False)


    df12 = pd.read_csv('text_cleaning_output.csv')

    df12.drop('UPC', axis=1)
    df12.drop('Text', axis=1)
    df12 = df12[['Supplier', 'Portfolio','Sub-Category','UPC_final','Brand','Product', 'Code', 'Item Desc (text)', 'Reason', 'Reason Attribute', 'Text_final', 'Brand', 'Store', 'Rcv Date', 'Case ID']]

    # print(df12)
    df12.to_csv('text_final_output.csv', index=False)
    
    os.remove('Text.csv')
    os.remove('text_cleaning_output.csv')
    os.remove('out1.csv')
    os.remove('UPC.csv')
    
    