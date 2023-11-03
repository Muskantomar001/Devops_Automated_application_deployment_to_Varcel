def deploy():
    
    url = f"https://api.vercel.com/v1/projects/{VERCEL_PROJECT_ID}/deployments"  #vercel REST API
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {VERCEL_TOKEN}"
    }
    data = {
        "name": "Deployment Name",
        "target": "production"
    }
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print("Triggered deployment in Vercel")
    else:
        print("Failed to trigger deployment in Vercel")
        print(response.text)
