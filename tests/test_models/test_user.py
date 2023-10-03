#!/usr/bin/python3
from tests.test_models.test_base_model import test_basemodel as Test_BaseModel
from models.user import User


class test_User(Test_BaseModel):
    """Test user class """
    
    def __init__(self, *args, **kwars):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User
        
    def test_first_name(self):
        new = self.value()
        new.first_name = "Brian"
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        new = self.value()
        new.last_name = "James"
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        new = self.value()
        new.email = "brian@gmail.com"
        self.assertEqual(type(new.email), str)

    def test_password(self):
        new = self.value()
        new.password = "brian1234"
        self.assertEqual(type(new.password), str)
