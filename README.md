# docnow-ansible
Ansible playbooks for setting up dnflow

[![LICENSE](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](./LICENSE)

## Purpose

The goal of this repository is to have a lightweight method of developing and reproducing the [docnow/dnflow](https://github.com/docnow/dnflow) tool. With the use of freely available tools a user can set up a disposable environment on their personal computer or on the AWS cloud.

### Install prerequisite tools 

These scripts are intended to be run on a Unix-like system. They are tested to work on Mac OSX and Ubuntu Trusty Tahr.

To use these scripts, [Vagrant](https://vagrantup.com) must already have been installed on the local system with the [VirtualBox](https://virtualbox.org) provider working (do not use a package manager, follow the instructions on the sites directly). For provisioning to AWS, the `aws` will be installed. 

For each of these providers only Ubuntu 14.04 is supported.

## Includes

- Ubuntu 14.04
- Python3

## Setup

Clone this repository locally

```bash
git clone https://github.com/docnow/dnflow-ansible
cd dnflow-ansible
```

## Initial Configuration

Before deploying the environment you must make a few changes. Specifically you will need to register an application at [apps.twitter.com](https://apps.twitter.com). Once you've created your application, note down the **consumer key, consumer secret**. It is also important to remember to fill out the _Callback URL_ otherwise the application will not work. You can use `http://example.org`.  With these two variables in hand you can modify the `group_vars/all_template` and then copy it into place:

```bash
cp group_vars/all_template group_vars/all
```

For all environments, we have a `Vagrantfile` which will work. We have provided example provider files for Virtualbox and AWS.

Boxes take approximately _10 mins_ to come up, and it can take much longer locally depending on your internet connection.

### Provider: Virtualbox

```bash
$ vagrant up
```

On the first run it will install the `vagrant-triggers` plugin. In addition it will make a copy of `provider/example.virtualbox.yml` Take a look at the contents of that file and if you need to make adjustments do so before running.


```bash
$ vagrant up
```

again.

### Provider AWS

```bash
$ vagrant up --provider aws
```

On the first run it will install the `vagrant-triggers` and `vagrant-aws` plugins. In addition it will make a copy of `provider/example.aws.yml` Take a look at the contents of the `provider/aws.yml` and enter the AWS account information needed. You must enter the following.

* `keypair_name`: the name of the AWS keypair that will be used to log in to the instance. This keypair should already exist within your AWS account and its private key file should reside on the local system.
* `ami`: The ami from the EC2 dashboard of your region.
* `security_group`: The name of the security_group from AWS.
* `region`: For convenience, you may want to set the same region as the one your machine is running in (i.e. `us-west-2`).
* `private_key_path`: the pathname of the private key on the local system corresponding to the aforementioned keypair.
* `access_key_id`: the AWS IAM access key to the account under which the EC2 instance will be created.
* `secret_access_key`: the AWS IAM secret key to the account under which the EC2 instance will be created.


## After installation

### Provider: Virtualbox

Go to http://192.168.60.14

### Provider: AWS

Go to your AWS Console

* Select your running instance
* Click on the **connect** information to log into it.

You will need the AWS provided public dns name (make a note of this) This information will be needed to be replaced in the following files

`/home/docnow/dnflow/dnflow.cfg` HOSTNAME 

`/etc/nginx/sites-enabled/docnow` server_name

The run the following command

```bash
sudo stop docnow
sudo start docnow
```

Then point your URL to the AWS location above

Current maintainers:

* [Francis Kayiwa](https://github.com/kayiwa)
* [Ed Summers](https://github.com/edsu)

## License

[MIT](https://opensource.org/licenses/MIT)
