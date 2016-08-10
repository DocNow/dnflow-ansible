#-*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
# General Vagrant VM
  config.vm.box = "ubuntu/trusty64"
  config.ssh.insert_key = false
  config.vm.provider :virtualbox do | v |
    v.memory = 2048
  end

# dnflow server
  config.vm.define "dnflow" do | dnflow |
    dnflow.vm.hostname = "dnflow-app1.dev"
    dnflow.vm.network :private_network, ip: "192.168.60.14"
    dnflow.vm.provision "ansible_local" do |ansible|
        ansible.playbook = "docnow.yml"
        ansible.sudo = true
        ansible.verbose = ""
    end
  end

end
