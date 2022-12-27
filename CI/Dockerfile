FROM python:3.8.5-alpine3.12

ENV APP_HOME /app
ENV ELASTIC_PASS OVr7_2xU5Jyuz0Z0EvWy

WORKDIR $APP_HOME

RUN apk --update add build-base
RUN apk --update add linux-headers

COPY ./db_classes ./db_classes
COPY ./utils ./utils
COPY ./models ./models
COPY ./main.py main.py

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

# Run it
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0"]
