import os
SHU_DOMAINS = [
    'speedtest.shu.edu.cn',
    'selfreport.shu.edu.cn',
    'newsso.shu.edu.cn',
    'oauth.shu.edu.cn',
    'services.shu.edu.cn',
    'xk.autoisp.shu.edu.cn',
    'xk.shu.edu.cn',
]
SHU_IPS = []


def get_ip(domain):
    ip = os.popen("dig +short {}".format(domain)).read().strip()
    return ip


def config_ovpn():
    global SHU_IPS
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
        SHU_IPS.append(get_ip(domain))
    SHU_IPS = list(set(SHU_IPS))
    for ip in SHU_IPS:
        routing_config += "\n"
        routing_config += "route %s 255.255.255.255" % ip
    print(routing_config)

    with open('.github/vpn/config.ovpn', 'r') as f:
        content = f.read()
        content = content.replace('# ROUTING CONFIG', routing_config)
        with open('.github/vpn/config.ovpn', 'w') as fa:
            fa.write(content)


if __name__ == '__main__':
    config_ovpn()
