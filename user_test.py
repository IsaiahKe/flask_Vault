import unittest
from user import User
class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user=User('isaiah','morara','1234')
        self.assertEqual(self.new_user.fname,'isaiah')
        self.assertEqual(self.new_user.sname,'morara')
        self.assertEqual(self.new_user.email,self.new_user.fname+self.new_user.sname+'@gmail.com')
        self.assertEqual(self.new_user.password,'1234')

    def test_add_user(self):
        self.new_user.add_user()
        self.assertEqual(len(User.user_list),1)
   
        
    def tearDown(self):
        User.user_list=[]
     
  
if __name__ =='__main__':
    unittest.main()
