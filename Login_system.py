
system = {'name1':'pwd1', 'name2':'pwd2'}
def newusers():
    name = input('enter a name: ')
    while name in system:
        print('User already exists! Try another.')
        name = input('enter a name: ')
    else:
        pwd = input('set the password:')
        system[name] = pwd

def oldusers():
    print('Enter the  username and password')
    name = input('username: ')
    pwd = input('password: ')
    if system.get(name) == pwd:  
        print(name, 'welcome back ') 
    else:  
        print('login incorrect')

def login():
    option = """
            (N)ew User Login 
            (O)ld User Login
            (E)xit\n """
    while(True):
        op = input('Enter the option: ')
        if(op == 'N' or op == 'n'):
            newusers()
        elif(op == 'O' or op == 'o'):
            oldusers()
        elif(op == 'E' or op == 'e'):
            print('Goodbye!')
            break
        else:
            print('Unknown option!\n')
            print(option)

if __name__ == '__main__':  
    login()  
    