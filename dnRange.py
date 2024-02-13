from broadworks_ocip import BroadworksAPI
import csv
from broadworks_ocip import OCIRequest

def setup():
    #XSP config 
    with open('baseconfig.txt', encoding='latin-1') as f:
        for xsp, port, user, provisioner_passwd, domain in csv.reader(f):
            provisioner = '@'.join([user, domain]) 
     
    #params = {'service_provider_id':sp_id, 'phone_number':phoneNumber}
    #dnrange = ['3035551212','3035551220'] 
    minphone_number = '3035551212'
    maxphone_number = '3035551220'
    #dnrange = [minphone_number, maxphone_number] 
    #XSP config
    OCI_Session = BroadworksAPI(host=xsp, port=port, username=provisioner, password = provisioner_passwd)
    
    result = OCI_Session.command("ServiceProviderDnAddListRequest",
         service_provider_id="labSP", dn_range=[OCI_Session.get_type_object("DNRange", min_phone_number=minphone_number,max_phone_number=maxphone_number)])
         #service_provider_id="labSP", phone_number=['3037775555'])
         
                 
        
if __name__ == '__main__':
    setup()