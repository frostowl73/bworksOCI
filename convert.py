import re

def convert(oci_response):
    #li = list(oci_response.split(','))
    li = re.split('\] |\[ |, |\) |\(', oci_response)
    print(li[1])
    #print('\n')
    return li

zstr = "[systemAdminTable(administrator_id='admin', last_name='Administrator', first_name='Default', type='system', read_only='false', language='English', account_disabled='false', last_authenticated_date='Jun 17, 2021 08:30 MDT'), systemAdminTable(administrator_id='jester', last_name=None, first_name=None, type='system', read_only='false', language='English', account_disabled='false', last_authenticated_date='Oct 06, 2021 10:35 MDT'), systemAdminTable(administrator_id='zschell', last_name=None, first_name=None, type='system', read_only='false', language='English', account_disabled='false', last_authenticated_date='Jun 17, 2021 08:30 MDT')]"
print('\n')
#print (convert(zstr))
convert(zstr)