# cloud-build-demo

A simple build pipeline for Cloud Build to execute in response to my GitHub repo changes (See [terraform-demo](https://github.com/rebeid/terraform-demo) for automated Cloud Build trigger setup)

<img width="1728" alt="cloudbuild-history-screenshot" src="https://github.com/user-attachments/assets/935bf70b-ed50-41ab-8cfd-eb5c78d932ad">


It builds, pushes (to Artifact Registry) and deploys a sample web app, which listens on port 8090, on a new VM instance.

<img width="800" alt="app-screenshot" src="https://github.com/user-attachments/assets/661a5f66-263c-47f9-a866-1c9f4e7835cf">
