# tql-infra
IAC provisioning with terraform and docker-compose

## Task 1: Deploy python scripts to convert json file to xml file

This task deploys two containers to encrypt and decrypt an xml file.

### Container 1: encrypt-container

The container contains a python script to convert a json file to a xml file, encrypt the file and place the encrypted file in a shared directory `/shared` where it can be accessible to decrypt-container

### Container 2: decrypt-container

This container contains a python script to decrypt an encrypted file located in the shared directory `/shared`.

### Building the docker images and starting the containers

To build the docker images for the containers run the following commands

`docker build -t encrypt-img .` build the encrypt-container

`docker build -t decrypt-img -f Dockerfile_dec` build the decrypt container

To start the containers, encrypt and decrypt files follow the steps below

**Encryption**

`docker run -it -v datadir:/shared --name encrypt-container encrypt-img` start the container in an interactive bash terminal

A json file is present in this current directory. Also, you can create any json file

To convert the json file to xml file and encrypt it run the following commands

- `./json2xml.py myjson.json` this will create a `.xml` with the name in the current directory. run `ls` to view files, run `cat myjson.xml` to see the content of the file

- `./encrypt.py myjson.xml` this will encrypt the `.xml` and place it in the shared directory `/shared` so it is accessible to the decrypt-container

You can exit the container by simple typing exit at the terminal prompt

Subsequently, you start the container and encrypt file by running the following commands

- `docker container start encrypt-container` start the enrypt-container

- `docker exec -it encrypt-container bash` start an interactive terminal where you can perform the conversion and encryption steps above or

- `docker exec -it encrypt-container ./json2xml.py myjson.json` to convert json to xml

- `docker exec -it encrypt-container ./encrypt.py myjson.xml` to encrypt the file and place it in `/shared` directory


**Decryption**

- `docker run -it --name decrypt-container -v datadir:/shared decrypt-img` start the decrypt container in an interactive bash terminal

To decrypt any file present in the shared directory the command should be in the form `./decrypt.py filename.xml`. `decrypt.py` script will look for the filename in the shared directory `/shared`

- `./decrypt.py myjson.xml` will decrypt the myjson.xml file and place it in the current directory

You can exit the container by simple typing `exit` at the terminal prompt

subsequently, you can start the container by running the following command

- `docker start decrypt-container`

- `docker exec -it decrypt-container bash` to exec into the container, where you would be able to decrypt any file present in the `/shared` directory or 

- `docker exec -it decrypt-container ./decrypt.py myjson.xml` to run the decrypt script on available file without entering into the container

### Using shell script

A shell script `deploy.sh` has been provisioned in the `pyjson2xml` directory to build the images and contains functions to start the containers. Follow the steps below to use the script

- `. ./deploy.sh` will build the images for the two containers `encrypt-img` and `decrypt-img`

- `start_encrypt_container` will start the encrypt container. Thereafter you can following the steps outlined above for performing the conversion and encryption

- `start_decrypt_container` will start the decrypt container in interactive bash terminal. Thereafter you can follow the steps outlined above for performing decryption

### Using docker compose

You can also use docker compose to deploy the container services. Following steps shows how to deploy using docker-compose

- `docker-compose compose.yml`

Thereafter, you can follow the steps outline above for starting, stoping, encrpting, and decrypting files needed


## Build Infrastucture as Code (IaC) 

# Install packages
`go get github.com/gruntwork-io/terratest/modules/http-helperz`
`go get github.com/jinzhu/copier`
