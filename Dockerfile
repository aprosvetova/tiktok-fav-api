FROM python:3.9-alpine

RUN apk -U add chromium udev ttf-freefont build-base
RUN pip install TikTokApi aiohttp

ADD main.py .

EXPOSE 8080

CMD [ "python", "./main.py" ]