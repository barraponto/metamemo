FROM python:3.8
WORKDIR /app
RUN ["python", "-m", "pip", "install", "poetry"]
COPY ["poetry.lock", "pyproject.toml", "./"]
RUN ["poetry", "install"]
COPY ["./src", "./src"]
CMD ["poetry", "run", "python", "src/manage.py", "runserver", "0.0.0.0:8000"]
