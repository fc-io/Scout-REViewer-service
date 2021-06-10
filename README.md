# Scout-REViewer-servic

A rest service for generating REViewer output.

## Getting started

Add a reference (.fasta) file to data folder.

Make sure ~conda is installed.

``` bash
conda env create
```

``` bash
conda activate Scout-REViewer-service
```

``` bash
# FLASK_APP=app.py FLASK_ENV=development flask run
flask run
```

``` json
// http://127.0.0.1:5000/reviewer

{
  "vcf": "test1",
  "reference": "test2",
  "catalog": "test3",
  "locus": "test4"
}
```
