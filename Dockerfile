FROM python:3.10-alpine

WORKDIR /data/

COPY . /data

RUN  pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple \
 &&  mkdir db file


EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]