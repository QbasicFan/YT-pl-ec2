# YT-pl-ec2
# How to deploy this app on EC2

## Create an instance and allow connections

![Screenshot](/image/set01.png?raw=true "EC2 test")

![Screenshot](/image/set02.png?raw=true "EC2 test")

![Screenshot](/image/set03.png?raw=true "EC2 test")

1
sudo apt-get update

2
git clone https://github.com/QbasicFan/YT-pl-ec2.git

3
cd into app dir 

4
sudo apt install python3-pip -y

5
pip install django

6
python3 manage.py runserver 0.0.0.0:9000
