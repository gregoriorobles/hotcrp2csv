# hotcrp2csv
Python script to transform the list of accepted papers from HotCRP's JSON file into IEEE CS spreadsheet format


## Configuration

Edit hotcrp2csv, and modify the following three variables, as in the example below:

```
ACRONYM = "MSR"  # Acronym of the conference
TRACK = "Technical"  # Track (leave empty if single track)

# Page limit depending on the type of papers. 
# Syntax --> Hotcrp type: Number of pages
PAGE_LIMIT = {
    "Full (10 pages plus 2 additional pages of references)": "10+2",
    "Short (4 pages plus 1 additional page of references)": "4+1"
}
```


## Usage

```
usage: hotcrp2csv.py input.json > output.csv

input.json is the list of accepted papers as exported in JSON from HotCRP

output.csv is the output file in CSV format
```


## Conferences with several tracks

Imagine you are running a conference with two tracks (Technical Papers and the Data Showcase) and have two JSON files as exported from HotCRP: msr2021-technical.json and msr2021-data.json.

Edit hotcrp2csv.py, and modify the following three variables:

```
ACRONYM = "MSR"  # Acronym of the conference
TRACK = "Technical"  # Track (leave empty if single track)

# Page limit depending on the type of papers. 
# Syntax --> Hotcrp type: Number of pages
PAGE_LIMIT = {
    "Full (10 pages plus 2 additional pages of references)": "10+2",
    "Short (4 pages plus 1 additional page of references)": "4+1"
}
```

Then run:

```
hotcrp2csv.py msr2021-technical.json > msr2021.csv
```


Let's then add the papers from the Data Showcase Track.
Edit again hotcrp2csv.py, and modify the following three variables:

```
ACRONYM = "MSR"  # Acronym of the conference
TRACK = "Data"  # Track (leave empty if single track)

# Page limit depending on the type of papers. 
# Syntax --> Hotcrp type: Number of pages
PAGE_LIMIT = {
    "Data": "4+1"
}
```

And then run:

```
hotcrp2csv.py msr2021-data.json >> msr2021.csv
```

Note ``>>`` that appends to the old CSV (with the Technical Papers) the Data Showcase papers, so that you will have a unique CSV file.


## License

Licensed under GNU General Public License (GPL), version 3 or later.
