#### What is Docker ?
Docker is a software platform that allows you to build, test, and deploy applications quickly. Docker packages software into standardized units called containers that have everything the software needs to run including libraries, system tools, code, and runtime. Using Docker, you can quickly deploy and scale applications into any environment and know your code will run.
#### why we used Docker ?
1. Skip the code faster :- Docker users on average ship software 7x more frequently than non-Docker users
2. Standerdized operation :- Small containerized applications make it easy to deploy, identify issues, and roll back for remediation.
3. Seamlessly Move :- Docker-based appliaction can be seamlessly move from the local development to the product base 
4. Save Money :- Docker container help us to run more code on each server, improve your utilization and save money.
#### what is the difference between virtualization and containerization ?
![image](https://user-images.githubusercontent.com/96170504/219357213-34c5f4f6-42ad-48be-a1ac-2f10c4b08fd1.png)
## Basic Commands
1. docker images
![image](https://user-images.githubusercontent.com/96170504/219027853-9bea2681-f7fe-4aae-aa6c-5188956ca860.png)
2. docker pull ubuntu:latest
![image](https://user-images.githubusercontent.com/96170504/219028328-aa02ff87-4a55-497e-aa93-fe912efea00c.png)
3. docker images --no-trunc
![image](https://user-images.githubusercontent.com/96170504/219028522-95ad1c37-5711-4475-a771-3bd375b7377e.png)
#### Steps after creating Dockerfile
docker build .
docker container run -it --name namedockerfile dockerid  [this command is basically used run the container in the interactive mode]
#### what is dockerfile, Image and container ?
![image](https://user-images.githubusercontent.com/96170504/219370769-1bf6c571-be4b-4b9d-bda8-98ed297498f6.png)
**DockerFile** is a set of instuction file which help use in producing the Docker Image.
**Image** It is a kind of read-only template crafted with source code, libaries, external dependencies, tools, and other miscellaneous files that are needed for any software application to run successfully on any platform or OS.  
**container** A container is nothing but a box that has the ability to run the docker image templates. 
A container can also be considered as a cohesive software unit that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another.  
#### Docker Image vs Containers
1. The key difference between a Docker image Vs a container is that a Docker image is a read-only immutable template that defines how a container will be realized. A Docker container is a runtime instance of a Docker image that gets created when the $ docker run command is implemented.  
2. Before the docker container can even exist docker templates/images are built using $ docker build CLI. 
3. Docker image templates can exist in isolation but containers can't exist without images.  
4. So docker image is an integral part of containers that differs only because of their objectives which we have already covered.  
5. Docker images can’t be paused or started but a Docker container is a run time instance that can be started or paused. 
Command to check the **process id** :- **ps -ef**
#### How to push ur image in the repository?
1. docker login [provide ur username and password of github].
2. docker tag imageid repositoryname:v1
3. check the docker images updated with ur tag.
4. docker push repositoryname:tag
