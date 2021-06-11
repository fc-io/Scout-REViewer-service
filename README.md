# Scout-REViewer-service

A rest service for generating REViewer output.

## Getting started

### Prerequists

Have access to a server serving the files you want to run with/through REViewer.

Make sure ~conda is installed.

Add a reference (.fasta) file to data folder. (after cloning)

### Setup

``` bash
git clone <project>
cd <project>
```

``` bash
conda env create
```

``` bash
conda activate Scout-REViewer-service
```

### Run (development)

``` bash
uvicorn main:app --reload
```

### API

Example requests – http://127.0.0.1:8000/reviewer

``` bash
curl --location --request POST 'http://127.0.0.1:8000/reviewer' \
--header 'Content-Type: application/json' \
--data-raw '{
  "reads": "http://localhost:5010/justhusky_exphun_hugelymodelbat_realigned.bam",
  "vcf": "http://localhost:5010/justhusky_exphun_hugelymodelbat.vcf",
  "catalog": "http://localhost:5010/catalog_test.json",
  "locus": "TCF4"
}'
```

## TODO

DONE: get files from remote
DONE: store files on server
TODO: run REViewer with local file path as arguments
TODO: send back REViewer generated SVG
TODO: delete temp files
TODO: think about if this is secure (enough)
TODO: tests
TODO: DRY up
TODO: handle files that are to large
