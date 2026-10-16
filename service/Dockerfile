FROM izaaksofer/complaint-router-base:1
WORKDIR /app
COPY model/ model/
COPY serve.py .
ENV MODEL_URI=/app/model
EXPOSE 8000
CMD ["uvicorn", "serve:app", "--host", "0.0.0.0", "--port", "8000"]