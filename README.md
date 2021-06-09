<!-- Header -->
<br />
<img src="https://www.dicoding.com/img/bangkit/logo.svg" />
<p align="center">
  <h1 align="center">Virtual Customer Services for Public Services</h1>

  <p align="center">
    Google Bangkit Capstone Project 2021 - CAP0276 - GovIT
    <br />
    <a href="#">View Demo</a>
    ·
    <a href="#">Download APK</a>
    ·
    <a href="https://github.com/B21-CAP0276/capstone-project-B21CAP0276/issues">Report Issues</a>
  </p>
</p>

<!-- TEAM MEMBERS -->
<h4>Team Members</h4>
<ul>
  <li>Muhammad Fahd Ishamuddin - M2492370</li>
  <li>Tria Rahmat Mauludin - M0020048</li>
  <li>Gandara Fajar Umbara - C0121245</li>
  <li>Wahyu Aji Sulaiman - C2001979</li>
  <li>Ni Putu Febrina Sari Wulantari - A1451707</li>
  <li>Alfiah Putri Nuralan - A2782530</li>
</ul>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#background">Background</a></li>
    <li><a href="#model-machine-learning">Model Machine Learning</a></li>
    <li><a href="#gcp-schematic">GCP Schematic</a></li>
    <li><a href="#setup">Setup</a></li>
  </ol>
</details>

For **Android App Development** commit history, please kindly check the [android branch](https://github.com/B21-CAP0276/capstone-project-B21CAP0276/tree/android).

## Background
1. Most of people didn’t understand the requirements or the procedure for using public services
2. Some of them must go to public services place like Kantor Desa/Kelurahan/Kecamatan just for asking the requirements
3. This is very inefficient and can causes a long queues

## Model Machine Learning
![modelling](https://user-images.githubusercontent.com/38114768/121340513-ea8f7d80-c949-11eb-8a17-0ed9bc72246b.png)

## GCP Schematic
![schematic_gcp](https://user-images.githubusercontent.com/38114768/121340584-fda24d80-c949-11eb-9d4d-8be6dbd204a5.png)

## Setup
<!-- Requirements -->
### Requirements
  * [Python:3.6](https://www.python.org/downloads/release/python-360/)
  * [Tensorflow:2.5.0](https://www.tensorflow.org/install/pip)
  * [Flask:1.1.2](https://pypi.org/project/Flask/)
  * [Numpy:1.19.5](https://pypi.org/project/numpy/)
  * [Sastrawi:1.0.1](https://pypi.org/project/Sastrawi/)
  * [Docker:20.10.6](https://docs.docker.com/engine/release-notes/)
  * [Google Cloud Platform](https://cloud.google.com/)

<!-- Step -->
### Steps
* If you're machine learning enthusiast, here is [directory ipynb](https://github.com/B21-CAP0276/capstone-project-B21CAP0276/tree/main/models)
* If you're cloud computing enthusiast. here are the steps:
1. Fork this [repository](https://github.com/B21-CAP0276/capstone-project-B21CAP0276.git) to your repository or clone and upload standalone on GitHub.
2. **Create Service** on Google Cloud Run
3. Type anything you want to service name or region and **Next**
4. Select **Continuosly deploy new revisions from a source repository** in **Configure the service's First Version** .
5. Click **SET UP WITH CLOUD BUILD**.
6. After Pop-uping Set Up With Cloud Build, please check again you are enabled Cloud Build API.
7. Click **Advanced Options** and then **Enable Repository API**.
8. After giving authorize. Choose **GitHub** on **Repository Provider**.
9. Check **Mirror Github Repository using Cloud Source Repositories**.
10. Select your repository.
11. Click **Next**.
12. Chek **Dockerfile** in Build Type section and keep in default.
13. Click **Save**.
14. Back to **Cloud Run** - Create Service. Click **Next**.
15. For authentication please check on **Allow unauthenticated invocations** to allow all incoming connection. After that click **Create**.
16. This process (build artifact) will take 5-10 minutes.

Happy Testing
