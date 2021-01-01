#! /bin/bash

docker volume create sharedir;

docker build -t encrypt-img .;

docker build -t decrypt-img -f Dockerfile_dec .;

function start_encrypt_container () {
  docker run -it --name encrypt-container -v sharedir:/shared encrypt-img;

  if [[ $? != 0 ]]; then 
     docker start encrypt-container;
     sleep 4
     docker exec -it encrypt-container bash;
  fi
}

function start_decrypt_container () {
  docker run -it --name decrypt-container -v sharedir:/shared decrypt-img;
  if [[ $? != 0 ]]; then
     docker start decrypt-container;
     sleep 4
     docker exec -it decrypt-container bash;
  fi
}




