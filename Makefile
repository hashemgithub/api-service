# Makefile for API Service

# Variables
APP_NAME := api-service
IMAGE_NAME := hashemabusara/$(APP_NAME)
TAG := latest
HELM_RELEASE := $(APP_NAME)-release

# Targets
.PHONY: build run test clean deploy

build:
	@echo "Building $(APP_NAME)..."
	docker build -t $(IMAGE_NAME):$(TAG) .

run:
	@echo "Running $(APP_NAME)..."
	docker run -p 5000:5000 $(IMAGE_NAME):$(TAG)

test:
	@echo "Running tests..."
	python -m unittest discover tests

clean:
	@echo "Cleaning up..."
	docker rmi $(IMAGE_NAME):$(TAG)

deploy:
	@echo "Deploying $(APP_NAME) using Helm..."
	helm upgrade --install $(HELM_RELEASE) ./helm/$(APP_NAME)
