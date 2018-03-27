# Obtaining Data

The test data that will be used for recipes and exercises will be from the Enron Dataset. You can read [here](https://www.technologyreview.com/s/515801/the-immortal-life-of-the-enron-e-mails/) to learn more regarding the dataset.

download.py is a commandline program that runs on the Python library itself. 

## Usage
```
$ python download.py
```

Running the program on default will automaticall download the zipped file of the Enron dataset.

```
$ python download.py -u "<insert download url>"
```
Running the program with the `u` argument will allow you to download a valid file link to your current directory.

