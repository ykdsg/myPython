"""
imapclient库
> IMAPClient is an easy-to-use, Pythonic and complete IMAP client library.

github地址: https://github.com/mjs/imapclient
Docs: https://imapclient.readthedocs.io/en/2.2.0/

【demo】
new_imap_client - 创建IMAP客户端

usage - 常见操作使用，包括:
        检索指定邮件（根据邮件标题）
        解析邮件
        打印From,Subject，Size信息
        循环邮件part内容
        下载附件
        获取邮件正文内容并解码

example_serach_since - IMAPClient.search，根据日期范围检索邮件

parse_winmail_dat - 解析文件为winmail.dat的附件, 并下载
"""

import email
import logging
import sys
from datetime import datetime
from email.header import decode_header
from email.parser import Parser
from email.utils import parsedate_to_datetime

import pytz
from imapclient import IMAPClient


def customer_imap_client(folder='INBOX') -> IMAPClient:
    # 【修改】账号和密码
    return new_imap_client('******', '*******', folder)


def new_imap_client(username, password, folder='INBOX') -> IMAPClient:
    """创建IMAP客户端

    :param username: 账号
    :param password: 密码
    :param folder: 邮件箱,默认值INBOX(收件箱),发件箱Sent Messages
    :return: IMAPClient
    """
    try:
        # 【修改】邮件服务器地址
        client = IMAPClient('imap.mxhichina.com')
        client.login(username, password)
    except Exception as e:
        logging.error(e)
        sys.exit(1)
    else:
        # 选择邮件箱
        # 【tips】client.list_folders()可列出所有folder名称
        client.select_folder(folder, readonly=True)
        return client


def usage():
    """常见操作使用

    :return:

    标准库email
    【参考】https://docs.python.org/zh-cn/3/library/email.html
    """

    with customer_imap_client() as client:

        # 【参考】flags标志:https://imapclient.readthedocs.io/en/2.2.0/concepts.html#message-flags
        # DELETED = br'\Deleted' 邮件删除标记
        # SEEN = br'\Seen'  邮件已阅标记
        # ANSWERED = br'\Answered' 邮件已回复标记
        # FLAGGED = br'\Flagged' 表示邮件是否为回收站中的邮件
        # DRAFT = br'\Draft' 草稿邮件标记
        # RECENT = br'\Recent'  新邮件标记
        # -----------------------------------------------------------------------------------------------
        # 【实践经验】如果是检索收件箱(INBOX), 上面的6个标志基本没啥用，例如DELETE标志，一般是返回[]空列表，
        # 因为邮件被删除时将自动转到已删除邮件目录，INBOX目录已不存在此邮件。
        # 收件箱常用到的标志是ALL(默认值)、 SINCE这两个
        # 这里是获取收件箱的所有邮件id
        messages = client.search()
        # 【output】search方法执行很快，返回一个存储邮件id的列表, [1, 2, 3, ...]这种

        # fetch selectors are passed as a simple list of strings.
        # 【demo参考】https://imapclient.readthedocs.io/en/2.2.0/concepts.html#working-with-fetched-messages
        # 【fetch指令参考(他人博客)】https://www.cnblogs.com/rain99/articles/10550470.html
        # FLASG 为该邮件设置的标记
        # INTERNALDATE 邮件的实际日期。
        # RFC822:邮件mine内容
        # RFC822.HEADER 邮件头部信息
        # RFC822.SIZE 邮件大小
        # RFC822.TEXT 邮件文本内容
        # ENVELOP 邮件头属性
        # UID 邮件唯一标识
        # ---------------------------------------------------------------------------------------------
        # 【处理业务需求】假设需求是找出以subject开头的标题的最新邮件，并下载附件。
        # 【思路】有些邮件包含附件后会变得特别大，如果要遍历的邮件很多，直接遍历处理，每封邮件都获取'RFC822'内容，
        # fetch方法执行耗时可能会很长, 因此可以分两次fetch处理，减少处理时长：
        # 1)第一次fetch先使用ENVELOP或者RFC822.HEADER获取邮件头信息找到满足业务需求邮件的id
        # 2)第二次fetch根据这个邮件id使用'RFC822'获取邮件MIME内容，下载附件

        while messages:
            message_id = messages.pop()
            # 第一次fetch
            response = client.fetch(message_id, ['ENVELOPE', 'FLAGS', 'RFC822.SIZE'])
            print('{id}: {size} bytes, flags={flags}'.format(
                id=message_id,
                size=response[message_id][b'RFC822.SIZE'],
                flags=response[message_id][b'FLAGS']))

            envelope = response[message_id][b'ENVELOPE']

            subject, decode = decode_header(envelope.subject.decode())[0]
            # 【解码】对诸如b"=?gb2312?B?UkU6IElEQSDUpLLivfi2yLj619k=?="含有中文的内容转换解码
            if decode:
                try:
                    subject = subject.decode(decode)
                except LookupError:  # 处理不识别的编码，如'unknown-8bit'
                    subject = subject.decode('gb2312')
            else:
                subject = str(subject)

            # 假设需求是找到标题是以subject开头的最新邮件
            if subject.startswith('sujbect'):
                # 这里是第二次fetch, 直接根据消息id获取邮件MIME内容
                response = client.fetch(message_id, ['RFC822'])

                # 【parse】https://docs.python.org/zh-cn/3/library/email.parser.html?highlight=message_from_bytes#email.message_from_bytes
                email_message = email.message_from_bytes(response[message_id][b"RFC822"])

                # 解析邮件主体
                msg = Parser().parsestr(email_message.as_string())

                # 【do something start】 //////////////////////////////////////////////////
                for part in msg.walk():
                    # 提取附件文件名，没有则返回None
                    file_name = part.get_filename()

                    if file_name is None:
                        continue

                    filename, decode = decode_header(file_name)[0]

                    # 若有中文需要先转码
                    filename = filename.decode(decode) if decode else str(filename)
                    # 空白符转空格，有需要的可以加上这行代码
                    filename = filename.replace('\xa0', ' ')

                    # 下载附件
                    with open(filename, 'wb') as file:
                        file.write(part.get_payload(decode=True))

                # 获取邮件正文内容并解码，get_content_charset将尝试获取编码字符集，gb2312是默认值
                content = msg.get_payload()[0].get_payload(decode=True).decode(msg.get_content_charset('gb2312'))
                print(content)

                # 【do something end】 //////////////////////////////////////////////////////////////

                # 已找到满足需求的邮件，退出循环和函数
                return


def example_serach_since():
    from datetime import date

    # 中国时区，用于后续转换邮件其他时区的Date值
    # 【tips】pytz.common_timezones列出的各个时区的名称
    shanghai = pytz.timezone('Asia/Shanghai')

    with customer_imap_client() as client:
        # 筛选2021年3月14日及以后的邮件
        # 【Notification】实测发现只支持到天的检索，不支持时分秒,例如:
        # [u'SINCE', datetime(2021, 3, 14, 16)]
        # 效果仍然是从3月14号0点开始检索
        # 【Notification】这个时间不一定准，比如可能把3月14日之前的邮件也会找出来，
        # 因此要对邮件时间做进一步的处理和确认
        messages = client.search([u'SINCE', date(2021, 3, 14)])

        response = client.fetch(messages, ['FLAGS', 'RFC822.SIZE', 'RFC822'])

        for message_id, data in response.items():
            print('{id}: {size} bytes, flags={flags}'.format(
                id=message_id,
                size=data[b'RFC822.SIZE'],
                flags=data[b'FLAGS']))

            email_message = email.message_from_bytes(data[b"RFC822"])

            # 【邮件处理】format_datetime()的逆操作,在成功时返回一个 datetime:
            # Thu, 18 Mar 2021 18:14:00 +0000 -> datetime.datetime(2021, 3, 18, 18, 14, tzinfo=datetime.timezone.utc)
            # .astimezone(shanghai)将转换为中国时区
            # 【参考】关于更多处理邮件的工具:https://docs.python.org/zh-cn/3/library/email.utils.html
            msg_date = parsedate_to_datetime(email_message.get('Date')).astimezone(shanghai)

            # 按时间过滤邮件
            # 【注意】带时区不能直接跟datetime做比较
            if msg_date.replace(tzinfo=None) < datetime(2021, 3, 14, 16):
                continue
