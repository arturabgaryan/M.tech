FROM python:3.9-slim

COPY requirements.txt requirements.txt
ADD requirements.txt /

RUN pip install -r  /requirements.txt

ADD mtech.py /

ENV PYTHONUNBUFFERED=1

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "mtech.py", "--server.port=8501", "--server.address=0.0.0.0"]
