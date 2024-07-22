def check_password(password):
    
    error_msg =[]

    if (len(password) >= 8 and
        any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        password[-1].isdigit()):
         
        return error_msg
    
    else:

        if len(password) <8:
            error_msg.append("Password size is less than 8")
        
        if not any(c.islower() for c in password):
            error_msg.append("There is no lower case letter present")
        
        if not any(c.isupper() for c in password):
            error_msg.append("There is no upper case letter present")

        if password[-1].isdigit() == False:
            error_msg.append("Last index is not a numeric value")

    return error_msg
    