import csv

with open('baseconfig.txt', encoding='latin-1') as f:
        lines = f.read()
        print(lines)
        
# with open('UserAdd.csv', encoding='latin-1') as userList:
#          ulines = userList.read()
#          print(ulines)
         

with open('Useradd.csv', encoding='latin-1') as userfile:
    for sp_id, group_name, UserId, LastName, FirstName, CallingLineIdLastName, CallingLineIdFirstName, phone, ext, password in csv.reader(userfile):
        params = {'service_provider_id': sp_id, 'group_id': group_name, 'user_id' :UserId, 'last_name' :LastName, 'first_name' :FirstName,'calling_line_id_last_name': CallingLineIdLastName,'calling_line_id_first_name': CallingLineIdFirstName,'phone_number':phone, 'extension': ext, 'password' : password}
        print(params)

    
    
    
    
    
