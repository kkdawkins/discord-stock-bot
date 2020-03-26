FROM python:3.8
ADD bot.py /
ADD requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python3", "./bot.py"]