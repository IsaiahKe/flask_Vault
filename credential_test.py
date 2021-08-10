import unittest
from credential import Credential
class TestCredential(unittest.TestCase):
    '''
    test  class instance
    '''
    def setUp(self):
        self. new_cred= Credential('facebook','morara','12345')
        self.assertEqual(self.new_cred.name,'facebook')
        self.assertEqual(self.new_cred.username,'morara')
        self.assertEqual(self.new_cred.passcode,'12345')

    
    def tearDown(self):
        Credential.credential_list=[]
        
    def test_add_credential(self):
        cred=Credential('isaiah','morara','keoye')
        cred.add_credential()
        self.assertEqual(len(Credential.credential_list),1)
    def test_delete_all(self):
        self.new_cred.add_credential()
        Credential.delete_all()
        self.assertEqual(len(Credential.credential_list),0)
        
    def test_find_by_username(self):
        self.new_cred.add_credential()
        new=Credential('facebook','morara','123445')
        new.add_credential()
        found=Credential.find_by_username('facebook')
        self.assertEqual(found.username,new.username)
    
    def test_display_all(self):
        cred= Credential.display_all()
        self.assertEqual(cred,Credential.credential_list)
if __name__=='__main__':
    unittest.main()
   