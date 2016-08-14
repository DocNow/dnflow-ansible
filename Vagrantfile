#-*- mode: ruby -*-
# vi: set ft=ruby :

# To install under AWS you need to have the vagrant-aws provider plugin installed.
# You can install this using the following command:
#
#   vagrant plugin install vagrant-aws
#
# If no "--provider" is specified during "vagrant up" then the default
# (VirtualBox) provider will be used.

Vagrant.configure(2) do |config|

  # Ansible provisioner default settings
  config.vm.provision :ansible_local do |ansible|
    ansible.playbook = "docnow.yml"
    ansible.sudo = true
    ansible.verbose = ""
  end

  # dnflow server
  config.vm.define :dnflow do |dnflow|
    dnflow.vm.hostname = "dnflow"

    dnflow.vm.provider :virtualbox do |vb, override|
      override.vm.box = "ubuntu/trusty64"
      override.vm.network :private_network, ip: "192.168.60.24"
      # Customize the amount of memory on the VM:
      vb.memory = "2048"
    end

    dnflow.vm.provider :aws do |aws, override|
      override.vm.box = "aws_dummy"
      override.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"
      override.vm.box_check_update = false
      aws.aws_dir = ENV['HOME'] + "/.aws/"
      aws.ami = "ami-df0607b5" # Ubuntu Trusty LTS
      aws.region = "us-east-1"
      aws.instance_type = "t2.small"
      #aws.associate_public_ip = true
      override.ssh.username = "ubuntu"
      aws.tags = {
        'Name' => "dnflow }"
      }
    end
  end
end
