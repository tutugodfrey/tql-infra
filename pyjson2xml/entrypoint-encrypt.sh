#! /bin/bash

echo VIEWING CONTENT OF JSON FILE;
cat myjson.json;
./json2xml.py myjson.json;
cat myjson.xml;
echo ENCRYPTING THE CONVERTED XML FILEL;
./encrypt.py myjson.xml;
cat /shared/myjson.xml;
echo THE FILE IS NOW ENCRYPTED AND SHARED FOR DECRYPT CONTAINER TO ACCESS;
