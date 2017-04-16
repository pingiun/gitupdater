FROM python:3-onbuild

ENV FLASK_APP server.py

ENV GITUPDATER_SETTINGS settings.py

CMD [ "flask", "run" ]
