# docnow-ansible
Ansible playbooks for setting up dnflow

[![LICENSE](https://img.shields.io/badge/license-ISC-blue.svg?style=flat-square)](./LICENSE)

## Introduction

This is a development environment for docnow's dnflow

Vagrant is used for launching the environment, and we will support these providers

1. Virtualbox
2. AWS

For each of these providers only Ubuntu 14.04 is supported. We will also provide Docker as an additional provider.

## Includes

- Ubuntu 14.04
- Python3

## Requirements

1. [Vagrant](http://www.vagrantup.com/)
2. [Virtualbox](https://www.virtualbox.org/)
3. [git](https://git-scm.com/)

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

Boxes take approximately _10 mins_ to come up, and it can take much longer locally depending on your internet connection.

### Provider: Virtualbox

```bash
$ vagrant up
```

Current maintainers:

* [Francis Kayiwa](https://github.com/kayiwa)

## License

[ISC](https://opensource.org/licenses/ISC)
