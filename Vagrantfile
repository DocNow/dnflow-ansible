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

# docnow server
  config.vm.define "docnow" do | docnow |
    docnow.vm.hostname = "docnow-app1.dev"
    docnow.vm.network :private_network, ip: "192.168.60.14"
    docnow.vm.provision "ansible_local" do |ansible|
        ansible.playbook = "docnow.yml"
        ansible.sudo = true
        ansible.verbose = ""
    end
  end
  
  docnowvm.vm.provider :aws do |aws, override|
      keypair = "#{ENV['KEYPAIR_NAME']}"
      keypair_filename = "#{ENV['KEYPAIR_FILE']}"
      override.vm.box = "aws_dummy"
      override.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"
      override.vm.box_check_update = false
      aws.access_key_id = ENV['AWS_ACCESS_KEY']
      aws.secret_access_key = ENV['AWS_SECRET_KEY']
      aws.keypair_name = keypair
      aws.ami = "ami-df0607b5" # Ubuntu Trusty LTS
      aws.region = "us-east-1"
      aws.instance_type = "t2.small"
      aws.security_groups = ["default_vpc_web_vt_ssh"]
      #aws.associate_public_ip = true
      override.ssh.username = "ubuntu"
      override.ssh.private_key_path = "#{keypair_filename}"
      aws.tags = {
        'Name' => "Docnow #{keypair}"
      }
  end
end
