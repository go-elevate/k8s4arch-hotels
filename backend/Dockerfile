FROM python:alpine

WORKDIR /app
COPY *.py Dockerfile requirements.txt ./
COPY assets ./assets

RUN pip install -r requirements.txt

ENV FLASK_APP=controller.py
ENV FLASK_ENV=production

RUN mkdir /db

ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]