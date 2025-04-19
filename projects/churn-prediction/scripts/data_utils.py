from pyspark.sql.functions import col

def load_data(spark, path):
    return spark.read.csv(path, header=True, inferSchema=True)

def clean_data(df):
    # TotalCharges를 double로 변환
    df = df.withColumn("TotalCharges", col("TotalCharges").cast("double"))
    # 주요 컬럼 기준 null 제거
    return df.na.drop(subset=["TotalCharges", "MonthlyCharges", "tenure", "Churn"])
