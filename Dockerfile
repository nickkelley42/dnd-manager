FROM python:3

WORKDIR /dnd_manager

COPY . /dnd_manager

RUN pip install -r requirements.txt

CMD ["gunicorn", "dnd_manager.wsgi", "-b", "0.0.0.0:8000"]
EXPOSE 8000
