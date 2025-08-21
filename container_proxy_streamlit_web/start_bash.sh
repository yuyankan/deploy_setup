#!/bin/bash

# Define image name and container name
IMAGE_NAME="run_streamlit_spc_maintain_app_image:202507"
CONTAINER_NAME="my_streamlit_spc_maintain_app_container"
HOST_PORT="8020"
CONTAINER_PORT="8501"

# Stop and remove any existing container with the same name
echo "Stopping and removing existing container (if any)..."
docker stop "$CONTAINER_NAME" > /dev/null 2>&1
docker rm "$CONTAINER_NAME" > /dev/null 2>&1
docker rmi "$IMAGE_NAME" > /dev/null 2>&1

# Build the Docker image
echo "Building Docker image: $IMAGE_NAME"
docker build -t "$IMAGE_NAME" .

# Check if the build was successful
if [ $? -ne 0 ]; then
    echo "Docker image build failed. Exiting."
    exit 1
fi

# Run the Docker container in detached mode
echo "Running Docker container: $CONTAINER_NAME on port $HOST_PORT"
docker run -d \
    -p "$HOST_PORT":"$CONTAINER_PORT" \
    --name "$CONTAINER_NAME" \
    "$IMAGE_NAME"

# Check if the container started successfully
if [ $? -ne 0 ]; then
    echo "Docker container failed to start. Check logs for details."
    exit 1
fi

echo "Container '$CONTAINER_NAME' started successfully."
echo "You can check its status with: docker ps"
echo "You can view its logs with: docker logs $CONTAINER_NAME"
echo "Access your Streamlit app at: http://localhost:$HOST_PORT"
