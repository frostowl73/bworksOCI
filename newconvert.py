import sys
from broadworks_ocip import BroadworksAPI
import os
import re

def listToString(s):
    str1 = ''
    print(str1.join(s))
    
def convert(oci_response):
    #li = list(oci_response.split(','))
    li = re.split('\] |\[ |, |\) |\(', oci_response)
    print(li[1])
    print(f'crap ass  {li[11]}')
    print(li[21])
    #print('\n')
    return li

# configure the API, connect and authenticate to the server
api = BroadworksAPI(
    host = 'xxx', port='2208', username='xxx@vle.broadsoft.com', password='xxx',
)
sysadmin = api.command("SystemAdminGetListRequest")
#
# 
# print(sysadmin.system_admin_table)
ab = sysadmin.system_admin_table
print(ab)
print('\n')
#listToString(str(ab))
convert(str(ab))
print('\n')







#s = ['[systemAdminTable', "administrator_id='admin'", "last_name='Administrator'", "first_name='Default'", "type='system'", "read_only='false'", "language='English'", "account_disabled='false'", "last_authenticated_date='Jun 17", "2021 08:30 MDT')", 'systemAdminTable', "administrator_id='jester'", 'last_name=None', 'first_name=None', "type='system'", "read_only='false'", "language='English'", "account_disabled='false'", "last_authenticated_date='Oct 06", "2021 10:35 MDT')", 'systemAdminTable', "administrator_id='zschell'", 'last_name=None', 'first_name=None', "type='system'", "read_only='false'", "language='English'", "account_disabled='false'", "last_authenticated_date='Jun 17", "2021 08:30 MDT')]"]
#print(listToString(s[1]))
