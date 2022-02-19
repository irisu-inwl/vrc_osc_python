FROM python:3.10

RUN mkdir /opt/app
WORKDIR /opt/app
RUN pip install --upgrade pip
ADD requirements.txt ./
ADD app.py ./
RUN pip install -r requirements.txt
ENV HOST 127.0.0.1
ENV PORT 9000

CMD ["streamlit", "run", "app.py"]