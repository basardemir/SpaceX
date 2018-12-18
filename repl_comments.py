from hashlib import sha256

cmnt_list = []

def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

while True:
    pswrd = input('Enter your password: ')
    hsh1 = create_hash(pswrd)
    if hsh1 == "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92":
        comment = input("Enter your comment: ")
        cmnt_list.append(comment)
        print("Previously entered comments: ")
        j = 0
        while len(cmnt_list) >= j+1:
            print(str(j+1) + ". " + cmnt_list[j])
            j = j+1
    else:
        print("I am sorry I can't let you do that.")
