import sys
import xml.dom.minidom
from xml.dom.minidom import parse

#Mostly, Cloudy, Pleasent, Beautiful, Patchy, Sunny
weatherlst = ['°' , 'RealFeel®', '%', 'Mostly', 'Sunny', 'Cloudy', 'Patchy', 'Storm', 'Snow', 'Rain']
lst = []
lst_final = []
#testlst = []
document = xml.dom.minidom.parse(sys.argv[1])
elements = document.getElementsByTagName('body')
counter = 0

for div1 in elements[0].getElementsByTagName('div'):
    for div2 in div1.getElementsByTagName('div'):
        for div3 in div2.getElementsByTagName('div'):
            for div4 in div3.getElementsByTagName('div'):
                for div5 in div4.getElementsByTagName('div'):
                    for div6 in div5.getElementsByTagName('div'):
                        for node in div6.childNodes:
                            if node.nodeType == node.TEXT_NODE:
                                x = str(node.nodeValue)
                                for i in weatherlst:
                                    if i in x:
                                        if x not in lst:
                                            lst.append(x)#data.append(node.nodeValue)    
                                            #continue
                           
y = lst                  
print(y)
print('\n')
try:
                               
    lst_final.append(lst[0])
    lst_final.append(lst[1])
    lst_final.append(lst[3])
    lst_final.append(lst[5])
    

    inf = open("location.txt", "r")
    location = inf.read()
    inf.close()
    
    
    
    st = "currently in " + location + " it is " + lst_final[0][-3:-1] + " degrees real feel " + lst_final[1][-3:-1] + " degrees and " + lst_final[2] + " with " + lst_final[3][0:2] + " percent humidity, "    
except:
    st = "Sir, you have my sinseerest apologies, as i am currently unable to obtain the weather"


print(str(lst_final)+'\n')

outf = open("morning_main2.txt", "w+")
outf.write(str(st))
outf.close()
