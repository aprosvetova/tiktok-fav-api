FROM python:3-slim

ADD main.py /

RUN pip install flask TikTokApi

ENTRYPOINT [ "python", "./main.py" ]