# cloud-build-demo

### A simple CI/CD pipeline using Cloud Build and Cloud Deploy

* Used Terraform to create resources including two GKE clusters representing dev and prod environments (see [terraform-demo](https://github.com/rebeid/terraform-demo) for more info)
<img width="1728" alt="gke-clusters" src="https://github.com/user-attachments/assets/963852b2-1e59-4326-ac6a-95dc77011bc9">

* Configured Cloud Build to trigger a build pipeline after every commit to a connected GitHub repo
<img width="1728" alt="cloud-build-repositries" src="https://github.com/user-attachments/assets/11693aba-14b9-471f-90e5-0ca25d107371">

* A green build triggers a delivery pipeline by Cloud Deploy
<img width="1728" alt="cloud-build-details" src="https://github.com/user-attachments/assets/091d366c-48fb-4388-9e00-18e03a824ece">

<img width="1728" alt="artifact-registry" src="https://github.com/user-attachments/assets/e8ff68dd-f17e-4074-8645-4dc220793bfe">

* A release is first deployed to dev environment
<img width="1728" alt="dev-cluster-deployment-details" src="https://github.com/user-attachments/assets/d89e8180-0522-425d-ae44-5e274c0ceb90">

* The sample web app is working as expected in dev environment
<img width="1728" alt="sample-web-app" src="https://github.com/user-attachments/assets/35ced737-9c04-453a-ac17-a2bdff848a9e">

* Release promotion to the next environment needs manual steps (promotion + final approval) on Cloud Deploy UI
<img width="1728" alt="cloud-deploy-pipeline" src="https://github.com/user-attachments/assets/d2955970-5f20-4236-a515-b5a6c683355e">
