# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app/CoRider

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY main.py .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "main.py"]
