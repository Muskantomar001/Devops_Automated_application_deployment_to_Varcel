import requests

def azure_devops_pipeline():
    #Azure DevOps REST API URL
    url = f"https://dev.azure.com/{ORG_NAME}/{PROJECT_NAME}/_apis/pipelines?api-version=7.1-preview.2"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {personal_access_token}"
    }
    data = {
        "folder": "\\",
        "name": "Your Pipeline Name",
        "configuration": {
            "type": "yaml",
            "path": AZURE_PIPELINE_YAML
        }
    }
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print("Created Azure DevOps Pipeline")
    else:
        print("Failed to create Azure DevOps Pipeline")
        print(response.text)

# Main function
if __name__ == "__main__":
    azure_devops_pipeline()
