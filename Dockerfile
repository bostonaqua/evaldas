FROM python:3.5-alpine

RUN apk add git bash && \
    apk add gcc musl-dev && \
    git clone https://github.com/bostonaqua/evaldas.git && \
    cd evaldas && \
    pip install -r requirements.txt

COPY run_web.sh /run_web.sh

CMD bash run_web.sh