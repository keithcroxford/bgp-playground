# BGP Routing Playground
This repo provide an easy way to experiment with BIRD Internet Routing Daemon, and GoBGP. 

# Containers
- r01 = GoBGP
- r02 = GPBGP
- routesvr = BIRD


# How to 
1. Make sure you have a recent version of docker installed
2. run `docker compose up -d` 
3. commands can be executed within the containers using
   - routesvr: use `docker exec -it routesvr birdc` to access the BIRD CLI. From there you can execute commands normally. 
   - r02: use `docker exec r02 gobgpc <command>`
   - r03: use `docker exec r01 gobgp <command>`
