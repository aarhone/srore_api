FROM python:3
RUN pip3 install flask
WORKDIR /flaskapp
COPY apif.py /flaskapp
EXPOSE 5000
ENV FLASK_APP=apif.py
CMD ["flask", "run", "--host=0.0.0.0"]