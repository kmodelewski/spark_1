# ENVIRONMENT SETUP

## PREPARE CATALOG STRUCTURE

```sql
CREATE EXTERNAL VOLUME transportation_dept.bronze.s3
    LOCATION 's3://transportationsparkanalytics'
    COMMENT 'spark_analytics_volume on S3'
  
```