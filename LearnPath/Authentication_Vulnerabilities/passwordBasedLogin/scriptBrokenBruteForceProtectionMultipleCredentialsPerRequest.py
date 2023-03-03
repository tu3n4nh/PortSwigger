passwords = open('../shortlist/passwords.txt', 'r').read().splitlines()

new_passwords = open('passwords.txt', 'w')
new_passwords.write('{"username":"carlos",')
# for password in passwords:
#     new_passwords.write(f'"password":"{password}",\n')
# new_passwords.write('}')
new_passwords.write('"password":[')
for password in passwords:
    new_passwords.write(f'"{password}",')
new_passwords.write('],')