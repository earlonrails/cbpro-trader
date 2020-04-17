FROM alpine:3.7

# Set locale
ENV LANG C.UTF-8
# Allow for curses interface
ENV TERM xterm

# Update Ubuntu & install system dependencies
RUN apk update
RUN apk add --no-cache build-base \
    gcc \
    wget \
    git \
    python3-dev
RUN pip3 install --upgrade pip setuptools

# Build and install ta-lib
ADD https://downloads.sourceforge.net/project/ta-lib/ta-lib/0.4.0/ta-lib-0.4.0-src.tar.gz /
RUN tar xzvf ta-lib-0.4.0-src.tar.gz
WORKDIR /ta-lib
RUN ./configure --prefix=/usr
RUN make
RUN make install

# Copy bot files
WORKDIR /app
COPY requirements.txt .
RUN pip3 install numpy==1.15.2
RUN pip3 install -r ./requirements.txt

CMD ["python3", "./cbpro-trader.py"]
