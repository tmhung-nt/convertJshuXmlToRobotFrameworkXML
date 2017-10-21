'''
Created on Oct 21, 2017

@author: Hung Tran

'''

import xml.etree.cElementTree as ET
import datetime
from Testcase import Testcase


class TestSuite(object):
    """
    Testcases object contains info of all testcases in Jshu xml file.
    Each testcase has following attributes:
        - _name: testecase's name
        - _starttime: testcase's start time
        - _endtime: testcase's end time
        - _status: passed or failed
    """

    def __init__(self, _input_jshu_xml):
        self._jshu_xml_file = _input_jshu_xml
        self._testcase_list = []
        self._xml_tree = None
        self._xml_root = None



    def extract_testcase_list_from_xml(self):
        """
        read jshu xml and extract testcase's information
        :return:
        """
        self._xml_tree = ET.ElementTree(file=self._jshu_xml_file)
        self._xml_root = self._xml_tree.getroot()
        number_of_tags = self.get_total_testcases()
        for i in range(0, number_of_tags):
            # get attributes of each testcase
            _tc_name = (self._xml_root[i].attrib)['name']
            _tc_start_time = self.convert_epoch_time((self._xml_root[i].attrib)['starttime'])
            _tc_end_time = self.convert_epoch_time((self._xml_root[i].attrib)['endtime'])

            _tc_locator = "testcase[@name=" + "\"" + _tc_name + "\"" + "]"
            _tc_status = self.get_testcase_status(_tc_locator)
            _tc_log = self.get_testcase_log(_tc_locator)
            # add testcase to testcase_list

            _testcase = Testcase(_tc_name, _tc_start_time, _tc_end_time, _tc_status, _tc_log)
            self._testcase_list.append(_testcase)

    def get_total_testcases(self):
        """
        get the total number of testcases in jshu xml files
        :return:
        """
        counter = 0
        #get number of child nodes in xml file
        for child_of_root in self._xml_root:
            child_of_root.tag
            counter += 1

        self._total_testcases = counter
        return counter

    def get_testcase_status(self, _element_to_be_searched):
        """
        input is an element to search in xml tree
        :param _element_to_be_searched:
        :return:
        """
        for _element in self._xml_tree.iterfind(_element_to_be_searched):
            if ((_element[0].text)) == None:
                return 'FAIL'
            else:
                return 'PASS'

    def get_testcase_log(self, _element_to_be_searched):
        """
        input is an element to search in xml tree
        :param _element_to_be_searched:
        :return:
        """
        for _element in self._xml_tree.iterfind(_element_to_be_searched):
            if ((_element[0].text)) == None:
                return ((_element[1].text))
            else:
                return ((_element[0].text))

    def get_testcase_list(self):
        """
        return the testcase_list list
        :return:
        """
        return self._testcase_list

    def get_total_number_of_testcases(self):
        return len(self._testcase_list)

    def convert_epoch_time(self, _input_epoch_time):
        """
        convert epoch time in miliseconds to human time in miliseconds as well
        :param _input_epoch_time:
        :return:
        """
        s = float(_input_epoch_time)
        return (datetime.datetime.fromtimestamp(s).strftime('%Y%m%d %H:%M:%S.%f'))

    def _print_testcases_info(self, _print_log=False):
        """
        print to console the testcases's information
        :return:
        """

        print "Total: %d TCs" % (self.get_total_number_of_testcases())
        _iter = 1
        for _testcase in self._testcase_list:
            print "Testcase %d:" % (_iter)
            print "\tName: %s" % (_testcase._name)

            print "\tStar time: %s" % (_testcase._start_time)
            print "\tEnd time: %s" % (_testcase._end_time)
            print "\tStatus: %s" % (_testcase._status)
            if _print_log:
                print "\tLog: %s" % (_testcase._log)
            _iter += 1

#
# _content = Testcases('inputXML/test.xml')
# _content.extract_testcase_list_from_xml()
# _content._print_testcases_info()
