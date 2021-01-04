# TalentQL assessment Tasks

---

As part of completing the tasks I've created three Github Action workflows that automate the required for the tasks in this assessment. You can the workflows by clicking on the **Actions** tab of the of the Github menu. Below is a brief description of the workflows

**Terraform CI:** pipeline runs basic terraform commands `fmt`, `init` `plan` on push and pull requests. Terraform `apply` is to run conditionally when push to `main` branch.

**Integration Test** The uses `terratest` present `test` folder to run test againt the `IaC` code. The test will provision resources on GCP (Network, Subnetwork, Firewall rules, Compute engine VM), install apache server, modify the content of the default index.html to contain **Hello world** (That's what we will be testing for), run curl on the external IP address of the server. After the test succeed, Terraform destroy/clean all the resources

**json2xml-pipeline:** The workflow automate all the step required to build docker images for encryption and decryption, start the containers, convert the json file in the encryption-container to xml file and encrypt the file. It then place the file in the /shared directory (docker volume mount) where it is accessible by the decryption container. The workflow the start the decryption container, retrieve the file from the `/shared` directory, decrypt it and place it in the current working directory.

You can look at the workflows output to see all that happened. The descriptions below will help with the setup instructions if it is necessary to run them in your local environmet.

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

- `docker-compose up`

Thereafter, you can follow the steps outline above for starting, stoping, encrpting, and decrypting files needed

---

## Task 2: Build Infrastucture as Code (IaC) 

This section provides a decription of how  to set the IaC (Infrastructure as Code) configuration for provision a VM in GCP and installing Apache server using Terraform. To begin clone the repository `git clone https://github.com/tutugodfrey/tql-infra`. The IaC configuration is contained within the `./tfinfra` directory. The directory contains two folders `infra` which holds the actual Terraform configurations for building out the infrastructures in GCP and `test` which uses `terratest` to test the configuration. 

CI pipeline has been configured to run and test the deployments upon push to github. Please see the `Actions` sections of the repo to view the jobs that has ran. If will like to test the deployment manually, please follow the steps below

`git clone https://github.com/tutugodfrey/tql-infra` clone the repository

`cd tql-infra/tfinfra/test` change directory to the test folder

`go test` run the test. 

Please note you will need to update the project name variable in tfinfra/infra/main.tf to a project in your GCP account to for the test to run. Also, your GLOUD SDK need to have Terraform and Golang properly configured to ensure you don't have an issue running the test.

# Install packages 

If you encounter an error that any of the following packages are missing, please run the command to install them and run the test again

`go get github.com/gruntwork-io/terratest/modules/http-helper`

`go get github.com/jinzhu/copier`

