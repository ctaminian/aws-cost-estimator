PRICING = {
    "EC2": {
        "t2.micro": 0.0116,   # USD per hour
        "t3.micro": 0.0104,   # USD per hour
        "t3a.micro": 0.0094,  # USD per hour
        "m5.large": 0.096,    # USD per hour
        "m5a.large": 0.086,   # USD per hour
        "c5.large": 0.085,    # USD per hour
        "c5a.large": 0.077,   # USD per hour
        "r5.large": 0.126,    # USD per hour
        "r5a.large": 0.113,   # USD per hour
    },
    "S3": {
        "storage_per_gb": 0.023,           # USD per GB
        "data_transfer_out_per_gb": 0.09,  # USD per GB
    },
    "RDS": {
        "MySQL": {
            "db.t3.micro": 0.0134,  # USD per hour
            "db.t3.small": 0.0268,  # USD per hour
            "db.t3.medium": 0.0536, # USD per hour
            "db.m5.large": 0.10,    # USD per hour
        },
        "PostgreSQL": {
            "db.t3.micro": 0.017,   # USD per hour
            "db.t3.small": 0.034,   # USD per hour
            "db.t3.medium": 0.068,  # USD per hour
            "db.m5.large": 0.12,    # USD per hour
        },
        "MariaDB": {
            "db.t3.micro": 0.0134,  # USD per hour
            "db.t3.small": 0.0268,  # USD per hour
            "db.t3.medium": 0.0536, # USD per hour
            "db.m5.large": 0.10,    # USD per hour
        },
        "Oracle": {
            "db.t3.micro": 0.0752,  # USD per hour
            "db.t3.small": 0.1504,  # USD per hour
            "db.t3.medium": 0.3008, # USD per hour
            "db.m5.large": 0.4000,  # USD per hour
        },
        "SQLServer": {
            "db.t3.micro": 0.034,   # USD per hour
            "db.t3.small": 0.068,   # USD per hour
            "db.t3.medium": 0.136,  # USD per hour
            "db.m5.large": 0.252,   # USD per hour
        },
    },
}
