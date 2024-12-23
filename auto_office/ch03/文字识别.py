from aip import AipOcr

""" 你的 APPID AK SK """
# APP_ID = '你的 App ID'
# API_KEY = '你的 Api Key'
# SECRET_KEY = '你的 Secret Key'
APP_ID = '116795676'
API_KEY = 'SFKuhF8Lh7iMH6yYGUz9flRD'
SECRET_KEY = 'hydqjLMrgZ1vBud5T9gkeFTyOlWhYlvt'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('example.png')

""" 调用通用文字识别, 图片参数为本地图片 """
result = client.basicGeneral(image)
print(result)
info = []
for i in result['words_result']:
    info.append(i['words'])
print(info)

with open('result.txt', 'w') as f:
    f.write(str(info))
