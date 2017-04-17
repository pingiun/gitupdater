# gitupdater

gitupdater can be used to automatically update git repo's with a webhook.

## Usage

1. Clone a github repository somewhere.
2. Set a webhook for the repository. (Use the JSON format)
3. Optionally set a secret in settings.py and you webhook
4. Fill in the path for the repository in settings.py
5. Run `FLASK_APP=server.py GITUPDATER_SETTINGS=settings.py flask run` or something like these docker commands:
```
docker build -t gitupdater .
docker run -d --restart=always -v /var/www/example.com:/gitrepo -p 127.0.0.1:8001:5000 gitupdater
```
6. Add a route or vhost to redirect your webhook to port 8001.
