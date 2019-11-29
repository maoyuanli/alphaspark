from utils.spark_initializer import SparkInitializer
SparkInitializer.init_spark()
from pyspark.sql.types import *


class SchemaRepository:
    stock_schema = StructType([StructField('Date', DateType(), True),
                               StructField('Open', FloatType(), True),
                               StructField('High', FloatType(), True),
                               StructField('Low', FloatType(), True),
                               StructField('Last', FloatType(), True),
                               StructField('Volumn', DoubleType(), True),
                               StructField('Turnover', DoubleType(), True), ])
