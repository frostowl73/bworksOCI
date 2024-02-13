'''
sample code: to read in variables from a csv file called, baseconfig.txt
'''

from broadworks_ocip import BroadworksAPI
import os
import csv
from pprint import pprint


def setup():
    #config 
    with open('baseconfig.txt', encoding='latin-1') as f:
        for xsp, port, user, provisioner_passwd, domain in csv.reader(f):
            provisioner = '@'.join([user, domain]) 
     
    group_name = "labSP_group1"  #use your own group name
    enter_id = "labSP"
    params = {'service_provider_id': enter_id, 'group_id':group_name}
    

    #init oci_session object
    OCI_Session = BroadworksAPI(host=xsp, port=port, username=provisioner, password = provisioner_passwd)

    #get available DNs in the group
    resp = OCI_Session.command("GroupDnGetAvailableListRequest", **params)
    pprint(resp.phone_number)
    
    #get Active DNs in the group
    resp = OCI_Session.command("GroupDnGetActivationListRequest", **params)
    pprint(resp.dn_table)
   
    
if __name__ == '__main__':
    setup()