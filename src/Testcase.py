class Testcase(object):
    """
    This object contains all attribute of a testcase
    """
    def __init__(self, _tc_name=None, _tc_start_time=None,
                 _tc_end_time=None, _tc_status=None, _tc_log=None):
        self._name = _tc_name
        self._start_time = _tc_start_time
        self._end_time = _tc_end_time
        self._status = _tc_status
        self._log = _tc_log
