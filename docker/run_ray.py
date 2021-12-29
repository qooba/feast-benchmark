from feast import FeatureStore
import pandas as pd

import ray
from ray.util.dask import ray_dask_get
import time
ray.init()
dask.config.set(scheduler=ray_dask_get)
store = FeatureStore(repo_path=".")

start_time = time.time()
training_df = store.get_historical_features(
    entity_df=pd.read_parquet('./dataset/entity_df.parquet'), 
    features = [
        'my_statistics:f0',
        'my_statistics:f1',
        'my_statistics:f2',
        'my_statistics:f3',
        'my_statistics:f4',
        'my_statistics:f5',
        'my_statistics:f6',
        'my_statistics:f7',
        'my_statistics:f8',
        'my_statistics:f9',
        'my_statistics:y',
    ],
).to_df()

print(training_df)
print("--- %s seconds ---" % (time.time() - start_time))
