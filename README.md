# Example Python AWS Batch Job

This is an example repo you can fork to create an AWS Batch job. The full process of deploying this repo's Docker Image and the associated AWS Batch infrastrcuture is described in this [article](https://medium.com/@caminmccluskey/setting-up-an-aws-batch-job-to-process-daily-tasks-4d31d6bac257).


## Installation 

First set up a virtual environment to isolate dependencies. You can do this in many ways but as an example:

```bash
$ pyenv virtualenv 3.10.0 <chosen-virtualenv-name>
$ pyenv activate <chosen-virtualenv-name>
```
Then to install dependencies: 

`$ make install`


## Running Locally 

Run `$ make run`


## Deploying to ECR

You may want to use an Github Action to deploy the image to ECR on pushes to the master branch. 

To push new images locally, ensure you have the aws-cli installed then run the following:

```bash
$ aws ecr get-login-password --region <aws-region> --profile <named-profile-with-ecr-access> | docker login --username AWS --password-stdin <aws-account-number>.dkr.ecr.<aws-region>.amazonaws.com
$ docker build -t <your-image-name> .
$ docker tag <your-image-name>:latest <aws-account-number>.dkr.ecr.<aws-region>.amazonaws.com/<ecr-repo-name>:latest
$ docker push <aws-account-number>.dkr.ecr.<aws-region>.amazonaws.com/<ecr-repo-name>:latest
``` 

Note: the above works only for aws-cli versions >2 and the `--profile <named-profile-with-ecr-access` commmand line argument is only neccessary if you have multiple AWS profiles.

