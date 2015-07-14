__author__ = 'kws'

import csv
from lxml import etree

stat_names = ["og", "fg", "ibu", "srm", "abv"]

def beer_subcats(tree):
    '''Return a list of subcategories of beers'''
    all_subcats = tree.xpath("//class[@type='beer']/category/subcategory")
    cats_with_stats = [element for element in all_subcats if len(element.xpath("stats/exceptions"))==0]

    return cats_with_stats

def extract_stats(beer_subcat):
    '''Return a dictionary with beer name and statistics'''
    stats = dict(name=beer_subcat.xpath("name")[0].text)
    for stat_name in stat_names:
        stats[stat_name + "_low"] = float(beer_subcat.xpath("stats/" + stat_name + "/low")[0].text)
        stats[stat_name + "_high"] = float(beer_subcat.xpath("stats/" + stat_name + "/high")[0].text)

    return(stats)

def header_names():
    '''Return list of header names for the csv file'''
    stat_low_names = [name + "_low" for name in stat_names]
    stat_high_names = [name + "_high" for name in stat_names]
    header_fields = ["name"] + stat_low_names + stat_high_names
    header = [str(headerfield) for headerfield in header_fields]

    return(header)

def writer(beer_subcats):
    '''Write statistics about the beer subcategories to a csv file'''
    header = header_names()

    with open("beerstats.csv", "w+") as beerfp:
        csvwriter = csv.DictWriter(beerfp, fieldnames=header)
        csvwriter.writeheader()

        for beer_subcat in beer_subcats:
            csvwriter.writerow(extract_stats(beer_subcat))


if __name__=='__main__':
    tree = etree.parse("styleguide2008.xml")
    writer(beer_subcats(tree))
