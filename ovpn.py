import os


def config_ovpn():
    users = os.environ['users'].split(';')
    user = users[0].split(',')
    secret = user[0] + "\n" + user[1]
    with open('secret.txt', 'w') as f:
        f.write(secret)

    routing_config = """route-nopull
    route-metric 150
    max-routes 1000
    route 202.120.127.100 255.255.255.255
    route 202.120.127.250 255.255.255.255
    """
    with open('.github/vpn/config.ovpn', 'r') as f:
        content = f.read()
        content = content.replace('# ROUTING CONFIG', routing_config)
        with open('.github/vpn/config.ovpn', 'w') as fa:
            fa.write(content)


if __name__ == '__main__':
    config_ovpn()
