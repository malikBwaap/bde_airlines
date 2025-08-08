FROM python:3.13

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install ipykernel --no-cache-dir --progress-bar=off -r requirements.txt --root-user-action=ignore
RUN python -m pip install --upgrade --progress-bar=off pip setuptools wheel --root-user-action=ignore
RUN python -m pip install --no-cache-dir --progress-bar=off -r requirements.txt --root-user-action=ignore
RUN python -m pip install waitress --root-user-action=ignore
RUN python -m pip install gunicorn --root-user-action=ignore

CMD ["gunicorn", "app:server", "-b", "0.0.0.0:8050", "-w", "1"]

COPY app.py .

CMD ["python", "app.py"]
