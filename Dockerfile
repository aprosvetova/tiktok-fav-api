FROM python:3-slim

ADD main.py /

RUN pip install flask TikTokApi

EXPOSE 80

ENTRYPOINT [ "python", "./main.py" ]