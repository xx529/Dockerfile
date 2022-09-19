c.Authenticator.admin_users = {'root', 'admin'}
c.JupyterHub.admin_access = True
c.LocalAuthenticator.create_system_users=True
c.DummyAuthenticator.password = "12345678"

c.Spawner.notebook_dir = '~'
c.Spawner.default_url = '/lab'
c.Spawner.args = ['--allow-root']