### Extract
You can pass the db-engine to some libs like pandas and sqlalchemy to perform
some queries.

Extract API using requests
Extract Database using SQLalchemy or pandas

Also explained very briefly about webAPI, JSON format, OLTP and OLAP.

Extract data using Spark from RDBMS
![](./extractspark1.png)

### Transform

Some examples
- Selection of an attribute (eg. email)
![transform1](./transform1.png)
- Translation of code values (New york to NY)
- Data Validation (date input)
- Split columns into multiple columns
- Joining from multiple sources
![](./trasnsform_pyspark_join.png)

#### MPP Databases

Tipically MPP load data better from colunas data files. CSV is NOT a good format for example.
![](mpp.png)

Using parquet (colunas format) from pandas and pyspark

![](parquet.png)

Sending this data to Redshift

![](redshift.png)

Or load to SQL database like POstgres

![](postgres.png)

## Filling Values

![](FillingValues.png)