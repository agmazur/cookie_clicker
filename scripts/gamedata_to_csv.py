def shuv_data_to_csv(data):
    import os
    import pandas as pd
    import numpy as np
    project_dir =  os.path.join(os.path.dirname(os.path.abspath(__file__)),"..")
    file_path = os.path.join(project_dir,"Data", "building_data.csv")
    df = pd.read_csv(file_path, sep=",")
    data_building_groputed=data.split(";")
    array_building_count=[]
    for element in data_building_groputed:
        ammount=element.split(",")[0]
        array_building_count.append(ammount)
    df["ammount_currently"]=array_building_count
    print(df)
    df.to_csv(file_path, index=False)