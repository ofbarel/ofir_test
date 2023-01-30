FROM python:3.10

# CMD bash -c "while true; do echo hello; sleep 2; done"

COPY . /app

WORKDIR /app

CMD python main.py