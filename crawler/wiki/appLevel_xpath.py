import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'Cookie': '_ga=GA1.2.828687320.1583719934; confluence.list.pages.cookie=list-content-tree; c=mkE7veAx-1594129645235-c9095a28133d4-184198851; _fmdata=QYPEtNYFYvg9g%2FKxG6nFuk9%2FiKSuhJwwNxvOz7AcilpOBNIRww6S3OgqbuU5%2FhiT9dOT%2FIf1KR34uvFL5vD2hM9VyTspKh0e4PSVP0QflAI%3D; _xid=XpBusurkuXJjScvv%2B9IzRqJBA1Mlk0fJ4UsLA5TU2ZJxj1luNqP1It2O0ieBy3jHbmnjXT1okInbxI0%2B0L%2B%2BKQ%3D%3D; mywork.tab.tasks=false; yduss_test_m_v2=M6zstR5Ipt04Ogi-A4HcNIDy-Pp6aRnnRl9_C9FxYJgMpwtC4YMUl3n1WrzGaEuNkYRQSu1A5QZyl6MvQce3VVfO_SIH014Eb1Fk_C2fAV6yH2nO0zLIasfdHIjYlz9x8U4s65HCvnXX70mLLFCpECbmjubGZKQceNh7ls3Kshf7N_v1lSlAui2cKA7SfurzrdyrRwDSAw8.; bkuid=115cef8bc2f14e1ab94db74da3439b5a; yduss_production_m_v2=M6zstR5Ipt04Ogi-A4HcNIDy-Pp6aRnnRl9_C9FxYJgnpR9hp8JfjCi8CoDRLwPmxJdfC-kTvlAilf0qQcO0BQHOryMH1w5YNlQx_XDIDQumVn2ZlGiDbcfiEcmH_GM2-V0m68XB6XGA7RvTLFenSyPihbbKM64Wdt1zms7JrxL4MO71ln9AsiqYT0OPJ9Ljt9zuXg..; seraph.confluence=52494353%3Ac65a532f4f33872f1216dd04e691238b744033d0; _gid=GA1.2.1555360649.1605418503; JSESSIONID=084E05772E333C56C8DB91927AE6B0BE',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

}


def get_on_page(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


if __name__ == '__main__':
    url = 'http://k.yangtuojia.com/pages/viewpage.action?pageId=46282129'
    html_resource = get_on_page(url)
    html = etree.HTML(html_resource)
    """ :type:etree._Element"""

    # print(type(html))
    # html_encode = etree.tostring(etree.HTML(html_resource), encoding="utf-8", pretty_print=True, method="html")
    # print(html_encode.decode('utf-8'))
    results = html.xpath('//tr/td[@class="confluenceTd"]/..')
    appLevels = []

    for result in results:
        # 指定类型，方便ide提示
        assert isinstance(result, etree._Element)
        tds = result.xpath('/td')  # type:etree._Element

        rowspan = tds[0].get('rowspan')
        if rowspan:
            print(rowspan)

        # rowspan = result.get('rowspan')
        # if rowspan:
        #     print(rowspan)

    # 文本获取
    # result = html.xpath('//tr/td[@class="confluenceTd"]/text()')
    # print(result)

    # 属性获取
    # result = html.xpath('//tr/td[@class="confluenceTd"]/@rowspan')
    # print(result)


class AppLevel:
    def __init__(self, appName, appLevel):
        self.appName = appName
        self.appLevel = appLevel
