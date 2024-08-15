#!/bin/bash

export APP_NAME="CrewMail"
export SUPPORT_EMAIL="souriya.khaosanga@gmail.com"
export BRAND_NAME="sour@chainable.co"
export OAUTH_CLIENT_NAME="credentials.json"
export REDIRECT_URIS="http://localhost:54702/"
export API_NAME="gmail.googleapis.com"
export PROJECT_ID="glassy-grin-432523-e7"


# Set the project to use
gcloud config set project $PROJECT_ID

# Enable the required API
gcloud services enable $API_NAME

# Create OAuth brand
gcloud alpha iap oauth-brands create --application_title="$APP_NAME" --support_email="$SUPPORT_EMAIL"

# Create OAuth client ID
gcloud alpha iap oauth-clients create $BRAND_NAME --display_name="$OAUTH_CLIENT_NAME" --redirect_uris="$REDIRECT_URIS" --type="WEB"

echo "Google Cloud project setup complete with OAuth client."