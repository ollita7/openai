FROM python:3.9
WORKDIR /src
SHELL ["/bin/bash", "-c"]

COPY requirements.txt .
COPY . /src

# Install requirements
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
