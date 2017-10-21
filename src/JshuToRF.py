'''
Created on Oct 21, 2017

@author: Hung Tran

'''

import xml.etree.cElementTree as ET
from Testcases import Testcases
import os

class JshuToRF(object):
    """
    Provide methods to read and convert Jshu xml report file to RobotFramework output.xml file.
    After converting, there is method to run rebot command to generate RobotFramework report/log html files
    """
    def __init__(self,_input_jshu_xml_file,_jobName=None ):
        self._input_jshu_xml_file = _input_jshu_xml_file
        if _jobName is not None:
            self._job_name = _jobName
        else:
            self._job_name = "Dummy Job Name"

    def create_xml_file_report(self):
        # extract testcase information from Jshu xml suite
        _ts_object = Testcases(self._input_jshu_xml_file)
        _ts_object.extract_testcase_list_from_xml()
        _tc_list = _ts_object.get_testcase_list()

        #get suite start time and end time
        _suite_starttime = _tc_list[0]._start_time
        _suite_endtime   = _tc_list[-1]._end_time

        # inital xml root of RobotFramework output.xml
        root = ET.Element("robot", generator="Robot Framwork", generated="")
        suite = ET.SubElement(root, "suite", id="RobotFramework Output XML", name=self._job_name, source="Something")

        for _tc in _tc_list:
            test = ET.SubElement(suite, "test", id=_tc._name, name=_tc._name)
            kw = ET.SubElement(test, "kw", name="LOG FROM JSHU", library="BuiltIn")
            doc = ET.SubElement(kw, "doc").text = "Logs the given message with the given level."
            msg = ET.SubElement(kw, "msg", timestamp="20171017 14:49:30.312", level="INFO").text = _tc._log

            kw_status = ET.SubElement(kw, "status", status=_tc._status, starttime=_tc._start_time, endtime=_tc._end_time)
            test_status = ET.SubElement(test, "status", status=_tc._status,
                                        starttime=_tc._start_time, endtime=_tc._end_time, critical="yes")

        suite_status = ET.SubElement(suite, "status", status=_tc._status, starttime=_suite_starttime,
                               endtime=_suite_endtime)

        statistics = ET.SubElement(root, "statistics")
        total = ET.SubElement(statistics, "total")
        # ET.SubElement(total, "stat", passed= "1",failed = "0").text = "some value1"
        # ET.SubElement(total, "stat", passed= "1",failed = "0").text = "some vlaue2"
        tag = ET.SubElement(statistics, "tag")
        suite = ET.SubElement(statistics, "suite")
        ET.SubElement(suite, "stat", passed="1", failed="0").text = "some value1"
        statistics = ET.SubElement(root, "errors")

        #writing xml tree to file
        file_name = "newXML/Final.xml"
        tree = ET.ElementTree(root)
        tree.write(file_name, xml_declaration=True)

    def generate_RF_output_xml(self):
        """
        run rebot command with input is Final.xml which is generate by create_xml_file_report()
        :return:
        """
        os.system('runRebotCommand.bat')

_convert = JshuToRF('inputXML/test.xml')
_convert.create_xml_file_report()
_convert.generate_RF_output_xml()



