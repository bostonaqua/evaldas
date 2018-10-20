FROM python:3.5-alpine

RUN apk add bash && \
    apk add gcc musl-dev && \
ADD . /evaldas
WORKDIR /evaldas
RUN pip install -r requirements.txt

COPY run_web.sh /run_web.sh

CMD ["bash", "run_web.sh"]