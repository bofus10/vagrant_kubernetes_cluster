# Kubernetes Cluster Deployment + kafka | grafana | prometheus

Following code is intented as test practice, code will deploy a kubernetes cluster (master|worker nodes) using vagrant and virtualbox. 
Optionally will deploy kafka, grafana, prometheus

## Technologies used 🛠️
On this project I used the following technology tools:
* Vagrant
* VirtualBox
* Ansible
* Kubernetes 1.21
  * Calico CNI
  * MetalLB LoadBalancer
* Docker
  * Docker-Distribution
* Python
* Grafana
* Prometheus
* Kafka
  * Kafkacat Pod for testing purposes

## Setup 🔧
* Clone the Repository
* Install Vagrant and VirtualBox
* Install Vagrant vbguest Plugin for VirtualBox:~~vagrant plugin install vagrant-vbguest~~
  * Vagrant will ask to install version 0.30.0 if not present on first run
* If you dont want all the second phase deployments that include grafana, kafka and prometheus, remove the second_phase.yml from the pwd.

On the Vagrant file you will specify the Network you k8s cluster will run on and the Number of workers to create.

## Usage 📋
Optional: Edit network and number of nodes
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

Once all is deployed, you can access Grafana monitoring webpage via 170.10.10.241:3000

User/Pass is default admin/admin

Under Dashboards -> Manage -> Default there are some Dashboards reporting metrics of Pods, Cluster, etc
  * -> Kubernetes / Compute Resources / Cluster
  * -> Kubernetes / Compute Resources / Namespace (Pods)
  * -> Kubernetes / Compute Resources / Node (Pods)
  * -> Kubernetes / Compute Resources / Workload
  * -> Kubernetes / Networking / Namespace (Pods)
  * -> Kubernetes / Networking / Pod
  * -> Kubernetes / Kubelet
  * -> Kafka / Workload
  * And more...

## License 📄
Project License type: GPL-3.0 License - Check [LICENSE](LICENSE) file for more details.
