from pyspark.sql.functions import count, when, col, round

def show_churn_rate_by(df, colname):
    result = (
        df.groupBy(colname)
        .agg(
            count("*").alias("total"),
            count(when(col("label") == 1, True)).alias("churned")
        )
        .withColumn("churn_rate(%)", round(col("churned") / col("total") * 100, 2))
        .orderBy("churn_rate(%)", ascending=False)
    )
    result.show(truncate=False)
