def azure_repo():
    url = f"https://dev.azure.com/{ORG_NAME}/{PROJECT_NAME}/_apis/repositories?api-version=6.0"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {personal_access_token}"
    }
    data = {
        "name": REPO_NAME,
        "project": {
            "id": PROJECT_NAME
        }
    }
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Created Azure DevOps Repo: {REPO_NAME}")
    else:
        print("Failed to create Azure DevOps Repo")
        print(response.text)
