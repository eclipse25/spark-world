# 베이스 이미지: Java + Python 환경
FROM openjdk:11-slim

# 1. Python, 기본 유틸리티 설치
RUN apt-get update && \
    apt-get install -y python3 python3-pip procps curl && \
    apt-get clean

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. requirements.txt 복사 및 의존성 설치
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# 4. 프로젝트 복사
COPY projects/churn-prediction/ .

# 5. 실행
CMD ["python3", "scripts/main.py"]
