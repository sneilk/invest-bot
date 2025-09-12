FROM python:3.12.3

WORKDIR /user/src/app

COPY . .


RUN pip install --no-cache  -r requirements.txt

EXPOSE 5000

CMD ["python3", "./main.py"]
