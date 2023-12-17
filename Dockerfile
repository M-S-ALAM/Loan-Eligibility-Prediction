FROM python:3.10-slim

WORKDIR /app

COPY /requirements.txt ./requirements.txt
COPY /model ./model
COPY /source ./source
COPY /app.py ./app.py


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8503

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]