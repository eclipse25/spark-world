from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

def prepare_features(df, categorical_cols, numeric_cols):
    # Churn → label
    label_indexer = StringIndexer(inputCol="Churn", outputCol="label", handleInvalid="skip")

    # 각 범주형 컬럼 → 인덱스
    indexers = [
        StringIndexer(inputCol=col, outputCol=f"{col}_index", handleInvalid="skip")
        for col in categorical_cols
    ]

    pipeline = Pipeline(stages=[label_indexer] + indexers)
    df = pipeline.fit(df).transform(df)

    # VectorAssembler
    input_cols = [f"{col}_index" for col in categorical_cols] + numeric_cols
    df = VectorAssembler(
        inputCols=input_cols,
        outputCol="features",
        handleInvalid="skip"
    ).transform(df)

    return df

def train_model(train_df):
    lr = LogisticRegression(featuresCol="features", labelCol="label")
    return lr.fit(train_df)

def evaluate_model(model, test_df):
    predictions = model.transform(test_df)
    evaluator = BinaryClassificationEvaluator(labelCol="label", metricName="areaUnderROC")
    auc = evaluator.evaluate(predictions)
    return auc
