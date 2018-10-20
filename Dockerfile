FROM python:3.5-alpine

RUN apk add git bash && \
    apk add gcc musl-dev && \
    git clone https://github.com/bostonaqua/evaldas.git && \
    cd evaldas && \
    pip install -r requirements.txt && \

CMD bash run_web.sh
