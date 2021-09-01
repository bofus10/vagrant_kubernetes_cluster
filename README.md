# Evolution Challange

Following code is to present to Evolution team 

## Technologies used 🛠️
On this project I used the following technology tools:
* Vagrant
* VirtualBox
* Ansible
* Kubernetes 1.21
  * Calico CNI
  * MetalLB LoadBalancer
* Docker
* Python
* Grafana
* Prometheus
* Kafka
  * Kafkacat Pod for testing purposes

## Setup 🔧
* Install Vagrant and VirtualBox
* Install Vagrant vbguest Plugin for VirtualBox: _vagrant plugin install vagrant-vbguest_

On the Vagrant file you will can specify the Network you k8s cluster will run on and the Number of workers to create.

## Usage 📋
* Clone the Repository
* Run vagrant up

Vagrant will create 1 k8s master and N workers, will deploy kubernetes with local_ansible.
After the master and the workers are up, a Second Phase will be run on the Master, where the following steps will occur:
* Build Docker Kafka Image with Prometheus JMX Plugin
* Build Docker Consumer and Producer Image, which will contain a Python script emulating traffic between kafka Topics
* Deploy kafka containers and settings on k8s
* Deploy Grafana and Prometheus on K8s
* Set grafana LoadBalancer Service on $NETWORK.241 (by default 170.10.10.241:3000)
* Deploy a Producer Pod 
* Deploy a Consumer Pod

## License 📄
Project License type: GPL-3.0 License - Check [LICENSE](LICENSE) file for more details.
