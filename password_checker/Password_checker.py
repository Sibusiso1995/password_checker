import re

#pswd = input("Enter a password: ")
def password_is_valid(password):
    # checking condintion 1
    if len(password) == 0:
        raise Exception("password should exist")
    
    else: 
        # checking condition 2
        if len(password) <= 8:
            raise Exception("password should be longer than than 8 characters")
      
        else:
            # checking condition 3
            if not re.search("[a-z]",password):
                raise Exception("password should have at least one lowercase letter")
                
            # checking condition 4
            elif not re.search("[A-Z]", password):
                raise Exception("password should have at least one uppercase letter")
            
            # checking condition 5
            elif not re.search("[0-9]", password):
                raise Exception("password should at least have one digit")

            else:
                # checking condition 6
                if not re.search("[{ % & * / !']", password):
                    raise Exception("password should have at least one special character")

def password_is_ok(password):
    condition = 0
    if len(password) <= 8:
        return False

    else:
        # condition 3
        if re.search("[a-z]",password):
            condition += 1
        
        # condition 4
        if re.search("[A-Z]", password):
            condition += 1

        # checking condition 5
        if re.search("[0-9]", password):
            condition += 1
            
        # checking condition 6
        if re.search("[{ % & * / !']", password):
            condition += 1

            return True
        