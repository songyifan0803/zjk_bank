import requests

class Api:
    @classmethod
    def get_cookies(cls):
        cookies = requests.request(url='http://10.150.2.50:31545/open-inmanage/index.html/open-inmanage/IM01001.do',
                                  data={'loginName': 'test004', 'loginPassword': 'c618e0213afd11198037d7abef3b3fad', 'remember': 'true'},
                                  method='POST')
        print(cookies.text)
        return cookies.cookies

    @classmethod
    def test_Api(cls, url, data=None):
        cookies = cls.get_cookies()

        if data != None:
            requests.request(url=url, data=data, method='POST', cookies=cookies)
        else:
            requests.request(url=url, method='GET', cookies=cookies)


if __name__ == '__main__':
    url = 'http://10.150.2.50:31545/open-inmanage/index.html/open-inmanage/IMC033013.do'
    data = {'routeId': 'http-111', 'routeName': '测试1号', 'routePath': 'http', 'routeOrder': '1',
            'routeAssertList[0][preName]': 'IFPReadBodyPredicateFactory', 'routeAssertList[0][preDesc]': '获取POST请求的报文',
            'routeAssertList[0][preInput]': '1', 'routeAssertList[0][preHashPar]': '0', 'routeAssertList[0][assertName]': 'IFPReadBodyPredicateFactory',
            'routeAssertList[0][_checked]': 'true', 'routeAssertList[0][_disabled]': 'true', 'sysId': '', 'protocolId': '',
            'routeUrl': 'http://ss',  'envId': '', 'routeType': '1'}

    Api.get_cookies()


