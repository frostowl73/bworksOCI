'''
sample code: to read in a file for adding Users
'''

from broadworks_ocip import BroadworksAPI
import os
import csv


def setup():
    #XSP config 
    with open('baseconfig.txt', encoding='latin-1') as f:
        for xsp, port, user, provisioner_passwd, domain in csv.reader(f):
            provisioner = '@'.join([user, domain]) 

    with open('sp_group.csv', encoding='latin-1') as dnlist:
        for sp_id, groupid, phone in csv.reader(dnlist):
            lphone = [phone]
            print(f'Unassigned DN {lphone}')
            params = {'service_provider_id': sp_id, 'group_id':groupid, 'phone_number': lphone}
        
            #XSP config
            OCI_Session = BroadworksAPI(host=xsp, port=port, username=provisioner, password = provisioner_passwd)
            
            #Add User
            resp = OCI_Session.command("GroupDnUnassignListRequest", **params)
    
if __name__ == '__main__':
    setup()