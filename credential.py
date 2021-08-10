class Credential():
    '''
    create credential class
    '''

    def __init__(self, name, username, passcode):
        self.name = name
        self.username = username
        self.passcode = passcode

    credential_list = []  # credential list

    def add_credential(self):
        '''
        Add credentials
        '''
        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        delete all credential
        '''
        Credential.credential_list.remove(self)
    def delete_all():
        Credential.credential_list=[]
    @classmethod
    def delete_by_account(cls,name):
        for credential in cls.credential_list:
            if credential.name==name:
                Credential.credential_list.remove(credential)
    @classmethod   
    def find_by_username(cls,name):
        for credential in cls.credential_list:
            if credential.name==name:
                return credential
   
  
    @classmethod
    def display_all(cls):
        return cls.credential_list