from tracemalloc import stop
from broadworks_ocip import BroadworksAPI
import csv


def setup():
    #XSP config 
    with open('baseconfig.txt', encoding='latin-1') as f:
        for xsp, port, user, provisioner_passwd, domain in csv.reader(f):
            provisioner = '@'.join([user, domain]) 
     
    #params = {'service_provider_id':sp_id, 'phone_number':phoneNumber}
            
    #XSP config
    OCI_Session = BroadworksAPI(host=xsp, port=port, username=provisioner, password = provisioner_passwd)

    sinrg = input('Do you wnat to add a Single DN or DN Range to a Service Provider? (Single/Range)')

    if sinrg.replace('s', 'S') == 'Single':
        sp_id = input('Please enter Service Provider Id: ')
        strNumber = input('Enter Single DN: ')
        phoneNumber = []
        #print(strNumber)
        phoneNumber.append(strNumber)
        #print(phoneNumber)
        params = {'service_provider_id':sp_id, 'phone_number':phoneNumber}
       
        
        
    if sinrg.replace('r', 'R') == 'Range':
        sp_id = input('Please enter Service Provider Id: ')
        minphone_number = input('Enter DN mimimum Range: ')
        maxphone_number = input('Enter DN maximum Range: ')
        dnrange = [OCI_Session.get_type_object("DNRange", min_phone_number=minphone_number,max_phone_number=maxphone_number)]
        # print(type(dnRange))
        params = {'service_provider_id':sp_id, 'dn_range': dnrange}
                
    #Add Dn(s)
        resp = OCI_Session.command("ServiceProviderDnAddListRequest", **params)
    
if __name__ == '__main__':
    setup()