# PRO690N1A - DevOps Project2 & Final Exam
PRO690N1A – Introduction to DevOps Practices and Principles

Kevin Hutchison and Akshaykumar Paladiya

Project 2 & Final Exam

## Project Setup
```bash
git clone git@github.com:kevinmenotyou/devops_project2.git
```

### Diagram
Install Python3 (e.g. 3.10)

```bash
cd "<your devops_project2 root directory>"
py -m venv diagram/env
source diagram/env/Scripts/activate
pip install -r ./diagram/requirements.txt
```

Install Chocolatey https://chocolatey.org/

Install graphviz
```bash
choco install graphviz
```

### Terraform
//TODO

### Docker
//TODO

### Jenkins
//TODO

### Ansible

#### Ubuntu
```bash
sudo apt update
sudo apt install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt update
sudo apt install ansible
sudo apt install git-all

curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
az login --use-device-login
```