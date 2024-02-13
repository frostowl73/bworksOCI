'''Add a Single Dn or DN range to a specified Service Provider'''


from broadworks_ocip import BroadworksAPI
import csv


def setup():
    #XSP config 
    with open('baseconfig.txt', encoding='latin-1') as f:
        for xsp, port, user, provisioner_passwd, domain in csv.reader(f):
            provisioner = '@'.join([user, domain]) 
     
             
    #XSP Login via broadworksAPI
    OCI_Session = BroadworksAPI(host=xsp, port=port, username=provisioner, password = provisioner_passwd)

    sinrg = input('Do you want to add a Single DN or DN Range to a Service Provider? (Single/Range)')

    if sinrg.replace('s', 'S') == 'Single':
        sp_id = input('Please enter Service Provider Id: ')
        strNumber = input('Enter Single DN: ')
        phoneNumber = []
        phoneNumber.append(strNumber)
        params = {'service_provider_id':sp_id, 'phone_number':phoneNumber}
        
       
        
    if sinrg.replace('r', 'R') == 'Range':
        sp_id = input('Please enter Service Provider Id: ')
        minphone_number = input('Enter DN mimimum Range: ')
        maxphone_number = input('Enter DN maximum Range: ')
        dnrange = [OCI_Session.get_type_object("DNRange", min_phone_number=minphone_number,max_phone_number=maxphone_number)]
        params = {'service_provider_id':sp_id, 'dn_range': dnrange}
                
    #Add Dn(s)
    add_DN = OCI_Session.command("ServiceProviderDnAddListRequest", **params)
    print(add_DN)
    
if __name__ == '__main__':
    setup()