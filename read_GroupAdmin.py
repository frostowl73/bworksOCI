'''
sample code: to read in variables from a csv file called, baseconfig.txt
'''

from broadworks_ocip import BroadworksAPI
import os
import csv

def setup():
    #config 
    with open('baseconfig.txt', encoding='latin-1') as f:
        for xsp, port, user, provisioner_passwd, domain in csv.reader(f):
            provisioner = '@'.join([user, domain]) 
     
    group_name = "Group1"  #use your own group name
    enter_id = "labSP"
    params = {'service_provider_id':enter_id, 'group_id':group_name}
    

    #init oci_session object
    OCI_Session = BroadworksAPI(host=xsp, port=port, username=provisioner, password = provisioner_passwd)

    #get Admin in the group
    resp = OCI_Session.command("GroupAdminGetListRequest", **params)
    for admin in resp.group_admin_table:
        print(f'{group_name} Admin is: {admin.administrator_id}')
    # print('\n')
    # #print(resp.group_admin_table)
   
    
if __name__ == '__main__':
    setup()