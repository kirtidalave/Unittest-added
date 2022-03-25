import unittest

def login_verification(username, password):
    if username == "admin" and password =="12345":
        return True
    else:
        return False


def login(param, param1):
    pass


class verification(unittest.TestCase):
    def test_login(self):
        result = login("admin","12345")
        self.assertTrue(result)







if __name__=="__main__":
        unittest.main()