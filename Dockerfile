FROM continuumio/miniconda3

RUN set -ex;         \
    apt-get update;  \
    apt-get install -y \
        libzmq5 \
        libbz2-dev \
        zlib1g-dev \
        bzip2 \
        ca-certificates \
        git \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libxrender1 \
        mercurial \
        subversion \
        wget \
        g++ \
        cmake \
        make \
        liblzma-dev \
        libcurl4-openssl-dev \
    && apt-get clean

RUN set -ex;                                                                   \
    mkdir -p /REViewer;                                                        \
    wget -qO- --no-check-certificate https://github.com/Illumina/REViewer/archive/8683e73.tar.gz | tar -zxf - -C ./REViewer --strip-components=1;  \
    cd /REViewer;                                                              \
    mkdir build;                                                               \
    cd build;                                                                  \
    cmake ..; \
    make;

COPY . /Scout-REViewer-service
COPY .env.docker .env

RUN conda env create -f /Scout-REViewer-service/environment.yml

ENTRYPOINT [\
    "conda", "run", "--no-capture-output", "-n", "Scout-REViewer-service", \
    "uvicorn", "main:app", "--app-dir", "/Scout-REViewer-service", "--host", "0.0.0.0", "--port", "${SRS_PORT}" \
]
