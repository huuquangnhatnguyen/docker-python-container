FROM python:3.9-slim
# Set the working directory
WORKDIR /home/data

# Copy Python script and text files to the container
COPY script.py .
COPY IF.txt .
COPY AlwaysRememberUsThisWay.txt .

# Create the output directory
RUN mkdir output

# Run the Python script
RUN python script.py