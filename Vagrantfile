# -*- mode: ruby -*-
# vi: set ft=ruby :
require 'yaml'

### Look for a settings file
def load_settings(file)
  dir = File.dirname(File.expand_path(__FILE__))
  if !File.exist?("#{dir}/provider/#{file}.yml")
    FileUtils.cp("#{dir}/provider/example.#{file}.yml", "#{dir}/provider/#{file}.yml") 
    if !File.exist?("#{dir}/provider/#{file}.yml")
      raise "Settings file not found! Please copy provider/example.#{file}.yml to vagrant/#{file}.yml and try again."
    end
  end
  YAML.load_file "#{dir}/provider/#{file}.yml"
end

### install required plugins
unless Vagrant.has_plugin?("vagrant-triggers") and Vagrant.has_plugin?("vagrant-aws")

  system("vagrant plugin install vagrant-triggers")
  system("vagrant plugin install vagrant-aws")
  puts "Dependencies installed, please try the command again."
  exit
end

VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

### Global Provisions

  config.vm.provision :ansible_local do |ansible|
    ansible.playbook = "docnow.yml"
    ansible.become = true
    ansible.verbose = ""
  end

  # Fix 'no tty' errors
  config.vm.provision "fix-no-tty", type: "shell" do |shell|
    shell.privileged = false
    shell.inline = "sudo sed -i '/tty/!s/mesg n/tty -s \\&\\& mesg n/' /root/.profile"
  end

### Virtualbox Provider
  config.vm.provider :virtualbox do |provider, override|
    settings = load_settings 'virtualbox'
    provider.name = settings['name']
    provider.cpus = settings['cpus']
    provider.memory = settings['memory']
    override.vm.box = settings['box']
   # override.vm.network "public_network", bridge: "en1: Wi-Fi (AirPort)"
    override.vm.network :private_network, ip: "192.168.60.14"
 end

### AWS provider
  config.vm.provider :aws do |provider, override|
    settings = load_settings 'aws' 
    provider.access_key_id = settings['access_key_id']
    provider.secret_access_key = settings['secret_access_key']
    provider.keypair_name = settings['keypair_name']
    provider.ami = settings['ami']
    provider.region = settings['region']
    provider.monitoring = settings['monitoring']
    override.vm.box = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"
    override.ssh.username = settings["ssh_username"]
    override.ssh.private_key_path = settings['private_key_path']
  end

end
