'''from broadworks_ocip import BroadworksAPI

# configure the API, connect and authenticate to the server
api = BroadworksAPI(
    host = args.host, port=args.port, username=args.username, password=args.password,
)

# get the platform software level
response = api.command("SystemSoftwareVersionGetRequest")
print(response.version)
'''

##############################
from broadworks_ocip import BroadworksAPI
import os

# configure the API, connect and authenticate to the server
api = BroadworksAPI(
    host = '10.122.51.167', port='2208', username='jester@vle.broadsoft.com', password='happy123',
)

# get the platform software level
response = api.command("SystemSoftwareVersionGetRequest")
print(f'My Version sucka: {response.version}')
print('\n')

# get Sys Admins
sysadmin = api.command("SystemAdminGetListRequest")
for admin in sysadmin.system_admin_table:
    print(admin.administrator_id)
print(sysadmin.system_admin_table) 
print('\n')

# get the Service Providers
sp_list = api.command("ServiceProviderGetListRequest")
for provider in sp_list.service_provider_table:
        print(provider.service_provider_id)
print(sp_list.service_provider_table)
print('\n')

# get Group Admins
groupAdmin = api.command("GroupAdminGetListRequest", service_provider_id= sp_list, group_id='Group1')
for admin in groupAdmin.group_admin_table:
    print(f'My Group Admin: {admin.administrator_id}')
#print(groupAdmin.group_admin_table)
