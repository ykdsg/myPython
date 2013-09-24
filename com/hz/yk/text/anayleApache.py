# -*- coding:utf8 -*-
from StringIO import StringIO

__author__ = 'ykdsg'

import re
import os

vhost_start = re.compile(r'<VirtualHost\s+(.*?)>')
vhost_end = re.compile(r'</VirtualHost')
docroot_re=re.compile(r'(DocumentRoot\s+)(\S+)')
def replace_docroot(conf_string,vhost,new_docroot):
    '''   yield new lines of an httpd.conf file where docroot lines matching the
        specified vhost are replaced withthe new_docroot
    '''
    conf_file = StringIO(conf_string)
    in_vhost=False
    for line in conf_file:
        vhost_start_match = vhost_start.search(line)
        if vhost_start_match:
            curr_vhost=vhost_start_match.groups()[0]
            in_vhost=True
        if in_vhost and (curr_vhost == vhost):
            docroot_match=docroot_re.search(line)
            if docroot_match:
                sub_line = docroot_re.sub(r'\1%s' % new_docroot,line)
                line = sub_line
        vhost_end_match = vhost_end.search(line)
        if vhost_end_match:
            in_vhost = False
        yield line

if __name__=='__main__':
    import sys
    conf_file='apache.xml'
    vhost = 'local2:80'
    docroot = '/v/test/new'
    conf_string=open(conf_file).read()
    for line in replace_docroot(conf_string,vhost,docroot):
        print line




