FROM python:3.9-slim as build

RUN apt update \
    && apt install -y --no-install-recommends python3-dev default-libmysqlclient-dev build-essential

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


FROM python:3.9-slim as release

WORKDIR /src

RUN apt update && apt install -y default-libmysqlclient-dev

COPY --from=build /usr/local/lib/python3.9 /usr/local/lib/python3.9/
COPY --from=build /usr/local/bin /usr/local/bin/

COPY . .

ENTRYPOINT [ "python" ]

CMD [ "uwsgi.py" ]
