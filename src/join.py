'''
Created on Oct 18, 2017

@author: Tu Pham
'''
import os, os.path, sys
import glob
from xml.etree import ElementTree

def run(files):
    xml_files = glob.glob(files +"/*.xml")
    xml_element_tree = None
    for xml_file in xml_files:
        data = ElementTree.parse(xml_file).getroot()
        # print ElementTree.tostring(data)
        for result in data.iter('results'):
            if xml_element_tree is None:
                xml_element_tree = data 
                insertion_point = xml_element_tree.findall("./results")[0]
            else:
                insertion_point.extend(result) 
    if xml_element_tree is not None:
        print (ElementTree.tostring(xml_element_tree))