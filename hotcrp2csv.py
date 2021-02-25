#!/usr/bin/env python3
#
# This file is part of hotcrp2csv (https://github.com/gregoriorobles/hotcrp2csv).
# Copyright (c) 2021 Gregorio Robles
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import json
import sys

####################################################################
# Configuration
####################################################################

ACRONYM = "MSR"  # Acronym of the conference
TRACK = "Technical"  # Track (leave empty if single track)

# Page limit depending on the type of papers. 
# Syntax --> Hotcrp type: Number of pages
PAGE_LIMIT = {
    "Full (10 pages plus 2 additional pages of references)": "10+2",
    "Short (4 pages plus 1 additional page of references)": "4+1"
}

####################################################################
# Main program
####################################################################

columns = [
    "Paper Id",
    "Paper Title",
    "First name",
    "Last name",
    "Email",
    "Affiliation",
    "Page Limit",
    "Corresponding Author?"
]

if len(sys.argv) != 2:
    sys.exit("Usage: hotcrp2csv.py hotcrp-exported.json > confname.csv")

with open(sys.argv[1]) as json_file:
    data = json.load(json_file)
    print('"', '","'.join(columns), '"', sep="")
    for pub in data:
        contact_authors = [contact["email"] for contact in pub["contacts"]]
        for author in pub["authors"]:
            contact = 'Y' if author["email"] in contact_authors else 'N'
            affiliation = author.get('affiliation', '')
            if TRACK:
                paper_id = '"' + ACRONYM + "-" + TRACK + "-" + str(pub["pid"])
            else:
                paper_id = '"' + ACRONYM + "-" + str(pub["pid"])
            print(paper_id, pub["title"], author["first"], author["last"], author["email"], affiliation, PAGE_LIMIT[pub["length_paper"]], contact + '"', sep='","')
