'''
Created on Oct 18, 2017

@author: Tu Pham
'''

import xml.etree.cElementTree as ET
import datetime

def sum_of_tag():
    tree = ET.ElementTree(file='test.xml')
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
        b = ((root[i].attrib)['starttime'])
        c = ((root[i].attrib)['endtime'])         
        file = open("temp.txt","a+")
        file.write(a + "," + b + "," + c +'\n')
    file.close()
    
def check_testcase_status(context):
    tree = ET.ElementTree(file='test.xml')
    for elem in tree.iterfind(context):
        if ((elem[0].text)) == None:
            return False
        else:
            return True
        
def get_log_content(context):
    tree = ET.ElementTree(file='test.xml')
    for elem in tree.iterfind(context):
        if ((elem[0].text)) == None:
            return ((elem[1].text))
        else:
            return ((elem[0].text))  
         
def get_firststarttime():
    f = open("temp.txt")
    lines = f.readlines()
    first_row = (lines[0].split(','))[1]
    return (first_row)
    f.close()

def get_lastendtime():
    f = open("temp.txt")
    lines = f.readlines()
    last_row = (lines[-1].split(','))[2]
    return (last_row)
    f.close()
    
    
    
def convert_epoch_time(epoch):
    s = float(epoch)
    return (datetime.datetime.fromtimestamp(s).strftime('%Y%m%d %H:%M:%S.%f'))
  

def create_xml_file_report():
    get_testcase_name()
    
    first_starttime = convert_epoch_time(get_firststarttime())
    last_endtime = convert_epoch_time(get_lastendtime())
    
    lines = [line.rstrip('\n') for line in open('temp.txt')]      
    root = ET.Element("robot", generator="Robot 3.0.2 (Python 3.6.2 on win32)", generated="20171017 14:49:30.312")
    suite = ET.SubElement(root, "suite", id = "The Final", name = "Man to Man", source="Something")     
    for i in lines:                
        a = i.split(',')
        test_case_name = a[0]
        starttime = convert_epoch_time(a[1])
        endtime = convert_epoch_time(a[2])
        context = "testcase[@name=" + "\"" + test_case_name + "\"" + "]"
        if check_testcase_status(context) == False:
            test_case_status = "FAIL"
        else:
            test_case_status = "PASS"    
                   
        test = ET.SubElement(suite, "test", id = test_case_name, name = test_case_name)
        kw = ET.SubElement(test, "kw", name ="LOG FROM JSHU", library="BuiltIn")
        doc = ET.SubElement(kw,"doc").text = "Logs the given message with the given level."
        msg = ET.SubElement(kw, "msg",timestamp ="20171017 14:49:30.312",level="INFO").text = get_log_content(context)
        status = ET.SubElement(kw,"status", status = test_case_status, starttime = starttime, endtime = endtime)
        status = ET.SubElement(test, "status", status = test_case_status, starttime = starttime, endtime = endtime, critical="yes")
        
    
    status = ET.SubElement(suite, "status", status = test_case_status ,starttime = first_starttime, endtime = last_endtime)
        
    statistics = ET.SubElement(root, "statistics")
    total = ET.SubElement(statistics, "total")
    #ET.SubElement(total, "stat", passed= "1",failed = "0").text = "some value1"
    #ET.SubElement(total, "stat", passed= "1",failed = "0").text = "some vlaue2"
    tag = ET.SubElement(statistics, "tag")
    suite = ET.SubElement(statistics, "suite")
    ET.SubElement(suite, "stat", passed= "1",failed = "0").text = "some value1"
    statistics = ET.SubElement(root, "errors")    
    file_name = "newXML/Final.xml"
    tree = ET.ElementTree(root)
    tree.write(file_name)


#rebot --Output output.xml *.xml

create_xml_file_report()


