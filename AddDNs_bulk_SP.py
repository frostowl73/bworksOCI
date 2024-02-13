'''
Add Mutiple DNs to Mutiple Service Providers reading from file sp_dn.csv
'''

from broadworks_ocip import BroadworksAPI
import os
import csv


def setup():
    #XSP config 
    with open('baseconfig.txt', encoding='latin-1') as f:
        for xsp, port, user, provisioner_passwd, domain in csv.reader(f):
            provisioner = '@'.join([user, domain]) 

    with open('sp_dn.csv', encoding='latin-1') as dnlist:
        for sp_id, phone in csv.reader(dnlist):
            lphone = [phone]
            print(f'Added dn {lphone}')
            params = {'service_provider_id': sp_id, 'phone_number': lphone}
        
            #XSP config
            OCI_Session = BroadworksAPI(host=xsp, port=port, username=provisioner, password = provisioner_passwd)
            
            #Add User
            resp = OCI_Session.command("ServiceProviderDnAddListRequest", **params)
    
if __name__ == '__main__':
    setup()