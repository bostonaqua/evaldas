FROM python:3.5-alpine

RUN apk add bash && \
    apk add supervisor
COPY supervisord.conf /etc/supervisord.conf
ADD . /evaldas
WORKDIR /evaldas
RUN pip install -r requirements.txt

COPY run_web.sh /run_web.sh

CMD ["bash", "run_web.sh"]