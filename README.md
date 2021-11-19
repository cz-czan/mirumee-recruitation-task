A CLI app written for recruitation purposes at Mirumee Software.

## Setup
Install requests:
```shell
pip install requests
```
## Usage
Execute `main.py` without any arguments to get core information on all cores, without taking failed and upcoming missions 
into consideration:
```shell
python main.py
```
The cores are ordered from most reused to least reused.

Use the `-l` or `--limit` option to limit the number of cores on which the information is fetched:
```shell
python manage.py -l 10
```

Use the `-u` or `--upcoming` flag to include upcoming flights in the data, the `-f` or `--failed` flag to include 
failed flights, and the `-d` or  `--debug` flag to get details about each core and all the missions it 
took/will take ( depending on flags ) part in.
