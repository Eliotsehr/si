# SI Project

Use JupyterHub to build and deploy a multi-tenant platform for exploratory data analysis with support for R, Python 3, Julia, and Go.


**Objectives**

- Spawn single-user servers using Docker containers
- Support MariaDB and MongoDB
- Jupyter notebook with kernel support for R, Python 3, Julia, and Go
- Atomic must be the operating system (OS) of the host machine


***Project Scheme***

[![INSERT YOUR GRAPHIC HERE](https://imgur.com/oL0kaSj.jpg)]()


# Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Start the hub](#start-the-hub)
- [Using the hub](#using-the-hub)
- [What is left to do](#what-is-left-to-do)

# Requirements

- The OS hosting the hub : <a href="http://cloud.centos.org/centos/7/atomic/images/CentOS-Atomic-Host-Installer.iso" target="_blank">Atomic OS</a> (here the CentOS version)
- <a href="https://www.virtualbox.org/wiki/Downloads" target="_blanck">VirtualBox</a> for the emulation

# Installation

We will setup two VMs, on based on AtomicOS and the other one on Debian. As everything is running locally we must make sure that our VMs are on the same virtual network in the VirtualBoxs parameters.

To setup the VMs network go to File > Parameters > Networks and thenn click on the green cross button on the right.

Once you've installed the two VMs shut them down and for each click on Configuration > Network then NAT Network and select the network you created.

Boot the 2 VMS


# Configuration

**Atomic OS Setup**


Fisrt we will update the system with:

	#atomic host upgrade
	#systemctl reboot

Second we will setup the storage for the docker containers:

	#vi /etc/sysconf/docker-storage-setup

Add the following line replaceing X by the amount of storage you want to add:

	ROOT_SIZE=XG

Set up the sotrage with the command:

	#docker-storage-setup
	
Finally create a directory for the config files:

	#mkdir jupyterhub
	#cd jupyterhub

**Bitbucket setup**

You will need a bitbucket application to make the authentication machanism work. To do so you need to log on your bitbucket account then go to Bitbucket Settings > Oauth > New user

Here you fill up the fields and be carefull with the Call back URL it must be: **http://<atomic_host_ip>/hub/oauth_callback**

Once you're done you save the application and you shoul'd see it appearing. By clicking on the arrow on the right you will see your **client_id** and **client_secret**

You must write those two strings inside the *jupyterhub_config.py* in the **c.BitbucketOAuthenticator.client_id = '<YOUR_CLIENT_ID>'**
and **c.BitbucketOAuthenticator.client_secret = '<YOUR_CLIENT_SECRET>'**

Finally write the call back url that you created in the application at **c.BitbucketOAuthenticator.oauth_callback_url = '<YOUR_CALLBACK_URL'**

**Building the hub**

We need to create a network for the dockers that jupyterhub will use

	#docker network create jupyterhub
	
Then once the *Dockerfile*, *requirements.txt* and *jupyterhub_config.py* are in the jupyterhub directory we build the hub

	#docker build -t hub .

We also need the image that jupyterhub is going to use for the single-user servers

	#docker pull jupyter/datascience-notebook
	
	
# Start the hub
	
We will start with the following instructions:

- run it on the docker network
- use port 8000
- mount the host docker socket

Type the following command:

	#docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock --network jupyterhub --name jupyterhub -p 8000:8000 hub
	
## Using the hub

If you go to your Debian host you can now access the hub throw your browser via : <atomic_host_machine_ip>:8000

As there is no whiteliste in the config anyone using Bitbucket can log in and use the hub.

## What is left to do

- Build our own Dockerfile to implement Go and MariaDB/MongoDB
