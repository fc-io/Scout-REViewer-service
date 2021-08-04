# Scout-REViewer-service

A rest service for generating REViewer output.

## Getting started

### To make it run (a bit more) quickly

Run with docker

#### Setup

``` bash
git clone <project>
cd <project>
```

Create a docker specific env file called `.env.docker` in the root folder with
the following content:

```
HOST_DATA=<absolute_path_to_host_machine_folder_with_reference_file>

SRS_PORT=5050

REV_PATH=/REViewer/build/install/bin/REViewer
REV_REF_PATH=/host_data/<file_name_of_the_reference_file_in_the_host_data_folder>.fasta
REV_CATALOG_PATH=data/catalog_test.json
```

2 changes that needs to be made are:

1. update the `HOST_DATA` value to point towards your `.fasta` reference file.
   This will be used as default if the user does not provide one.
2. update the file name in the `REV_REF_PATH` to match the reference file in
   your `host_data` folder

SRS_PORT can be changed to set the port the service exposes.

REV_CATALOG_PATH can be changed to point to a custom file in the `host_data`
folder but this is not required as one is provided by default.

#### run

``` bash
env $(cat .env.docker) docker compose up
```

The crazy `env $(cat .env.docker)` is because `docker compose up` does not support
an `--env-file` option like `docker run` does.

### To develop locally

#### Setup

``` bash
git clone <project>
cd <project>
```

Create an env file called `.env`. With the following
content:

```
REV_PATH=/Users/<User>/bin/REViewer/build/install/bin/REViewer
REV_REF_PATH=../my_host_data/human_g1k_v37_decoy.fasta
REV_CATALOG_PATH=data/catalog_test.json
```

2 changes that needs to be made are:

1. Update the `REV_PATH` value to point towards your instance of REViewer. See
   https://github.com/Illumina/REViewer for installation instructions.
2. Update the file name in the `REV_REF_PATH` to point towards a reference
   file.

`REV_CATALOG_PATH` can be changed to point to another catalog file but this is
not required as one is provided as default.

Then load dependencies and the virtual environment using anaconda or mini-conda:

``` bash
conda env create
```

#### Run (development)

``` bash
conda activate Scout-REViewer-service
```

``` bash
uvicorn main:app --reload
```

### API

#### Example requests

Notice that the first time REViewer runs with a new reference file it will take
a bit longer since it will generate a `fasta.fai` file. You can avoid this by
adding a corresponding (same name, different file extension) `fasta.fai` file
to the same location as your fasta file (or provide one with the API request –
TBD) – if you already have one.

##### files accessible from another server

If running in docker use `host.docker.internal` instead of `localhost` to
access your own server.

``` bash
curl --location --request POST 'http://127.0.0.1:8000/reviewer' \
--header 'Content-Type: application/json' \
--data-raw '{
  "reads": "http://localhost:5010/justhusky_exphun_hugelymodelbat_realigned.bam",
  "reads_index": "http://localhost:5010/justhusky_exphun_hugelymodelbat_realigned.bam.bai",
  "vcf": "http://localhost:5010/justhusky_exphun_hugelymodelbat.vcf",
  "catalog": "http://localhost:5010/catalog_test.json",
  "locus": "TCF4"
}'
```

##### files from locally accessible file system

This will avoid copying the files and instead use the already existing files.
This is preferred if possible as it should be faster and reduce writes.

``` bash
curl --location --request POST 'http://127.0.0.1:8000/reviewer' \
--header 'Content-Type: application/json' \
--data-raw '{
  "reads": "/<path_to_file>/justhusky_exphun_hugelymodelbat_realigned.bam",
  "reads_index": "/<path_to_file>/justhusky_exphun_hugelymodelbat_realigned.bam.bai",
  "vcf": "/<path_to_file>/justhusky_exphun_hugelymodelbat.vcf",
  "catalog": "/<path_to_file>/catalog_test.json",
  "locus": "TCF4"
}'
```

#### Docs

Automatically generated API docs can be accessed at
`http://<server-address>:<port>/docs` when running the server. But the content
of this `README.md` is more extensive.

## Testing

Needs a `.fasta` reference file to run. See instructions for `.env` files above.

```
pytest
```

## TODO

- [x] get files from remote
- [x] store files on server
- [x] run REViewer with local file path as arguments
- [x] send back REViewer generated SVG
- [x] bundle REViewer
- [x] Dockerize
- [ ] make smaller docker build
- [x] delete tmp files, maybe it's good if this also runs as some kind of chron job
- [x] tests
- [x] more tests – primarily for optional post values
- [ ] more tests 2 – check that it fails well with wrong input
- [ ] unit tests - low prio
- [ ] make sure to check if all files are created correctly after fetching
- [ ] validate urls – add helpful error messages if wrong file input (check that a file is download)
- [ ] prettify && DRY up

- [x] API documentation
- [x] make it possible to select port through .env variables – docker

- [ ] handle files that are too large – test? low priority
- [ ] security – should be enough for now since this will be an internal service

- [x] add viewBox attribute to allow for responsive scaling when added to HTML

### Ideas

- [ ] file uploader
- [ ] rate limiting
- [ ] could pipe svg instead of creating a file? (Don't think this can be easily done.)

