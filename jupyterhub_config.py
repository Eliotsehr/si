# Configuration file for jupyterhub.

c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.hub_connect_ip = 'jupyterhub'

# Docker network
c.DockerSpawner.network_name = 'jupyterhub'


#Authenticator

from oauthenticator.bitbucket import BitbucketOAuthenticator
c.JupyterHub.authenticator_class = BitbucketOAuthenticator  

c.BitbucketOAuthenticator.oauth_callback_url = '<YOUR_CALLBACK_URL>'
c.BitbucketOAuthenticator.client_id = '<YOUR_CLIENT_ID>'
c.BitbucketOAuthenticator.client_secret = '<YOUR_CLIENT_SECRET>'

#Whitelist and admins

#c.Authenticator.admin_users = {''}
#c.Authenticator.whitelist = {''}


#Spawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = 'jupyter/datascience-notebook'
