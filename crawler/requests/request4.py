import urllib.parse

import requests

cookies = 'p_h5_u="79AAEB9F-D24C-4847-92C2-932C73D17252"; selectedStreamLevel="LD"; searchHistory="衣服,抖音,贝因美,贝因美童享,VAPE,澳洲爱他美金装加强,爱他美,爱他美,爱他美,德国爱他美Aptamil3段"; pgv_pvi="2359243776"; pgv_si="s6484395008"; cna="gaUpFa1GdUoCAbeG1JLr8aC4"; _ga="GA1.2.1541449524.1554801582"; uid="1a643571256b4c8080e33c932419549b"; yduss_test_m_v2="M6zstR5Ipt04Ogi-A4HcNIDy-Pp6aRnnRl9_C9FxYJgsoRRt4MxR2y6qHbv8aRv-18dfC7hGtgp1k_opRJK8AgaVqCNd2AxdZQMw932cXVy3WHPflXucZ8HOPI-f5Hlr8w5ytpHGvyKJvhXYflOoTXXlh7KWb6IYeY17lsqasw7_Y7T9lHQbvyibdmiUJtvgpseiAQg."; yduss_test_m="M6zhthVOv904OhWpFYuNLJjktLl6KVThX0EcQYM7M9UqrVkvp4gRmDz7QvmZL1-2msgeLeIRpAgnxvdoEIqnAhGY9TMwk19OdV1jryXZXUamEzvfyzyLO8GfRtuF6m8y-V0gt8WW7iPV5RTcfFL6HC7lgeHEZLQCYtcqzZDk91eaPLuhgXZIpzrAZUOhOcWl-NStTwbZDVA4L2-gLbBBmr1YZuYGOOEuo9_EZ7XdttYJUJiSKplXTKsChkeZq932qOn9URHBxxPCT8SW8K8ozFZi7zg7YHus0108CnKpvR7f5fzQe8JcwBUOOYIuaG1t8cKzz4WtxpMNIfWTkCApRUDHPSL68GF8NShjal2fQF9j7lL8nf8BAfVf-Y0yupk."; UM_distinctid="16dd43ec4f22a0-0b4f5183ae7f23-1d3d6b55-13c680-16dd43ec4f3af9"; bkuid="115cef8bc2f14e1ab94db74da3439b5a"; _token_hipac_seller_test_="SSOV3_voqf7s0qvak6rck9k95ODvjAA-ZuxYWVZ3-15V-Q4Pvdw_Sn4Hf0TXQSqokrHGGFe-J2kKAll_MR3np0Rnig6VW-Rwm491KcbkgEIV0lEDPWdYReMVAqF63gIfscZpjM95SHh0QVs2gG-mrwrSxgoKMtFXYaQU_G51p0a1jO7OdF0TCF6c_UTs4DMWCWeipA9LGvGZlFJuZwZmT76b2ByZffHLtEIkK6NtZaqL6E-ov7kUE."; hipac_seller_uid="5daf868fd61b4648be3e24fbe1ac61e2"; yduss_production_m="M6zhthVOv904OhWpFYuNLJjktLl6KVThX0EcQYNieJZmrhdi4sxHyXf7HrvaY02Bm8JIUuoU6kEki7l9B8nrEDaE_jVH2lxdOxRg4mvDXEi-WG7MxH2PaJrJFtnb7282-g12t5eX7ieFuU3ZKVOnSyKwlajQPP9NK_M22q_C70bsb-bogSMN_1nfYBXaL9TrsdfgARrJVSckP2nXZLNS1PRbK6gBNKBp9YyYN6DUs9AHV5OWIZBQVLxO2A-Z5Jaju-a8VUKakUPAEcGW9Kx4mlYw7jg_MCf11gg9VyWl6AqW8bqBMpJn2hMXOYogZgE2vsz0296nzdpWPbjF1D8_RBPLYC2opDV-MCoyaQPDR1k27lH9yqkHBKtY_Q.."; yduss_production_m_v2="M6zstR5Ipt04Ogi-A4HcNIDy-Pp6aRnnRl9_C9FxYJh16lch8J0YixK9WvOXPAjxlsMMUO4WtFRwk_4qFMS8UAeVrHMBgQkIZF5n-yiIFEjgHymUknujaoCRV97c725mrw1265vGuXLUvBmMeFGqSHa10bXENqFMIY1zg8qdu0esNO-gkS9I1GzAflCEPNulvw.."; _fmdata="CMBVcfUZ6d9%2BBTPGlo%2FHRk85%2FKuKa3t5W8iHJWpiSRoLzqp2ia5eT7fsS3grgCeyths%2F47T9OTiFWj5XerhRS9hwjd9u5xGMxDJHtPTW890%3D"; df="3ec7a7e9ea98d4b1ffea5c1cccfb94e1-16a333b4298_tongdun"; yduss_production="M6zhthVOv904OhWpFYuNLJjk-Pp6ZAbwDQscSIN_eNs0uBdq5o8JkDS3WvOXPhvo18IPHuUW43slhaE5RsPmUwLA_n4AgQMEM1Nn_y_MXQuxGW6ekn2MbJufENqQ720y-F8n7JfBtSjuqUOEegTrRzX9leKeNvEMeoxvjJ3Z7U26ELiggXYM-W3KPBWGO9rptue_RgeeGwYlL37ZfLxDmr0cNbpHc_w84JibMqDJttYKQ4aBcsAHE9FOxT_Ss9GwsOPzEkjNlEmcNoDSs6c7y00oqDZnYyr6pEx-Oj7g7AqA8fzQe8JF3BcVGa41c0p--fP4mMLkmYxBd6jDgG46HxHLbS6z5z91Z3A_D0_GBRt0-A3-hOkNQrl_68h2sc60l5jFQ_i7DmAPRv8zePmIZsoEMNMPRhLkT1jyrYIvQaOOrqggBw7_NhoCAkQdZmikO_Zi0ZJQGODCgaP1mzR-3vgyBmJl_zgrq7luHFkyQMzafHUiqDStimR79WauYJOkikCG1x6oL_moMzefOR_oNnJKbIFa7P7nbzsgarhXWIBzo4yShhNxgegLOzUgKRFy"; hipac.cn_USERID="1a643571256b4c8080e33c932419549b"; hipac.cn_LASTLOGINTIME="1573636690659"; hipac.cnuser_uuid="cead4a24-8046-4bc4-af99-75e0ed76c90a"; layerId="6296"'

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}

jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, urllib.parse.quote(value))

r = requests.get("https://mall.hipac.cn/mall/view/goods/itemIndex.html", cookies=jar, headers=headers)
r.encoding = 'utf-8'
print(r.text)
