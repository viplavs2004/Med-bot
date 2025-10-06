# Use a newer version of Python that is compatible with your packages
FROM python:3.11-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker's build cache
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port your application will run on
EXPOSE 8080

# The command to run your application using the Uvicorn server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]

