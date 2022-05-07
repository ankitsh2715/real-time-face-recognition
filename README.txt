Build a distributed application that utilizes Amazon Lambda based PaaS to perform real-time face recognition on real videos recorded by the Raspberry Pi.

Group members names:

Ankit Sharma
Bharath Balaji
Naveen Kumar


To test the end to end flow, use following command on pi terminal:
python3 capture_videos.py

To create a Docker image from docker-image-folder use following commands:
docker build -t ccproj2 .

To tag the image as latest and push it to ECR, use following command with custom account identifiers:
docker tag ccproj2:latest 600083409750.dkr.ecr.us-east-1.amazonaws.com/ccproj2:latest
docker push 600083409750.dkr.ecr.us-east-1.amazonaws.com/ccproj2:latest
