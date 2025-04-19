## churn-prediction

고객 이탈 예측(Churn Prediction)은 고객이 서비스를 해지하거나 떠나는 걸 미리 예측해서, 이탈을 줄이고 고객 유지를 높이는 것을 목표로 하는 분석/모델링 프로젝트다.

이 프로젝트에서는 Kaggle에서 공개된 **Telco Customer Churn** 데이터를 활용해 PySpark 기반으로 탐색적 데이터 분석(EDA)을 진행하고, 이탈 여부를 예측하는 모델을 만들어본다.  

<br>

### 🔍 Background

- `churn`이란 **고객 이탈**을 의미한다.
- 이탈 가능성이 높은 고객을 미리 파악하면, 할인이나 혜택 같은 전략으로 떠나는 걸 막을 수 있다.
- 기업에서 자주 활용되는 고객 분석(Customer Analytics)의 대표적인 예시

<br>

### 📦 Dataset

- 출처: [Kaggle - Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- 데이터 개요:
  - **고객 개인 정보**: `gender`, `SeniorCitizen`, `Partner`, `Dependents`
  - **서비스 정보**: `InternetService`, `StreamingTV`, `TechSupport`, ...
  - **계약 정보**: `tenure`, `Contract`, `PaymentMethod`
  - **요금 정보**: `MonthlyCharges`, `TotalCharges`
  - **이탈 여부 (`Churn`)**: 예측 대상 label

<br>

### 🎯 Project Goals

1. **PySpark를 활용한 대규모 데이터 탐색 및 전처리**
2. **고객 이탈 여부를 분류하는 예측 모델 개발**
3. **이탈 고객의 특성 분석을 통한 인사이트 도출**

<br>
