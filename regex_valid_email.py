#5.	Validate a simple email address pattern.
#	Task: Create a regex to validate email addresses. The email must follow the pattern username@domain.extension.
#	Input: "test@example.com"
#	Expected Output: "Valid Email"
#	Input: "invalid-email.com"
#	Expected Output: "Invalid Email"
import re
def validate_email(email):
    pattern = r'[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return "valid Email"
    else:
        return "Invalid Email"
    
        
print(validate_email("test@example.com"))
print(validate_email("invalid-email.com"))
    