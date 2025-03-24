#!/bin/bash
#Instalando e atualizando o python no arquivo calc.py
sudo apt update
sudo apt install python3

python3 /home/pichau/ex_calculadora/execute.py

echo 'Complementos para executar a calculadora!'
echo "Você está em $PWD"
