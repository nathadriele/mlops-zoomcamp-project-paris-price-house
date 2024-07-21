import pandas as pd
from sklearn.model_selection import train_test_split

def load_dataset(file_path):
    data = pd.read_csv(file_path)
    features = ['squareMeters', 'numberOfRooms', 'hasYard', 'hasPool', 'floors', 'cityCode', 'cityPartRange', 
                'numPrevOwners', 'made', 'isNewBuilt', 'hasStormProtector', 'basement', 'attic', 'garage', 
                'hasStorageRoom', 'hasGuestRoom']
    target = 'price'
    X = data[features]
    y = data[target]
    return train_test_split(X, y, test_size=0.2, random_state=42)

