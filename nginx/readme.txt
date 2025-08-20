download image and send to server
==1.download common image ====
1. docker pull nginx:latest
2. docker save -o nginx_latest.tar nginx:latest

3. send to server
scp "nginx_latest.tar" carenk@10.161.81.13:~/00_enviroment/00_docker_images_tar/

4. docker load -i nginx_latest.tar


===2.define:customirize image: dockerfile=========
files to use: conf file


====3.then is container composefile====

==4. send all file to server:====
scp -r . carenk@10.161.81.13:~/00_enviroment/01_ngnix/