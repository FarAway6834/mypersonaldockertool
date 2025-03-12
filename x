#!/bin/sh
chmod u+x ./x
docker build -t farawayjams/mypersonaldockertool:latest ./
docker push farawayjams/mypersonaldockertool:latest