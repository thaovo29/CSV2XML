def dataSet(name, id):
    s = ""
    s += ("""
    <v:sampleDataSet dataSetName="{0}">
        <certi_id>
          <p>{1}</p>
        </certi_id>
        <name>
          <p>{0}</p>
        </name>
      </v:sampleDataSet>
    """).format(name, id)
    return s


import csv

prefix = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20001102//EN"    "http://www.w3.org/TR/2000/CR-SVG-20001102/DTD/svg-20001102.dtd" [
  <!ENTITY ns_graphs "http://ns.adobe.com/Graphs/1.0/">
  <!ENTITY ns_vars "http://ns.adobe.com/Variables/1.0/">
  <!ENTITY ns_imrep "http://ns.adobe.com/ImageReplacement/1.0/">
  <!ENTITY ns_custom "http://ns.adobe.com/GenericCustomNamespace/1.0/">
  <!ENTITY ns_flows "http://ns.adobe.com/Flows/1.0/">
  <!ENTITY ns_extend "http://ns.adobe.com/Extensibility/1.0/">
]>
<svg>
<variableSets  xmlns="&ns_vars;">
  <variableSet  varSetName="binding1" locked="none">
    <variables>
      <variable varName="username" trait="textcontent" category="&ns_flows;"></variable>
      <variable varName="certi_id" trait="textcontent" category="&ns_flows;"></variable>
      <variable varName="name" trait="textcontent" category="&ns_flows;"></variable>
    </variables>
    <v:sampleDataSets  xmlns:v="http://ns.adobe.com/Variables/1.0/" xmlns="http://ns.adobe.com/GenericCustomNamespace/1.0/">

"""

postfix = """</v:sampleDataSets>
  </variableSet>
</variableSets>
</svg>

"""

body = prefix

with open('Book1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            body += dataSet(row[0], row[1])
        line_count += 1

body += postfix
f = open("test.xml", "w")
f.write(body)
f.close()