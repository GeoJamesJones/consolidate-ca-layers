import os
import json

import pandas as pd

from arcgis.gis import GIS
from arcgis import features, geometry
from copy import deepcopy




def main():
    portal_items = {
        "Petroleum Facilty":"cc1a961f285d497c9da80ba9d11d2a6d",
        "Commercial Food Distribution Center":"31d53e5c4682438a8b1b84e73a5cc7a3",
        "Generation Station":"ef2eff6274f3467ca6f5674011da25da",
        "Food Retail":"ce2cf6740af845dd9a7b688265aacb36",
        "Food Production Center":"326138ef697a465a96088a805b886d2b",
        "Food Distribution":"17c5bd6810bd42c99826a160462e54a9",
        "Farm Ranch":"824ca9414f3643ccb52d4ba99d2f5366",
        "Government Site Infrastructure":"0c6eb9b8c6a34197bbac32c8a1bafce8",
        "Grain Storage":"cb4a43f9e596484ba6fb19c9bd4bce21",
        "Medical Treatment Facilities":"b08c80ba52b547158a85893484eb3c86",
        "Natural Gas Facility":"1ff4dc17483e4dc38ff1402345f6074b",
        "Propane Facility":"9a909b17bac041cd9e08eff7b0da625e",
        "Warehouse Storage Facility":"fbf015940b834f7e908926df7b651f8d",
        "Civilian Television":"2e533f317c9d44b99f49143387136f5d"
    }

    gis = GIS(r'https://swcs.maps.arcgis.com', os.environ['gis_user'], os.environ['gis_password'])
    print("Successfully connected to GIS.")

    for key, value in portal_items.items():
        portal_item = gis.content.get(value)
        print("Successfully connected to {}".format(key))
        
        flyr = portal_item.layers[0]
        fset = flyr.query()
        all_features = fset.features
        sr = fset.spatial_reference

        features_for_update = []

        for feature in all_features:
            feature_to_be_added = deepcopy(feature)
            for f in feature_to_be_added.attributes:
                print(f)    

if __name__ == "__main__":
    main()