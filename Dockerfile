# Use an Ubuntu base image
FROM ubuntu:latest

# Install dependencies
RUN apt-get update \
    && apt-get install -y wget xz-utils python3 python3-pip python3-venv

RUN python3 -m venv /venv \
    && /venv/bin/pip install --upgrade pip \
    && /venv/bin/pip install bs4 requests

ENV PATH="/venv/bin:$PATH"

# Set up a directory for the FiveM server
WORKDIR /serverdata

# Copy the script into the image
COPY script.py ./script.py

# Expose necessary ports for the FiveM server
EXPOSE 30120/tcp
EXPOSE 30120/udp
EXPOSE 40120/tcp

# Run the dynamic setup script at runtime
CMD ["/venv/bin/python", "script.py"]