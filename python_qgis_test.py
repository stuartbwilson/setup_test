from qgis.core import *

QgsApplication.setPrefixPath("C:\Program Files (x86)\QGIS 3.10", True)

qgs = QgsApplication([], False)

qgs.initQgis()

path_to_layer = r"c:\qgis_training\national_park.shp"

vLayer = QgsVectorLayer(path_to_layer, "NatParks_lyr", "ogr")

import urllib

params = {
    'service': 'WFS',
    'version': '1.1.0',
    'request': 'GetFeature',
    'typename': 'nmpwfs:protected_sites_deep_sea_marine_reserve',
    'srsname': "EPSG:3857"
}
    
uri2 = 'https://msmap1.atkinsgeospatial.com/geoserver/nmpwfs/ows?token=d46ffd2a-e192-4e51-8a6a-b3292c20f1ee' + urllib.unquote(urllib.urlencode(params))

if not vLayer.isValid():
    print("Layer not valid")
    
    
    
#print("end")
    


#vLayer = QgsVectorLayer(r"c:\QGIS_training\national_park.shp", "NatparkLyr", "ogr")

#uri = 'http://ogc.bgs.ac.uk/digmap625k_gsml_insp_gs/wfs?srsname=EPSG:23030&typename=union&version=4.1&request=GetFeature&service=WFS'

#vLayer = QgsVectorLayer(uri, "WFS_Layer", "WFS")



#_writer = QgsVectorFileWriter.writeAsVectorFormat(layer, r"c:\QGIS_Training\bgs_test.shp",layer.crs(), "ESRI Shapefile")

#feats_count = vLayer.featureCount()

#print(feats_count)



qgs.exitQgis







