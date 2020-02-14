FROM python:3
COPY main.py /app/
COPY requirements.txt /app/requirements.txt
ADD pip.conf /root/.pip/
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY qq_server.tar.gz /app/
RUN pip install /app/qq_server.tar.gz
CMD ["gunicorn", "-w", "2", "-b","0.0.0.0:5000","--access-logfile","-","--error-logfile","-","--log-file","-","qq_server:app"]
