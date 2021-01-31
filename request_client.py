import requests
import lxml.html as lh
import pandas as pd


##
##r = requests.get()
##print('__dict__')
##
######
##
##for key in r.__dict__.keys():
##    print(key)
##
##    
##print('/n/n/n')
##
##
##print('dir')
##print(dir(r))
##
##
##print('/n/n/n')
##
##
##
##print(r.text)
##
##print(r.headers)


url='https://www.reddit.com/r/wallstreetbets/'
#Create a handle, page, to handle the contents of the website
page = requests.get(url)
#Store the contents of the website under doc

#print(page.__dict__)

print(dir(page))

print(page.text)

#doc = lh.fromstring(page.content)
#Parse data that are stored between <tr>..</tr> of HTML
#tr_elements = doc.xpath('//tr')

##print(tr_elements)
##
##
###Create empty list
##col=[]
##i=0
###For each row, store each first element (header) and an empty list
##for t in tr_elements[0]:
##    i+=1
##    name=t.text_content()
##    #print '%d:"%s"'%(i,name)
##    col.append((name,[]))
##
##
###Since out first row is the header, data is stored on the second row onwards
##for j in range(1,len(tr_elements)):
##    #T is our j'th row
##    T=tr_elements[j]
##    
##    #If row is not of size 10, the //tr data is not from our table 
##    if len(T)!=10:
##        break
##    
##    #i is the index of our column
##    i=0
##    
##    #Iterate through each element of the row
##    for t in T.iterchildren():
##        data=t.text_content() 
##        #Check if row is empty
##        if i>0:
##        #Convert any numerical value to integers
##            try:
##                data=int(data)
##            except:
##                pass
##        #Append the data to the empty list of the i'th column
##        col[i][1].append(data)
##        #Increment i for the next column
##        i+=1
##
##
##


##
