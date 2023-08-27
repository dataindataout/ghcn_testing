import sqlalchemy as sql
import pandas as pd
import os

import config as cfg

# SQLAlchemy connection string
engine = sql.create_engine(
    "postgresql://{0}:{1}@{2}:{3}/{4}".format(
        cfg.db_user,
        cfg.db_password,
        cfg.db_host,
        cfg.db_port,
        cfg.database,
    )
)

# Input file path
input_filepaths = [
    "/tmp/2011.csv",
]

try:
    for path in input_filepaths:
        # create table with same name as file
        filename, _ext = os.path.splitext(os.path.basename(path))

        # Read in data using above specifications; data types will be auto-detected
        data = pd.read_csv(path)

        # Store data into the database specified in connection string above
        data.to_sql(filename, engine, index=False)

finally:
    engine.dispose()
