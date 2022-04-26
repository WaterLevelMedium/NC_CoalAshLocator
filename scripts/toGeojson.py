#this is a rough program that will dump to the geoJson file format.
# the indent=4 line formats the geojson vertically

import csv, json
from geojson import Point, Feature, FeatureCollection, dump
#sample point
point = Point((-115.81, 37.24))
with open('assets/Coal Ash Structural Fills (Closed).csv', newline='') as csvfile:

    reader = csv.DictReader(csvfile,delimiter=',')
    fillVolumes = list() #cubic yards!!
    for row in reader:
        print( row['estCuYd'], row)
        try:
            row['estCuYd'] = float(row['estCuYd'].replace(',',''))
        except ValueError:
            row['estCuYd'] = 'NODATA'
        finally:
            fillVolumes.append(row['estCuYd'])
    ave = 0
    for n in fillVolumes:
        if isinstance(n,float) == True:
            ave += n
        print(n)
    ave = ave / len(fillVolumes)
    # min = 200
    # max = 905,238
    print('\n\n\n',fillVolumes,'\nAverage:',round(ave,4),'Cubic yds. coal ash used in fill')

#feature_collection = FeatureCollection(features)
#with open('output.geojson', 'w') as f:
#       dump(feature_collection, f , indent=4)
