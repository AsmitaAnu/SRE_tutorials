FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requriment.txt
EXPOSE 5000
CMD ["python", "app.y"]

'

