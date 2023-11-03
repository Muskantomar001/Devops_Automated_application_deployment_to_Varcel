def trigger_azure_devops_pipeline():
    url = f"https://dev.azure.com/{ORG_NAME}/{PROJECT_NAME}/_apis/pipelines/{PIPELINE_ID}/runs?api-version=7.1-preview.1"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {personal_access_token}"
    }
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        print("Triggered Azure DevOps Pipeline")
    else:
        print("Failed to trigger Azure DevOps Pipeline")
        print(response.text)
