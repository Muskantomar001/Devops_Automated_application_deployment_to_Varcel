def push_code_ADO():
    os.chdir(SERVICE_CODE_PATH)
    os.system("git init")
    os.system(f"git remote add origin https://dev.azure.com/{ORG_NAME}/{PROJECT_NAME}/_git/{REPO_NAME}")
    os.system("git add .")
    os.system("git commit -m 'Initial commit'")
    os.system("git push -u origin --all")


