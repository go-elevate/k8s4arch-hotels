FROM python:alpine

WORKDIR /app
COPY *.py Dockerfile requirements.txt ./
COPY assets ./assets

RUN pip install -r requirements.txt

ENV FLASK_APP=controller.py
ENV FLASK_ENV=production
ENV FLASK_PORT=5000

RUN mkdir /db

ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0", "--port=$FLASK_PORT"]