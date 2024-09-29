#!/bin/bash
sudo apt-get update
sudo apt-get install -y software-properties-common
sudo add-apt-repository ppa:alex-p/tesseract-ocr -y
sudo apt-get update
sudo apt-get install -y tesseract-ocr
sudo apt-get install -y libtesseract-dev
