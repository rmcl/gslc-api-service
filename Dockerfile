FROM fsharp

RUN mkdir /app
WORKDIR /app

RUN  apt-get update -y && \
     apt-get upgrade -y && \
     apt-get dist-upgrade -y && \
     apt-get -y autoremove && \
     apt-get clean
RUN apt-get install -y zip

### INSTALL GSL

RUN echo "Fetching GSLc from Github"
ADD https://github.com/Amyris/Gslc/archive/master.zip master.zip
RUN unzip master.zip && mv "Gslc-master" "Gslc"

RUN echo "Building GSLc"
WORKDIR /app/Gslc
RUN ./build.sh

ADD gsl_api /app/gsl_api
WORKDIR /app/gsl_api

# INSTALL PYTHON & PIP

RUN apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt
RUN mkdir /gsl-tmp-output

