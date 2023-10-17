import subprocess 
import logging 
import random
from prefixes import prefix_list
from bgphosts import bgp_host_list

logging.basicConfig(
    encoding='utf-8',
    format='%(levelname)s:%(message)s',
    level=logging.INFO
)



def inject_route(prefix: str, bgp_host: str)->None:
    """ this function quickly adds routes into the GoBGP hosts"""

    if bgp_host not in bgp_host_list:
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
    for prefix in prefix_list:
        inject_route(prefix,random.choice(bgp_host_list))

if __name__ == "__main__":
    main()
