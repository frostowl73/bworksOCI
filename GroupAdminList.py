from broadworks_ocip import BroadworksAPI
import csv
import os


def setup():
    #XSP config 
    with open('baseconfig.txt', encoding='latin-1') as f:
        for xsp, port, user, provisioner_passwd, domain in csv.reader(f):
            provisioner = '@'.join([user, domain]) 

    #XSP Login via broadworksAPI
    api = BroadworksAPI(host=xsp, port=port, username=provisioner, password = provisioner_passwd)


    
    #SP list     
    sp_list = api.command("ServiceProviderGetListRequest")
    for provider in sp_list.service_provider_table:
        print(provider.service_provider_id)
    #print(sp_list.service_provider_table)
    
    params = {'service_provider_id':provider.service_provider_id} 
    for i in params:
        print(provider.service_provider_id)
        
    
    group_list = api.command("GroupGetListInServiceProviderRequest", **params)
    for group in group_list.group_table:
       print(f'SP_ID:{provider.service_provider_id} Group_ID:{group.group_id}')
    #print(group_list.group_table)
    
           
    '''#get Groups Admins
    grouplist = api.command("GroupGetListInServiceProviderRequest", **params) 
    for gadmin in grouplist.gadmin_table:
         print(gadmin.gadmin_table)
    print(grouplist.gadmin_table)'''

    '''# get Group Admins
    groupAdmin = api.command("GroupAdminGetListRequest", service_provider_id= sp_list, group_id = grouplist)
    for admin in groupAdmin.group_admin_table:
        print(f'My Group Admin: {admin.administrator_id}')
    #print(groupAdmin.group_admin_table)'''

if __name__ == '__main__':
    setup()