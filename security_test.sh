#!/bin/sh


ls -la /etc
ls -la ../
ls -la ../../
echo 'I am bad' > ../bad.txt
echo 'I am bad' > ../../bad.txt
echo 'I am bad' > ../../../bad.txt
echo 'I am bad' > /bad.txt
echo 'I am bad' > /etc/bad.txt
