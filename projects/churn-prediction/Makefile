PROJECT_NAME=churn-prediction
DOCKERFILE=Dockerfile
IMAGE_NAME=churn-app

build:
	docker build -f $(DOCKERFILE) -t $(IMAGE_NAME) ../../

run:
	docker run --rm $(IMAGE_NAME)
