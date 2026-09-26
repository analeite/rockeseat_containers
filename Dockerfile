FROM alpine:3.24.2 AS build

WORKDIR /rocketseat_containers/app

RUN apk add --no-cache python3 py3-pip gcc python3-dev musl-dev mariadb-connector-c-dev

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]