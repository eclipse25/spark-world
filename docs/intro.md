## Apache Spark intro

이 문서는 Apache Spark의 기본 개념과 본 프로젝트에서 어떻게 활용되었는지를 정리한 자료다.  
분산 처리 기반의 대용량 데이터 분석 도구인 Spark는 머신러닝, ETL, 스트리밍 처리 등 다양한 워크로드에 사용된다.

<br>

### Spark란?

Apache Spark는 **인메모리 기반의 분산 처리 시스템**이다.  
기존의 Hadoop MapReduce보다 훨씬 빠르고 유연하며, Python, Java, Scala, R 등 다양한 언어를 지원한다.

- 분산 데이터 처리
- 빠른 실행 속도 (In-Memory 처리)
- 다양한 API (SQL, MLlib, GraphX, Streaming)

<br>

### Spark의 주요 컴포넌트

| 컴포넌트 | 설명 |
|----------|------|
| Spark Core | 분산 처리와 스케줄링의 핵심 |
| Spark SQL | SQL 기반의 질의 지원 (DataFrame, Dataset) |
| MLlib | 머신러닝 라이브러리 |
| Spark Streaming | 실시간 스트리밍 처리 |
| GraphX | 그래프 데이터 처리용 컴포넌트 |

<br>

### 본 프로젝트에서의 활용

- **SparkSession**: 분석의 시작점으로, 로컬 Spark 컨텍스트를 생성
- **DataFrame API**: CSV 데이터 로딩, 전처리, null 제거 등 처리
- **MLlib**: Logistic Regression을 이용한 이탈 예측 모델 학습
- **VectorAssembler**: 여러 입력 컬럼을 하나의 feature 벡터로 변환
- **StringIndexer**: 범주형 컬럼 인코딩

<br>

### 참고할 개념

- **RDD vs DataFrame**  
  RDD는 Spark의 가장 기본적인 분산 데이터 구조로, 각 데이터를 직접 다루는 저수준 API다. 반면 DataFrame은 컬럼이 있는 테이블 형태로 다룰 수 있는 고수준 API이며, Spark SQL과 함께 자동 최적화(Catalyst)를 지원해 더 효율적이다.

  | 구분       | RDD                               | DataFrame                                      |
  |------------|------------------------------------|------------------------------------------------|
  | 추상화 수준 | 저수준 (함수형 프로그래밍 기반)     | 고수준 (SQL-like API)                          |
  | 성능 최적화 | 수동 최적화 필요                   | Catalyst를 통한 자동 최적화                   |
  | 주요 사용처 | 복잡한 로직 처리, 유연한 제어       | 대규모 데이터 처리, 분석, 모델 학습 등        |

- **Transformation vs Action**  
  Spark는 지연 실행(Lazy Evaluation) 구조를 가진다. 즉, Transformation만 쌓아둔 상태에서는 실제 연산이 발생하지 않고, Action이 호출되는 시점에 모든 연산이 실행된다.

  | 구분   | Transformation                         | Action                             |
  |--------|----------------------------------------|------------------------------------|
  | 정의   | 새로운 데이터셋을 만드는 연산             | 실제 결과를 반환하거나 출력하는 연산 |
  | 예시   | `select()`, `filter()`, `withColumn()` | `show()`, `count()`, `collect()`   |
  | 실행 시점 | 실행되지 않고 DAG에 쌓임 (Lazy)         | 전체 연산이 실제로 트리거됨        |

- **파티셔닝과 셔플(Shuffle)**  
  대용량 데이터를 분산 처리할 때는 데이터가 여러 노드에 나뉘어 저장되며, 이를 파티셔닝이라 한다.  
  `groupBy`, `join`처럼 데이터를 재분배해야 하는 연산에서는 노드 간 데이터 이동이 발생하는데, 이를 **Shuffle**이라 한다. 셔플은 성능에 영향을 많이 주기 때문에 피하거나 최소화하는 것이 중요하다.

<br>

### 학습 리소스 및 로드맵

- [Spark 공식 문서](https://spark.apache.org/docs/latest/)
- [Spark SQL과 DataFrame](https://spark.apache.org/docs/latest/sql-programming-guide.html)
- [Databricks Spark Tutorial](https://www.databricks.com/spark/getting-started-with-apache-spark)

1. Spark Core 개념 (RDD → DataFrame 변천)
2. Spark SQL + DataFrame API
3. MLlib을 활용한 머신러닝 모델 개발
4. 실행 구조 및 최적화 (Execution Plan, Transformations, Actions)
5. 클러스터 매니저와 배포 방식

```
Apache Spark
├── Spark Core
│   ├── RDD (Resilient Distributed Dataset)
│   ├── Transformations / Actions
│   ├── Lazy Evaluation
│   └── DAG Scheduler → Stages → Tasks
│
├── Spark SQL
│   ├── DataFrame / Dataset API
│   ├── SQL 쿼리 지원
│   ├── TempView / GlobalTempView
│   ├── Catalyst Optimizer
│   ├── UDF(User Defined Function)
│   └── Window Functions, Join, Aggregation
│
├── MLlib (Machine Learning)
│   ├── Transformers (StringIndexer, VectorAssembler, ...)
│   ├── Estimators (LogisticRegression, RandomForest, ...)
│   ├── Pipeline
│   └── Evaluators (BinaryClassificationEvaluator, etc.)
│
├── Spark Streaming
│   ├── DStream (Discretized Stream)
│   ├── Structured Streaming (DataFrame 기반)
│   └── 실시간 처리 (window, watermark, stateful)
│
├── GraphX
│   └── 그래프 기반 분석 알고리즘 (PageRank, Connected Components 등)
│
├── Execution Model
│   ├── Job
│   │   └── Stage
│   │       └── Task
│   ├── Narrow / Wide Transformations
│   └── Shuffle, Broadcast
│
├── File Format & Storage
│   ├── 지원 포맷: CSV, JSON, Parquet, Avro, ORC
│   ├── Partitioning: 파일 폴더 단위 저장 최적화
│   └── Bucketing: 키 기준으로 데이터 그룹핑
│
├── Hive & Metastore Integration
│   ├── Hive Catalog (enableHiveSupport)
│   ├── Managed Table / External Table
│   └── saveAsTable / createOrReplaceTempView
│
├── Cluster Manager
│   ├── Local[*]
│   ├── YARN
│   ├── Standalone
│   └── Kubernetes
│
├── Deploy Mode
│   ├── Client Mode
│   └── Cluster Mode
│
└── spark-submit
    ├── Resource 설정 (executor-memory, cores, etc.)
    ├── Main 클래스 / 파이썬 파일 지정
    └── 의존성, 환경 설정, 배포 관리
```

<br>