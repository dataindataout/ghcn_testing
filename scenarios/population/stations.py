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
    "/tmp/stations.txt",
]

try:
    for path in input_filepaths:
        # create table with same name as file
        filename, _ext = os.path.splitext(os.path.basename(path))

        # lookup tables don't have headers, so specify those here
        headings = [
            "id",
            "latitude",
            "longitude",
            "elevation",
            "state",
            "name",
            "gsn_flag",
            "hcn_crn_flag",
            "wmo_id",
        ]

        # lookup tables are fixed-width files, so specify the widths here
        colspecs = [
            (1, 11),
            (13, 20),
            (22, 30),
            (32, 37),
            (38, 40),
            (41, 70),
            (72, 75),
            (76, 79),
            (80, 85),
        ]

        # Read in data using above specifications; data types will be auto-detected
        data = pd.read_fwf(path, names=headings, header=None, colspecs=colspecs)

        # Store data into the database specified in connection string above
        data.to_sql(filename, engine, index=False)

finally:
    engine.dispose()
