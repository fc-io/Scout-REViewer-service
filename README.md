# Scout-REViewer-service

A rest service for generating REViewer output.

## Getting started

### Prerequists

Have access to files you want to run with/through REViewer.

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

### Run (development)

``` bash
conda activate Scout-REViewer-service
```

``` bash
uvicorn main:app --reload
```

### API

Example requests

#### files accessible form another server

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

#### files from locally accessible file system

``` bash
curl --location --request POST 'http://127.0.0.1:8000/reviewer' \
--header 'Content-Type: application/json' \
--data-raw '{
  "reads": "/path_to_file/justhusky_exphun_hugelymodelbat_realigned.bam",
  "vcf": "/path_to_file/justhusky_exphun_hugelymodelbat.vcf",
  "catalog": "/path_to_file/catalog_test.json",
  "locus": "TCF4"
}'
```

## TODO

- [x] get files from remote
- [x] store files on server
- [x] run REViewer with local file path as arguments
- [x] send back REViewer generated SVG
- [ ] bundle REViewer
- [ ] Dockerize
- [ ] delete tmp files, maybe it's good if this also runs as some kind of chron job
- [ ] think about if this is secure (enough)
- [ ] tests
- [ ] make sure to check if all files are created correctly after fetching
- [ ] validate urls – add helpful error messages if wrong file input
- [ ] prettify && DRY up
- [ ] handle files that are to large


### Extra (ideas)

- [ ] file uploader
