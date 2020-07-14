FROM python:3
LABEL maintainer "kamalraj Selvaraj"

WORKDIR /dockercon

COPY requirements.txt /dockercon
COPY docker_py_test.py /dockercon
COPY input.dat /dockercon/input.dat

RUN pip --version
RUN pip install --upgrade pip
RUN pip --version
#RUN pip install --no-cache-dir med2image
#RUN pip install --upgrade snowflake-connector-python
RUN pip install -r requirements.txt

ENTRYPOINT ["python3","docker_py_test.py"]
