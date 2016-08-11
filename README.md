# docnow-ansible
Ansible playbooks for setting up dnflow

[![LICENSE](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](./LICENSE)

## Introduction

These scripts are intended to be run on a Unix-like system. They are tested to work on Mac OSX.

To use these scripts, [Vagrant](https://vagrantup.com) must already have been installed on the local system with the [VirtualBox](https://virtualbox.org) provider working. For provisioning to AWS, the `aws` provider must also be installed. This can be done by executing the following command, which will install the aws Vagrant provider plugin: 

```bash
vagrant plugin install vagrant-aws
```

For each of these providers only Ubuntu 14.04 is supported. We will also provide Docker as an additional provider.

## Includes

- Ubuntu 14.04
- Python3

## Setup

Clone this repository locally

```bash
git clone https://github.com/docnow/docnow-ansible
cd docnow-ansible
```


## Initial Configuration

Before deploying the environment you must make a few changes. Specifically you will need to register an application at [apps.twitter.com](https://apps.twitter.com). Once you've created your application, note down the consumer key, consumer secret. With these two variables in hand you can modify the `group_vars/all.template` and then copy it into place:

```bash
cp group_vars/all.template group_vars/all
```

For all environments, we have an `example_Vagrantfile` which will work. The Vagrantfile will be ignored because when using `aws` sensitive information will be added. Copying the `example_Vagrantfile` to `Vagrantfile` will need to be performed by:

```bash
cp example_Vagrantfile Vagrantfile
```

Boxes take approximately _10 mins_ to come up, and it can take much longer locally depending on your internet connection.

### Provider: Virtualbox

```bash
$ vagrant up
```

### Provider AWS

When using the `aws` provider to `vagrant up` it is necessary to define several environment variables in order to authenticate to AWS and supply a keypair with which Vagrant can log in to the new AWS EC2 instance being deployed. These environment variables are as follows:

* `KEYPAIR_NAME`: the name of the AWS keypair that will be used to log in to the instance. This keypair should already exist within your AWS account and its private key file should reside on the local system.
* `KEYPAIR_FILE`: the pathname of the private key on the local system corresponding to the aforementioned keypair.
* `AWS_ACCESS_KEY`: the AWS IAM access key to the account under which the EC2 instance will be created.
* `AWS_SECRET_KEY`: the AWS IAM secret key to the account under which the EC2 instance will be created.

Please check these are appropriate before bringing up the instance with Vagrant and edit where necessary beforehand.

Current maintainers:

* [Francis Kayiwa](https://github.com/kayiwa)

## License

[MIT](https://opensource.org/licenses/MIT)
