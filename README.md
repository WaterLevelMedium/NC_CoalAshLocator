
------
### NC Coal Ash Structural Fill Site Locator

------

### Description

 <p>  &emsp; This web mapping application utilizes data from the<a href='https://deq.nc.gov/'> North Carolina Department of Environmental Quality </a></br><i><a href='https://deq.nc.gov/about/divisions/waste-management/science-data-and-reports/waste-management-gis-data-and-maps'> Division of Waste Management Site Locator Tool</a></i>.</br> </br> </br>
<b>Data</b></br>

- Each point feature on the map depicts a coal ash structural fill site, wherein the size of the circle is proportional to the volume (in cubic yards).
- The map also utilizes the <a href='https://www.nconemap.gov/datasets/NCDOT::ncdot-county-boundaries'> North Carolina Department of Transportation </a> County Boundary Shapefile to be used as reference. </br>

<b>Methods</b>
- This web map makes use of the Leaflet and Jquery libraries, and data for both the NC County Boundary overlay and the coal ash fill sites were downloaded as GeoJson Feature Collections.
- Proportional Scaling for circle sizes was based primarily on working numbers, i.e., figures were adjusted to roughly represent variance between the volume of coal ash used in the structural fill at each site. Additionally, sites completed before 1/4/1994 were not subject to reporting, and were defaulted to the set average. **Note: Radius units in display pixles.**
- The forumla used to calculate each circle size is as follows { (((Volume of Coal Ash at Site^in cubic yards^) / 2)^.5^ ) * .1 = Calculated Radius of Circle }
- When the average value was observed for a site (*NODATA* , *Pre 1/4/1994*) , the radius value was set to 9px.
- Each site features a popup with a brief information including address, date, name, county, and metrics for coal ash used.

</p>

----
*River Pyle 2022*
