import subprocess 


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

def inject_route(prefix: str)->None:
    """quickly adds routes into the table of r01"""
    cmd = f"docker exec r01 gobgp \
            global rib add -a ipv4 {prefix} \
            nexthop 192.50.50.10 identifier 20"
    subprocess.Popen(
        cmd, 
        shell=True, 
        stdout=subprocess.PIPE
    ).stdout.read() 

def main():
    for prefix in prefixes:
        inject_route(prefix)

if __name__ == "__main__":
    main()
