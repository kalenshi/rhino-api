FROM python:3.9
ENV PYTHONUNBUFFERED=1

RUN git clone https://github.com/kalenshi/rhino.git
WORKDIR ./rhino-api
RUN apt-get update \
    && pip install --upgrade pip && \
    pip install -r requirements.txt


CMD ["python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

# TODO work in progress



