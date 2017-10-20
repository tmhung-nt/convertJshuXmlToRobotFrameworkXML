'''
Created on Oct 12, 2017

@author: Tu Pham
'''
import xml.etree.cElementTree as ET

from datetime import datetime

def sum_of_tag():
    tree = ET.ElementTree(file='test1.xml')
    root = tree.getroot()
    counter = 0
    for child_of_root in root:
        child_of_root.tag
        counter += 1
    return counter

def get_testcase_name():
    tag_num = int(sum_of_tag())
    tree = ET.ElementTree(file='test.xml')
    root = tree.getroot()
    for i in range (0,tag_num):
        a = ((root[i].attrib)['name'])
        context = "testcase[@name=" + "\"" + a + "\"" + "]"
        print (context)
    for elem in tree.iterfind(context):
        return ((elem[0].text))



#def temp_sce_name():
#tag_num = int(sum_of_tag())
#tree = ET.ElementTree(file='test1.xml')
#root = tree.getroot()
#for i in range (0,tag_num):
#    a = ((root[i].attrib)['name'])
#    print (a)
#    file = open("temp.txt","a+")
#    c = file.write(a+'\n')
 
#file = open("temp.txt")
#for lines in file:
#    print (lines.rstrip('\n')) 
#lines = [line.rstrip('\n') for line in open('temp.txt')]
#print (len(lines))        
#print (temp_sce_name())        
        
tree = ET.ElementTree(file='test.xml')  
root = tree.getroot()
#for elem in tree.iter(tag='failure'):
#    print (root.attrib,elem.tag,elem.attrib)

for elem in tree.iterfind('testcase[@name="getConfigTest"]'):
        print ((elem[0].text))
#a = (get_testcase_name())
#print (a)



