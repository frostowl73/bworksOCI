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

    with open('Useradd.csv', encoding='latin-1') as userfile:
        for sp_id, group_name, UserId, LastName, FirstName, CallingLineIdLastName, CallingLineIdFirstName, phone, ext, password in csv.reader(userfile):
            params = {'service_provider_id': sp_id, 'group_id': group_name, 'user_id': UserId, 'last_name': LastName, 'first_name': FirstName, 'calling_line_id_last_name': CallingLineIdLastName, 'calling_line_id_first_name': CallingLineIdFirstName, 'phone_number': phone, 'extension': ext, 'password': password}
        
            #XSP config
            OCI_Session = BroadworksAPI(host=xsp, port=port, username=provisioner, password = provisioner_passwd)
            
            #Add User
            resp = OCI_Session.command("UserAddRequest21", **params)
    
if __name__ == '__main__':
    setup()
 