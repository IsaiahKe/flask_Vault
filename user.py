
class User():
    '''
    create class User
    '''

    def __init__(self,fname,sname,password):
        self.fname=fname
        self.sname=sname
        self.email=fname+sname+'@gmail.com'
        self.password=password
    user_list=[] #create user to handle data 
    def add_user(self):
        '''
        Add user to list
        '''
        User.user_list.append(self)
        
    @classmethod
    def get_password(cls,mail):
        '''
        display user password
        '''
        for user in cls.user_list:
            if user.email == mail:
                return user.password
            return 'No Match'
        
