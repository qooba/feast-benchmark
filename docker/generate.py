import pandas as pd
import numpy as np
from datetime import datetime, timezone
from sklearn.datasets import make_hastie_10_2
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def generate_entities(size):
    return np.random.choice(size, size=size, replace=False)

def generate_data(entities, year=2021, month=10, day=1) -> pd.DataFrame:
    n_samples=len(entities)
    X, y = make_hastie_10_2(n_samples=n_samples, random_state=0)
    df = pd.DataFrame(X, columns=["f0", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9"])
    df["y"]=y
    df['entity_id'] = entities
    df['datetime'] = pd.to_datetime(
            np.random.randint(
                datetime(year, month, day, 0,tzinfo=timezone.utc).timestamp(),
                datetime(year, month, day, 22,tzinfo=timezone.utc).timestamp(),
                size=n_samples),
        unit="s", #utc=True
    )
    df['created'] = pd.to_datetime(
            datetime.now(), #utc=True
            )
    return df

entities=generate_entities(1000000)

entity_df = pd.DataFrame(data=entities, columns=['entity_id'])
entity_df["event_timestamp"]=datetime(2021, 1, 14, 23, 59, 42, tzinfo=timezone.utc)
entity_df=entity_df[entity_df.entity_id == 100]
#entity_df=entity_df[entity_df.entity_id < 500]
entity_df.to_parquet('./dataset/entity_df.parquet')

all_data=[]

for d in range(1,15):
    data=generate_data(entities,month=1, day=d)
    all_data.append(data)

all_dd=pd.concat(all_data)
all_dd.set_index('datetime')
all_dd.to_parquet("./dataset/all_data.parquet")
