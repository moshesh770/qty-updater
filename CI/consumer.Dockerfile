FROM python:3.8.5-alpine3.12

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY ../consumer.py consumer.py

COPY ../consumer-requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Run it
CMD python -m consumer