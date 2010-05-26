#!/user/bin/env python
"""
scrap coordinates from the files and convert them into a kml file for a given country.
in case the file has multiple poly llines , you have to still do so for all of them


"""
#from django.db import connection
def country_kml(country):
    kml_template="""
    <Placemark>
    <name>%s</name>
    <description>%s</description>
    <Style>
    <PolyStyle>
      <color>44ff0000</color>
      <fill>1</fill>
      <outline>1</outline>
    </PolyStyle>
    <LineStyle>
      <width>2</width>
      <color>%s</color>
    </LineStyle>
  </Style>
  <MultiGeometry>
    <Polygon>
      <outerBoundaryIs>
        <LinearRing>
          <coordinates>
     %s
 
          </coordinates>
        </LinearRing>
      </outerBoundaryIs>
    </Polygon>
  </MultiGeometry>
    
    </Placemark>
    """
    
    
    description_template="<h1>%s figures for %s</h1><span>year %s</span><span>amount %s</span>" %(app,country,year,amount)
def create_polyline():
    return
def pop_list(parent_list,child_list):
    for l in child_list:
        parent.pop(parent.index(l))
    return parent_list    
    
def load(directory):
    import os
    import sys
    for (dirpath,dirnames,filenames) in os.walk(directory):
        for f in filenames:
            try:
                
                file=open(os.path.join(directory,f),'r')
                lines=[]
                lines=list(file.readlines())
                country_name=lines[0]
                if country_name.strip()=='sao':
                    while()
                    
                file.close()
                
            except :
                pass
if __name__=='__main__':
    load("/home/mugisha/Desktop/countries")
            
                
        