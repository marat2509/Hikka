FROM python:3.11-alpine as python-base
ENV DOCKER=true
ENV GIT_PYTHON_REFRESH=quiet

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN apk add --no-cache gcc build-base linux-headers

WORKDIR /hikka
COPY . /hikka
RUN pip install --no-warn-script-location --no-cache-dir --upgrade pip .
RUN rm -rf /hikka

WORKDIR /data

EXPOSE 8080

CMD python -m hikka
