import sys
import xml.dom.minidom
from xml.dom.minidom import parse

lst = []
lst_final = []
document = xml.dom.minidom.parse(sys.argv[1])
elements = document.getElementsByTagName('body')
counter = 0

for div1 in elements[0].getElementsByTagName('div'):
    for div2 in div1.getElementsByTagName('div'):
        for div3 in div2.getElementsByTagName('div'):
            for div4 in div3.getElementsByTagName('div'):
                for div5 in div4.getElementsByTagName('div'):
                    for div6 in div5.getElementsByTagName('div'):
                        for div7 in div6.getElementsByTagName('div'):
                            for div8 in div7.getElementsByTagName('div'):
                                for div9 in div8.getElementsByTagName('div'):
                                    for div11 in div9.getElementsByTagName('div'):
                                        for p1 in div11.getElementsByTagName('p'):
                                            for node in p1.childNodes:
                                                if node.nodeType == node.TEXT_NODE:
                                                    lst.append(node.nodeValue)#data.append(node.nodeValue)
                                                    #continue
                                                    
                                for node in div8.childNodes:
                                    if node.nodeType == node.TEXT_NODE:
                                        lst.append(node.nodeValue)#data.append(node.nodeValue)
                                        #continue
                                        
                        for div12 in div6.getElementsByTagName('div'):
                            for div13 in div12.getElementsByTagName('div'):
                                for div14 in div13.getElementsByTagName('div'):
                                    for p2 in div14.getElementsByTagName('p'):
                                         for node in p2.childNodes:
                                             if node.nodeType == node.TEXT_NODE:
                                                 lst.append(node.nodeValue)#data.append(node.nodeValue)
                                                 #continue
try:                                   
    lst_final.append(lst[4340])
    lst_final.append(lst[4342]) #" degrees real feel in the shade " + lst_final[2][-8:-6] +
    lst_final.append(lst[4343])
    lst_final.append(lst[4357])
    lst_final.append(lst[4421])

    '''
    x = 0
    for i in lst:
        if 'Humidity: 89%' in i:
            if 'to partly cloudy' not in i:
                x = lst.index(i)
    print(str(x) + '\n')
    '''

    inf = open("location.txt", "r")
    location = inf.read()
    inf.close()

    st = "currently in " + location + " it is " + lst_final[0][-3:-1] + " degrees real feel " + lst_final[1][-7:-5] + " degrees and " + lst_final[3] + " with " + lst_final[4][-6:-4] + " percent humidity, "    
except:
    st = "Sir, you have my sinseerest apologies, as i am currently unable to obtain the weather"



outf = open("morning_main2.txt", "w+")
outf.write(str(st))
outf.close()