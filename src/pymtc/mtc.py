#

import httplib
import urllib
import json


class MakeTestMessage(object):
    def __init__(self, **kwargs):
        self.__domain = kwargs.get('domain')
        self.__local = kwargs.get('local')
        self.__id = kwargs.get('id')
        self.__msgid = kwargs.get('msgid')

    def get_msgid(self):
        return self.__msgid

    def __repr__(self):
        return "<MakeTestMessage msgid={msgid!r}>".format(msgid=self.__msgid)


class MakeTestClient(object):
    def __init__(self, token=None):
        self.__token = token
        self.__version = "1.0"

    def dispose(self):
        pass

    def messageCount(self, mailbox):
        query = urllib.urlencode({'token': self.__token, "local": mailbox})
        headers = {
            "X-Client-Version": self.__version,
        }
        conn = httplib.HTTPConnection("www.make-test.com")
        uri = "{path}?{query}".format(path="/msg_count", query=query)
        conn.request("GET", uri, None, headers)
        response = conn.getresponse()
        if response.status != 200:
            raise EnvironmentError("Internal Server Error")
        data = response.read()
        conn.close()
        res = json.loads(data)
        result = res.get('count')
        return result

    def messageIndex(self, mailbox):
        result = None
        query = urllib.urlencode({'token': self.__token, "local": mailbox})
        headers = {
            "X-Client-Version": self.__version,
        }
        conn = httplib.HTTPConnection("www.make-test.com")
        uri = "{path}?{query}".format(path="/msg_index", query=query)
        conn.request("GET", uri, None, headers)
        response = conn.getresponse()
        if response.status != 200:
            raise EnvironmentError("Internal Server Error")
        data = response.read()
        conn.close()
        res = json.loads(data)
        if isinstance(res, list):
            result = []
            for msg in res:
                m = MakeTestMessage(**msg)
                result.append(m)
        return result

    def messageFetch(self, msgid):
        result = None
        query = urllib.urlencode({'token': self.__token, "msgid": msgid})
        headers = {
            "X-Client-Version": self.__version,
        }
        conn = httplib.HTTPConnection("www.make-test.com")
        uri = "{path}?{query}".format(path="/msg", query=query)
        conn.request("GET", uri, None, headers)
        response = conn.getresponse()
        if response.status != 200:
            raise EnvironmentError("Internal Server Error")
        result = response.read()
        conn.close()
        return result

