# Include Python
from python:3.11.1-buster

# Define your working directory
WORKDIR /

# Install runpod
# Install git
RUN apt-get update && apt-get install -y git

# Install python packages
RUN pip3 install --upgrade pip
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


# Add your file
ADD app.py .

# Call your file when your container starts
CMD [ "python", "-u", "/app.py" ]
