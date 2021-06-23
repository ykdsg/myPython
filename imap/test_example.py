from unittest import TestCase, main
from unittest import mock
from example import new_imap_client
import example


class Test(TestCase):

    @mock.patch('example.IMAPClient', spec=True)
    def test_new_imap_client(self, mock_client):
        example.usage()
        # with new_imap_client(username, password) as client:
        #     # 【assert】__init__
        #     mock_client.assert_called_with('smtp.exmail.qq.com')
        #     # 【assert】login
        #     mock_client().login.assert_called_with('USERNAME', '******')
        #     # 【assert】select_folder
        #     mock_client().select_folder.assert_called_with('INBOX', readonly=True)

        # with new_imap_client(username, password, 'Sent Messages') as client:
        #     # 【assert】Parameter:folder
        #     mock_client().select_folder.assert_called_with('Sent Messages', readonly=True)


if __name__ == '__main__':
    main(verbosity=2)
    # 【output】
    # test_new_imap_client (__main__.Test) ... ok
    # ----------------------------------------------------------------------
    # Ran 1 test in 0.004s
    # OK
