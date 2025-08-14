import os

from databricks.connect import DatabricksSession
from databricks.sdk.config import Config

class SparkSession:
    def __init__(self):
        if 'SPARK_HOME' in os.environ:
            print('SPARK_HOME environment variable is set.')
        else:
            self.spark = DatabricksSession.builder.serverless().profile('DEFAULT').getOrCreate()




# https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-connect/python/tutorial-serverless
# https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/install#version-support-matrix
# https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/three
