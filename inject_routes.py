import subprocess 
import logging 
import random

logging.basicConfig(
    encoding='utf-8',
    format='%(levelname)s:%(message)s',
    level=logging.INFO
)


prefixes = [
    "4.0.0.0/9",
    "4.55.0.0/16",
    "8.0.0.0/12",
    "8.0.0.0/9",
    "8.4.162.0/24",
    "8.5.160.0/24",
    "8.6.180.0/24",
    "8.10.144.0/22",
    "8.10.167.0/24"
]

bgp_hosts = [
    "r01",
    "r02"
]

def inject_route(prefix: str, bgp_host: str)->None:
    """ this function quickly adds routes into the GoBGP hosts"""

    if bgp_host not in bgp_hosts:
        logging.warn(f"{bgp_host} is not a valid BGPHost!")
        return False

    cmd = f"docker exec {bgp_host} gobgp \
            global rib add -a ipv4 {prefix} \
            nexthop 192.50.50.10 identifier 20"

    child = subprocess.Popen(
        cmd, 
        shell=True, 
        #stdout=subprocess.PIPE
    ).wait()

    if child == 0:
        logging.info(f"{prefix} add to {bgp_host}") 
        return True
    else: 
        return False

def main():
    """ entry point into the script """
    for prefix in prefixes:
        inject_route(prefix,random.choice(bgp_hosts))

if __name__ == "__main__":
    main()
