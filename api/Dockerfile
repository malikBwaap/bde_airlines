FROM python:3.13

WORKDIR /app

COPY requirements.txt .

ENV PIP_ROOT_USER_ACTION=ignore
RUN python -m pip install ipykernel --no-cache-dir --progress-bar=off -r requirements.txt --root-user-action=ignore
RUN python -m pip install --upgrade --progress-bar=off pip setuptools wheel -r requirements.txt --root-user-action=ignore
RUN python -m pip install --no-cache-dir --progress-bar=off -r requirements.txt --root-user-action=ignore
RUN python -m pip install requests --no-cache-dir --progress-bar=off -r requirements.txt --root-user-action=ignore


COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]