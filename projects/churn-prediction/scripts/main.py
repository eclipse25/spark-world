import logging
from pyspark.sql import SparkSession
from data_utils import load_data, clean_data
from features_and_model import prepare_features, train_model, evaluate_model

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("SparkSession 초기화")
    spark = SparkSession.builder.appName("ChurnPrediction").getOrCreate()

    logger.info("데이터 로드")
    df = load_data(spark, "data/Telco_customer_churn.csv")

    logger.info("데이터 정제")
    df = clean_data(df)

    # 피처 정의
    categorical_cols = ["gender", "SeniorCitizen", "Partner", "Dependents", "PhoneService",
                        "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup",
                        "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies",
                        "Contract", "PaperlessBilling", "PaymentMethod"]
    numeric_cols = ["tenure", "MonthlyCharges", "TotalCharges"]

    logger.info("피처 전처리")
    df = prepare_features(df, categorical_cols, numeric_cols)

    logger.info("데이터 분할")
    train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

    logger.info("모델 학습")
    model = train_model(train_df)

    logger.info("모델 평가")
    auc = evaluate_model(model, test_df)

    logger.info(f"ROC AUC Score: {auc:.4f}")
    spark.stop()
