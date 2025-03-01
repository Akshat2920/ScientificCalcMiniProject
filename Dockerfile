# Use an official lightweight Python image
FROM python:3.9.6

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Expose necessary ports
EXPOSE 5000 22

# Start SSH service and the Flask app
CMD ["/bin/bash", "-c", "/usr/sbin/sshd && python app.py"]
