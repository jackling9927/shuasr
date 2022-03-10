import os
SHU_DOMAINS = [
    'speedtest.shu.edu.cn',
    'selfreport.shu.edu.cn',
    'newsso.shu.edu.cn',
    'xk.autoisp.shu.edu.cn',
]


def get_ip(domain):
    ip = os.popen("dig +short {}".format(domain)).read().strip()
    return ip


def config_ovpn():
    users = os.environ['users'].split(';')
    user = users[0].split(',')
    secret = user[0] + "\n" + user[1]
    with open('secret.txt', 'w') as f:
        f.write(secret)

    routing_config = """route-nopull
    route-metric 150
    max-routes 1000
    """
    for domain in SHU_DOMAINS:
        routing_config += "\n"
        routing_config += "route %s 255.255.255.255" % get_ip(domain)

    with open('.github/vpn/config.ovpn', 'r') as f:
        content = f.read()
        content = content.replace('# ROUTING CONFIG', routing_config)
        with open('.github/vpn/config.ovpn', 'w') as fa:
            fa.write(content)


if __name__ == '__main__':
    config_ovpn()
