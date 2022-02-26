FROM python:3

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt update -y \
    && apt install -y  gcc python3-dev

# install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# copy project
COPY . .

EXPOSE 8000
# Run DB
RUN python manage.py makemigrations
RUN python manage.py migrate

# Run Server
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]





