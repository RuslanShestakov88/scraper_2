FROM python:3.7

ADD api.py .

RUN pip install selenium webdriver-manager

CMD ["python", "./api.py"]