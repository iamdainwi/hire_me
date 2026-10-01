FROM python:3.13.15-alpine

WORKDIR /app

ENV PYTHONDONOTWRITEBYTECODE=1

ENV PYTHONBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN add:user --disabled-password --no-create-home appuser

COPY . .

USER appuser

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" \
    || exit 1

EXPOSE 8000

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]