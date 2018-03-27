import argparse
import requests
import shutil

def download_file(url):
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

    return local_filename

parser = argparse.ArgumentParser(description='Download some file')
parser.add_argument('-u'
                    ,action='store'
                    ,dest='url'
                    ,default="https://www.cs.cmu.edu/~enron/enron_mail_20150507.tar.gz")

results = parser.parse_args()# collect cmd line args
url = results.url
print(url)
download_file(url)
