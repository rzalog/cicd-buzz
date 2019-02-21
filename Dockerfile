FROM rzalog/rpi-python:v1
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY . /app
WORKDIR /app

CMD python3 app.py