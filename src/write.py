import xml.etree.cElementTree as ET
from datetime import datetime


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
        file = open("temp.txt","a+")
        file.write(a +'\n')
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
  

def create_xml_file_report():
    get_testcase_name()
    times = str(datetime.now())
    lines = [line.rstrip('\n') for line in open('temp.txt')]       
    for i in lines:
        test_case_name = i
        context = "testcase[@name=" + "\"" + i + "\"" + "]"
        if check_testcase_status(context) == False:
            test_case_status = "FAIL"
        else:
            test_case_status = "PASS"
        
        root = ET.Element("robot", generator="Robot 3.0.2 (Python 3.6.2 on win32)", generated=times)
        suite = ET.SubElement(root, "suite", id = test_case_name, name = test_case_name, source="D:\WorkSpace\Pycharm\etmDemo\Test\test.robot")
        test = ET.SubElement(suite, "test", id = test_case_name, name = test_case_name)
        kw = ET.SubElement(test, "kw", name ="LOG FROM JSHU", library="BuiltIn")
        doc = ET.SubElement(kw,"doc").text = "Logs the given message with the given level."
        msg = ET.SubElement(kw, "msg",timestamp ="20171017 14:49:30.312",level="INFO").text = get_log_content(context)
        status = ET.SubElement(kw,"status", status = test_case_status, starttime ="20171017 14:49:30.312", endtime ="20171017 14:49:30.312")
        status = ET.SubElement(test, "status", status = test_case_status, starttime ="20171017 14:49:30.312", endtime="20171017 14:49:30.312", critical="yes")
        status = ET.SubElement(suite, "status", status = test_case_status ,starttime ="20171017 14:49:29.427", endtime="20171017 14:49:30.312")
        statistics = ET.SubElement(root, "statistics")
        total = ET.SubElement(statistics, "total")
        #ET.SubElement(total, "stat", passed= "1",failed = "0").text = "some value1"
        #ET.SubElement(total, "stat", passed= "1",failed = "0").text = "some vlaue2"
        tag = ET.SubElement(statistics, "tag")
        suite = ET.SubElement(statistics, "suite")
        ET.SubElement(suite, "stat", passed= "1",failed = "0").text = "some value1"
        statistics = ET.SubElement(root, "errors")    
        file_name = "E:/Eclipse-workspace/excel/ExcelTest/newXML/" + test_case_name +".xml"
        tree = ET.ElementTree(root)
        tree.write(file_name)
           
#create_xml_file_report()

#get_testcase_name()

#print (get_log_content('testcase[@name="PG2-AUTOSEPENGINE-HA-TC13_tc"]'))

create_xml_file_report()







