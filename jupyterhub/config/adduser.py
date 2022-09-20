import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', type=str, help='user name')
parser.add_argument('-p', type=str, help='user password')
parser.add_argument('--no_create_env', action="store_true", default=False, help='do not create conda env automatically for current user')
parser.add_argument('--no_create_home', action="store_true", default=False, help='do not create home folder for current user')
args = parser.parse_args()

user = args.u
psw = args.p

# create new user
if args.no_create_home:
    os.system(f'useradd --no-log-init --shell /bin/bash {user}')
else:
    os.system(f'useradd --create-home --no-log-init --shell /bin/bash {user}')

os.system(f'adduser {user} sudo')
os.system(f'echo "{user}:{psw}" | chpasswd')

if not args.no_create_env:
    os.system(f'su - {user} -s /bin/bash /create_env.sh')