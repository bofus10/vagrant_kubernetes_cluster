ENV['VAGRANT_NO_PARALLEL'] = 'yes'
IMAGE_NAME = "centos/7"

##########################
##### USER SETTINGS  #####
##########################
N_Instances = 3
NETWORK = "170.10.10"
##########################
##########################

Vagrant.configure("2") do |config|
    config.ssh.insert_key = false
    #VBox shared folder definition
    config.vm.synced_folder ".", "/vagrant", type: "virtualbox"
    #VBguest plugin install if not present
    config.vagrant.plugins = {"vagrant-vbguest" => {"version" => "0.30.0"}}
    #From VBGuest >0.22 allow_kernel_upgrade is needed
    config.vbguest.installer_options = { allow_kernel_upgrade: true }

    config.vm.provider "virtualbox" do |vb|
        vb.memory = 4096
        vb.cpus = 4
    end

    # Setup of K8s Master node
    config.vm.define "k8s-master" do |master|
        master.vm.box = IMAGE_NAME
        master.vm.network "private_network", ip: "#{NETWORK}.10"
        master.vm.hostname = "k8s-master"
        master.vm.provision "ansible_local" do |ansible|
            ansible.playbook = "kubernetes-setup/master-playbook.yml"
            ansible.extra_vars = {
                hostname: "k8s-master",
                network: NETWORK,
                node_ip: "#{NETWORK}.10",
                n_nodes: N_Instances,
            }
        end
    end

    # Setup of K8s Worker nodes
    (1..N_Instances).each do |i|
        config.vm.define "node-#{i}" do |node|
            node.vm.box = IMAGE_NAME
            node.vm.network "private_network", ip: "#{NETWORK}.#{i + 10}"
            node.vm.hostname = "node-#{i}"
            node.vm.provision "ansible_local" do |ansible|
                ansible.playbook = "kubernetes-setup/node-playbook.yml"
                ansible.extra_vars = {
                    hostname: "k8s-master",
                    network: NETWORK,
                    node_ip: "#{NETWORK}.#{i + 10}",
                    n_nodes: N_Instances,
                }
            end
        
            node.trigger.after :up do |trigger|
                trigger.name = "Node up"
                trigger.run_remote = {inline: "echo \"`date` `hostname` Ready\" >> /vagrant/nodes"}
            end
        end
    end
   
end