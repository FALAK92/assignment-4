#You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!
#This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.
#For example, using a hash function called SHA256(...) something as simple as
#hello


from hashlib import sha256

# ANSI escape codes for colors
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def hash_password(password):
    """🔒 پاس ورڈ کو SHA-256 میں ہیش کرتا ہے۔"""
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password_to_check):
    """✅ ای میل اور پاس ورڈ کو چیک کرتا ہے کہ وہ محفوظ شدہ ڈیٹا سے ملتے ہیں یا نہیں۔"""
    if email in stored_logins and stored_logins[email] == hash_password(password_to_check):
        print(f"{GREEN}✅ Access Granted! Welcome {email}! 🚀{RESET}")
        return True
    else:
        print(f"{RED}❌ Access Denied! Incorrect Email or Password.{RESET}")
        return False

def main():
    """📌 یوزر ان پٹ لے کر پاس ورڈ چیک کرتا ہے۔"""
    stored_logins = {
        "user1@example.com": hash_password("hello123"),
        "admin@secure.com": hash_password("adminpass"),
        "guest@site.com": hash_password("guest123")
    }

    print("🔑 Welcome to Secure Login System!\n")

    email = input(f"{YELLOW}📧 Enter your email: {RESET}")
    password = input(f"{YELLOW}🔑 Enter your password: {RESET}")

    login(email, stored_logins, password)

if __name__ == '__main__':
    main()
