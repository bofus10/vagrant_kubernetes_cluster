# We need python 3.8
FROM python:3.8

# make the working directory in the container
RUN mkdir /app

# specify where to install the app
WORKDIR /app/

# add all files to the working directory
ADD ./kafka-probe.py /app/

# Install the dependencies in the requirements file.
RUN python3.8 -m pip install kafka-python

# Run the appS
#CMD ["python", "/app/app.py"]