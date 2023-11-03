import requests

# Azure DevOps Configuration
ORG_NAME = "<YOUR_AZURE_DEVOPS_ORG_NAME>"
PROJECT_NAME = "<YOUR_AZURE_DEVOPS_PROJECT_NAME>"
PIPELINE_NAME = "<YOUR_PIPELINE_NAME>"
AZURE_PIPELINE_YAML = "<PATH_TO_YOUR_AZURE_PIPELINE_YAML>"
AZURE_PERSONAL_ACCESS_TOKEN = "<YOUR_AZURE_PERSONAL_ACCESS_TOKEN>"

# Azure DevOps REST API URL
api_url = f"https://dev.azure.com/{ORG_NAME}/{PROJECT_NAME}/_apis/pipelines?api-version=7.1-preview.2"

# Headers for the REST API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {AZURE_PERSONAL_ACCESS_TOKEN}"
}

# Define the pipeline configuration
pipeline_config = {
    "folder": "\\",
    "name": PIPELINE_NAME,
    "configuration": {
        "type": "yaml",
        "path": AZURE_PIPELINE_YAML
    }
}

# Create the pipeline
response = requests.post(api_url, json=pipeline_config, headers=headers)

if response.status_code == 200:
    print(f"Created Azure DevOps Pipeline: {PIPELINE_NAME}")
else:
    print("Failed to create Azure DevOps Pipeline")
    print(response.text)
