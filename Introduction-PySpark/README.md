# Getting to know Spark

Creating the connection is as simple as creating an instance of the `SparkContext`. The class constructor takes a few optional arguments that allow you to specify the attributes of the cluster you're connecting to.

An object holding all these attributes can be created with the `SparkConf()` constructor.

## Using Dataframes

Spark's core data structure is the Resilient Distributed Dataset (RDD). This is a low level object that lets Spark work its magic by splitting data across multiple nodes in the cluster. However it's hard to work directly with RDD's that's why we generally work with Spark Dataframe abstraction built on top of RDD's.

Spark Dataframes have a lot of optimezation built-in instead of RDD which needs to be careful implemented to have the best performance.

In order to start to work with Spark DataFrames you first have to create ``SparkSession`` object from your ``SparkContext``.

**Example**: 

```
from pyspark.sql import SparkSession

spark = SparkSession.getOrCreate()

print(spark)
```

**View tables available in Spark**:

```
print(spark.catalog.listTables())
```

**Querying tables available in Spark**:

```
query="SELECT * FROM flights LIMIT 10"

flights10 = spark.sql(query)

flights10.show()
```
**It's even possible to convert to Pandas DF**:

```
df = flights10.toPandas()
df.head()
```

## Converting Pandas to Spark

The `.createDataFrame()` method takes pandas DataFrame and returns a Spark DataFrame.

The outputs of this method is stored locally, not in the SparkSession catalog. For example a .sql() that references this Dataframe will throw an error. To access this data you'll need to save it as a temporary view. You can do that by using `createTempoView()` Spark DataFrame method, which take just one argument the name of the table you'd like to register. As it's temporary it can only be access by the current Session. There is also `createOrReplaceTempView()` to avoid human errors.

## Reading Files

```
file_path="/usr/local/share/dataset/test.csv"
airports = spark.read.csv(file_path, header=True)

airports.show()
```

## Creating Columns

Spark Dataframe is `immutable`, so columns can't be updated in place.

There is a method `withColumn` that can get a column info in Spark and returns a new DF to be reassinged to the old DF.

```
df = df.withColumn("newCol", df.oldCol + 1)
```

The above code creates a DataFrame with the same columns as df plus a new column NewCol where every entry is equal to the corresponding entry from oldCol plus one.

To overwrite an existing column just pass the name of the column as the first argument.

In order to open a existing table on Spark use `spark.table('nameofthetable')`

```
flights = spark.table("teste")

flights.head()

flights = flights.withColumn("teste_h", flights.col + 2)

```

## Filtering

Spark's `filter()` method is the SQL counterpart `WHERE` it expectes an true/false expression.

Examples:

```
flights.filter("air_time > 120").show()
flights.filter(flights.air_time > 120).show()

filterA = flights.dest == "SEA"
filterB = flights.dest == "PDX"

selected2 = flights.filter(filterA).filter(filterB)
```

## Selecting

The Spark variant of SQL's `SELECT` is the ``.select()`` method.

The difference between select() and withColumns() is that select() returns only the columns you specify, while withColumn() returns all the columns of the Dataframe in addition to the one you defined. For instance, you need to drop some columns at the beginning of the work, in this case use select()

**Example**

```
selected1 = flights.select("tailnum", "origin", "dest")

# Or

selected2 = flights.select(flights.tailnum, flights.origin, flights.dest)

```

It's also possible to have some transformations with Alias using `.select()` + `alias()` or `selectExpr()` like:

```
selected = flights.selectExpr("ait_time/60 as duration_hours")

# Or

selected2 = flights.select((flights.airtime/60).alias("duration_hrs"))
```
You can also define the variable with the select argument

```
avg_speed = (flights.distance/(flights.air_time/60)).alias("avg_speed")

spped = flights.select("origin","blbabla", avg_speed)

```

## Aggregation

Using `groupBy()` method you can have all aggregations function like: min, max, count, avg, sum...

```
df.groupBy().min("col").show(), it creates a GroupedData object then returns it as DataFrame.

```

**Sum Example**

```
flights.withColumn("duration_hours", flights.air_time/60).groupBy().sum("duration_hours").show()
```

**GroupBy can be specified more fields like**

```
flights.groupBy("someCol").sum("otherCol").show()

```

## Adv Aggregation

There is another method `.agg()` that let you to pass an aggregate column expression that uses any of the aggregate functions from the `pyspark.sql.functions`

```
import pyspark.sql.functions as F

by_month_dest = flights.groupBy("month","dest")

by_month_dest.avg.show()

by_month_dest.agg(F.stddev("dep_delay")).show()

```

## Joining

The Pyspark joins are performed using the DataFrame method `join()`

Tip: Column renaming: .withColumnRenamed("oldname","newname")

```
flights_with_airports = flights.join(airports, on="dest", how="inner")

```

# Machine Learning on Spark

At the core of the `pyspark.ml` module are the ``Transformer`` and ``Estimator`` classes. 

Transformer has a .transform() method that takes a DataFrame and returns a new DataFrame, usually the original one with a column appended, e.g: PCA, Bucketizer

Estimator: classes all implement a .fit method. These methos also takes a DataFrame and returns a model object like randomForestModel, etc.;..

## Data Types

Spark only handles numeric data for modeling, so all columns should be either integer or decimals (called doubles in Spark)

You can use `.cast()` works on columns or `.withColumn()` works on dataframes

```
model_data = model_data.withColumn("someCol", model_data.someCol.cast("integer") )

```

## String Indexer and OneHotEnconder

In order to have only numeric features to Spark model on it, for string columns you can use string indexer and one hot enconder

```
carr_indexer = StringINdexer(inputCol="carrier", outputCol="carrier_index")

carr_enconder = OneHotEncoder(InputCol="carrier_index", outputCol="carrier_fact")

```