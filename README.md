# hotcrp2csv
Python script to transform the list of accepted papers from HotCRP's JSON file into IEEE CS spreadsheet format.


## Configuration

Edit hotcrp2csv, and modify the following variables, as in the example below:

```
ACRONYM = "MSR"  # Acronym of the conference
TRACK = "Challenge"  # Track (leave empty if single track)

## Page limit depending on the type of papers. 
## There are two possibilities:
## a) Directly a number (in string format) when there is only one type

PAGE_LIMIT = "4+1"

## b) A dictionary with all the types of papers:
## Syntax --> Type: Number of pages

#PAGE_LIMIT = {
#    "Full (10 pages plus 2 additional pages of references)": "10+2",
#    "Short (4 pages plus 1 additional page of references)": "4+1"
#}

# If you append multiple tracks into a single CSV output file,
# only the first track should have a header. Else, put HEADER to False
HEADER = True
```


## Usage

After configuring hotcrop2csv.py for your conference, you are ready to run it.

```
Usage: hotcrp2csv.py input.json > output.csv

input.json is the list of accepted papers as exported in JSON from HotCRP

output.csv is the output file in CSV format
```


## Exporting JSON from HotCRP

If you want to export the list of accepted papers from HotCRP in JSON format, you first have to choose all accepted papers from the drop-down menu and then push ``Search``, as in following figure:

![Obtain the list of accepted papers](https://raw.githubusercontent.com/gregoriorobles/hotcrp2csv/main/accepted.png)

This will display the list of accepted papers. Then, at the bottom of the page, click on ``Download`` and in the drop-down menu choose ``JSON`` before pressing the ``Go!`` button as shown in the next figure:

![Download the list of papers in JSON format](https://raw.githubusercontent.com/gregoriorobles/hotcrp2csv/main/export.png)


## Conferences with several tracks

Imagine you are running a conference with two tracks (Technical Papers and the Data Showcase) and have two JSON files as exported from HotCRP: msr2021-technical.json and msr2021-data.json.

Let's first transform the Technical Papers. We have two types of files (``Full (10 pages plus 2 additional pages of references)`` and ``Short (4 pages plus 1 additional page of references)``) which correspond to ``10+2`` and ``4+1`` pages respectively, so we use option b) for the ``PAGE_LIMIT`` variable.

As it is the first transformation, we want ``HEADER`` to be ``True`` as to have the labels of the columns in the first line.

Thus, open hotcrp2csv.py and modify the configuration variables as below:

```
ACRONYM = "MSR"  # Acronym of the conference
TRACK = "Technical"  # Track (leave empty if single track)

## Page limit depending on the type of papers. 
## There are two possibilities:
## a) Directly a number (in string format) when there is only one type

#PAGE_LIMIT = "4+1"

## b) A dictionary with all the types of papers:
## Syntax --> Type: Number of pages

PAGE_LIMIT = {
    "Full (10 pages plus 2 additional pages of references)": "10+2",
    "Short (4 pages plus 1 additional page of references)": "4+1"
}

# If you append multiple tracks into a single CSV output file,
# only the first track should have a header. Else, put HEADER to False
HEADER = True
```

Then run:

```
hotcrp2csv.py msr2021-technical.json > msr2021.csv
```


Let's then add the papers from the Data Showcase Track, where there is only one type of papers (all 4+1 pages).
Note that we set the ``HEADER`` constant to ``False`` as we want to append the output to the same CSV file as used before.
Thus, edit hotcrp2csv.py, and modify the variables accordingly:

```
ACRONYM = "MSR"  # Acronym of the conference
TRACK = "Data"  # Track (leave empty if single track)

## Page limit depending on the type of papers. 
## There are two possibilities:
## a) Directly a number (in string format) when there is only one type

PAGE_LIMIT = "4+1"

## b) A dictionary with all the types of papers:
## Syntax --> Type: Number of pages

#PAGE_LIMIT = {
#    "Full (10 pages plus 2 additional pages of references)": "10+2",
#    "Short (4 pages plus 1 additional page of references)": "4+1"
#}

# If you append multiple tracks into a single CSV output file,
# only the first track should have a header. Else, put HEADER to False
HEADER = False
```

And then run:

```
hotcrp2csv.py msr2021-data.json >> msr2021.csv
```

Note ``>>`` that appends to the old CSV (with the Technical Papers) the Data Showcase papers, so that you will have a unique CSV file.


## License

Licensed under GNU General Public License (GPL), version 3 or later.
