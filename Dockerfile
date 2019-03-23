# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Update dependencies linux
RUN apt-get update

# RUN pip install jupyter

# Install the APP
WORKDIR /tmp_install
COPY requirements.txt /tmp_install
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Set the working directory to /app
COPY ./ /solution
WORKDIR /solution

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Go to app workdir
WORKDIR /app/src

# The app port
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
# CMD  ["jupyter notebook" "--ip 0.0.0.0 --no-browser --allow-root"]