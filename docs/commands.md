## Apache Spark 명령어 정리

<br>

### 1. SparkSession 생성

- ``SparkSession.builder.appName("MyApp").getOrCreate()``
  - 설명: 모든 Spark 작업은 SparkSession에서 시작됨. DataFrame API, SQL 등 모든 기능의 진입점
  - 예시: 로컬 세션 생성 후 DataFrame 작업 시작

<br>

### 2. 데이터 불러오기

- ``spark.read.csv(...)``
  - 설명: CSV 파일을 DataFrame으로 불러옴
  - 예시: ``spark.read.csv("file.csv", header=True, inferSchema=True)``

- ``spark.read.parquet(...)``
  - 설명: Parquet 파일을 DataFrame으로 불러옴
  - 예시: ``spark.read.parquet("file.parquet")``

<br>

### 3. 스키마 및 데이터 미리보기

- ``df.printSchema()``
  - 설명: DataFrame의 컬럼 구조와 데이터 타입을 출력함
  - 예시: ``df.printSchema()``

- ``df.show()``
  - 설명: 상위 몇 행의 데이터를 테이블 형태로 출력
  - 예시: ``df.show(5)``

- ``df.describe().show()``
  - 설명: 수치형 컬럼에 대한 통계 정보 요약 출력
  - 예시: ``df.describe().show()``

<br>

### 4. 컬럼 선택 및 필터링

- ``df.select(...)``
  - 설명: 지정한 컬럼만 선택
  - 예시: ``df.select("col1", "col2")``

- ``df.filter(...)``
  - 설명: 조건에 맞는 행만 필터링
  - 예시: ``df.filter(df["col"] > 100)``

- ``df.where(...)``
  - 설명: SQL 스타일의 조건으로 필터링
  - 예시: ``df.where("col = 'value'")``

<br>

### 5. 결측치 처리

- ``df.dropna()``
  - 설명: null 값을 가진 행 제거
  - 예시: ``df.dropna()``

- ``df.fillna(...)``
  - 설명: null 값을 특정 값으로 채움
  - 예시: ``df.fillna(0)``

- ``df.na.fill({...})``
  - 설명: 컬럼별로 다른 값으로 null 대체
  - 예시: ``df.na.fill({"col": 0})``

- ``df.na.drop(subset=[...])``
  - 설명: 특정 컬럼에 null이 있는 행만 제거
  - 예시: ``df.na.drop(subset=["col1", "col2"])``

- ``isNull()``, ``isNotNull()``
  - 설명: null 값 여부 확인용 조건
  - 예시: ``df.filter(col("col").isNotNull())``

<br>

### 6. 컬럼 생성 및 수정

- ``df.withColumn(...)``
  - 설명: 새로운 컬럼 생성 또는 기존 컬럼 수정
  - 예시: ``df.withColumn("new", col("a") + col("b"))``

- ``when().otherwise()``
  - 설명: 조건문 생성 (if-else와 유사)
  - 예시: ``df.withColumn("label", when(col("Churn") == "Yes", 1).otherwise(0))``

- ``df.withColumnRenamed(...)``
  - 설명: 컬럼 이름 변경
  - 예시: ``df.withColumnRenamed("old", "new")``

<br>

### 7. 그룹화 및 집계

- ``df.groupBy(...)``
  - 설명: 컬럼을 기준으로 그룹화
  - 예시: ``df.groupBy("col")``

- ``agg(...)``
  - 설명: 그룹화 후 여러 집계 함수 적용
  - 예시: ``df.groupBy("col").agg(avg("val"), count("val"))``

- ``count()``
  - 설명: 행 수 계산 (전체 또는 그룹별)
  - 예시: ``df.groupBy("col").count()``

- ``round(...)``
  - 설명: 반올림 처리
  - 예시: ``df.withColumn("rounded", round(col("value"), 2))``

<br>

### 8. alias (별칭 부여)

- ``col("col").alias(...)``
  - 설명: 컬럼에 새로운 이름을 부여
  - 예시: ``df.select(col("col").alias("new_name"))``

<br>

### 9. 정렬 및 중복 제거

- ``orderBy(...)``
  - 설명: 지정한 컬럼 기준으로 정렬 (기본 오름차순)
  - 예시: ``df.orderBy("col")``

- ``sort(...)``
  - 설명: orderBy와 동일 기능. 더 짧은 형태로 사용 가능
  - 예시: ``df.sort("col")``

- ``distinct()``
  - 설명: 중복된 행 제거
  - 예시: ``df.select("col").distinct()``

<br>

### 10. 파티션 및 캐싱

- ``repartition(...)``
  - 설명: 파티션 수 재조정
  - 예시: ``df.repartition(10)``

- ``coalesce(...)``
  - 설명: 파티션 수를 줄임 (주로 파일 출력 전에 사용)
  - 예시: ``df.coalesce(1)``

- ``cache()``, ``persist()``
  - 설명: DataFrame을 메모리에 유지
  - 예시: ``df.cache()`` ``df.persist()``

- ``unpersist()``
  - 설명: 캐시 제거
  - 예시: ``df.unpersist()``

<br>

### 11. StringIndexer (문자열 → 숫자 인코딩)

- ``StringIndexer(inputCol=..., outputCol=...)``
  - 설명: 문자열 범주형 데이터를 숫자 인덱스로 변환
  - 예시: ``StringIndexer(inputCol="gender", outputCol="gender_index")``

<br>

### 12. VectorAssembler (피처 통합)

- ``VectorAssembler(inputCols=..., outputCol=...)``
  - 설명: 여러 피처를 하나의 feature 벡터로 결합
  - 예시: ``VectorAssembler(inputCols=["col1", "col2"], outputCol="features")``

<br>

### 13. Pipeline

- ``Pipeline(stages=[...])``
  - 설명: 전처리 및 모델 학습을 하나의 작업으로 구성
  - 예시: ``Pipeline(stages=[indexer, assembler, model])``

<br>

### 14. 모델 학습 및 예측

- ``LogisticRegression(...)``
  - 설명: 로지스틱 회귀 모델 선언
  - 예시: ``LogisticRegression(featuresCol="features", labelCol="label")``

- ``fit(...)``
  - 설명: 모델을 학습 데이터에 학습시킴
  - 예시: ``model = lr.fit(train_df)``

- ``transform(...)``
  - 설명: 학습된 모델로 예측 수행
  - 예시: ``model.transform(test_df)``

<br>

### 15. 모델 평가

- ``BinaryClassificationEvaluator(...)``
  - 설명: 이진 분류 모델의 성능 평가 (AUC 등)
  - 예시: ``BinaryClassificationEvaluator(labelCol="label", metricName="areaUnderROC")``

- ``evaluate(...)``
  - 설명: 예측 결과 평가
  - 예시: ``evaluator.evaluate(predictions)``

<br>

### 16. 데이터 분할

- ``df.randomSplit([...])``
  - 설명: 데이터를 학습/테스트 세트로 분리
  - 예시: ``df.randomSplit([0.8, 0.2], seed=42)``

<br>

### 17. 임시 뷰 등록 및 SQL 사용

- ``createOrReplaceTempView(...)``
  - 설명: DataFrame을 SQL로 조회할 수 있도록 임시 뷰 등록
  - 예시: ``df.createOrReplaceTempView("table")``

- ``spark.sql(...)``
  - 설명: SQL 쿼리 실행
  - 예시: ``spark.sql("SELECT * FROM table")``

<br>

### 18. 기타 함수

- ``col(...)``
  - 설명: 컬럼 객체 참조
  - 예시: ``df.select(col("col1"))``

- ``isin(...)``
  - 설명: 컬럼 값이 주어진 목록에 포함되는지 확인
  - 예시: ``df.filter(col("col").isin("A", "B"))``

- ``drop(...)``
  - 설명: 컬럼 제거
  - 예시: ``df.drop("col1", "col2")``

- ``limit(...)``
  - 설명: 행 수 제한
  - 예시: ``df.limit(10)``

<br>

### 19. Spark 종료

- ``spark.stop()``
  - 설명: Spark 세션 종료