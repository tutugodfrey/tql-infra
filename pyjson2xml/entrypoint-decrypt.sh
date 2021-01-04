#! /bin/bash

echo VIEWING THE CONTENT OF THE CURRENT DIRECTORY;
ls;
echo VIEWING THE CONTENT OF THE ENCRYPTED XML FILE;
cat /shared/myjson.xml;
./decrypt.py /shared/myjson.xml;
echo THE ENCRYPTED FILE IS NOW DECRYPTED;
ls;
echo VIEWING THE CONTENT OF THE DECRYPTED XML FILE;
cat myjson.xml;
