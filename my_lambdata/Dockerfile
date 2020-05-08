FROM debian

# ### So logging/io works reliably w/Docker
# ENV PYTHONUNBUFFERED=1
# ### UTF Python issue for Click package (pipenv dependency)
# ENV LC_ALL=C.UTF-8
# ENV LANG=C.UTF-8
# ### Need to explicitly set this so `pipenv shell` works
# ENV SHELL=/bin/bash

### Basic Python dev dependencies
RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install python3-pip curl -y && \

# pip install package from mtoce pypi acct
RUN pip3 install -i https://test.pypi.org/simple/ lambdata-mtoce==1.0.2