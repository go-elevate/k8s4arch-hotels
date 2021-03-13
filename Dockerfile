FROM python:alpine

WORKDIR /app
COPY *.py Dockerfile requirements.txt ./

RUN pip install -r requirements.txt

ENV FLASK_APP=controller.py
ENV FLASK_ENV=production

CMD [ "flask", "run", "--host=0.0.0.0"]