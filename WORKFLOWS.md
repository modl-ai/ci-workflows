## Use GitVersion to calculate the appropriate SemVer for this Commit
**Workflow File**: [calc_new_versions.yml](.github/workflows/calc_new_versions.yml)  
**Description**: This workflow uses GitVersion to calculate the appropriate SemVer for the commit on which the
workflow is triggered.
See the Outputs section, as this action generates a variety of tags that can be used later for versioning
or artifact tagging.
### Inputs: 
|*Name*|*Description*|*Type*|*Is Required?*|*Default Value (If not required)*|
|------|-------------|------|--------------|---------------------------------|
| gitversion-config-path | Path to GitVersion.yml (from repo root) | string | false | GitVersion.yml |
| checkout-at-sha | Which commit hash should we use for checkout | string | false | ${{ github.sha }} |
### Outputs: 
|*Name*|*Description*|
|------|-------------|
| NuGetSemVerTag | SemVer Tag - Cleaned up so that NuGet can correctly consume it |
| PIPSemVerTag | SemVer Tag - Cleaned up so that PIP can correctly consume it |
| DockerSemVerTag | Semver Tag - Cleaned up so that Docker can correctly consume it |
| CommitsInBranch | Commits in the Branch - Useful to name other things |
| BranchName | Name of the Branch - Useful to name other things |
## Build and Publish Docker Images to Docker Hub
**Workflow File**: [docker_publish.yml](.github/workflows/docker_publish.yml)  
**Description**: This workflow is for building and publishing Docker images to a docker hub repository given a
Dockerfile and the appropriate credentials.
The published image will be tagged in the following format: `image-name:[image-version-prefix-]image-version`
<br>
Note that the `image-version-prefix` is entirely optional and can be ommitted if it doesn't make sense for your use case.
### Inputs: 
|*Name*|*Description*|*Type*|*Is Required?*|*Default Value (If not required)*|
|------|-------------|------|--------------|---------------------------------|
| image-name | Name of the image to be published (image-name:[image-version-prefix]image-version will be the final format for the tag) | string | true | N/A |
| image-version-prefix | Optional prefix for the image version (image-name:[image-version-prefix]image-version will be the final format for the tag) | string | false | [Empty String] |
| image-version | Image version (image-name:[image-version-prefix]image-version will be the final format for the tag) | string | true | N/A |
| update-latest | Do you also want to publish image-name:[image-version-prefix]latest? | boolean | false | false |
| dockerfile-path | Path to the Dockerfile to use | string | false | ./Dockerfile |
| checkout-at-sha | Which commit hash should we use for checkout | string | false | ${{ github.sha }} |
### Secrets: 
|*Name*|*Description*|*Is Required?*
|------|-------------|-------------|
| DOCKER_HUB_PASSWORD | hub.docker.com Personal Access Token (PAT) |  true |
| DOCKER_HUB_USERNAME | hub.docker.com username |  true |
| DOCKER_BUILD_SECRETS | Any secrets needed by the docker build step |  false |
## Use Bump2Version to Update Version in Required Files
**Workflow File**: [bump_version.yml](.github/workflows/bump_version.yml)  
**Description**: This workflow uses bump2version to keep any files (like setup.py and similar) with the correct
version stamp.
It will update the files and create a new commit.
If you need to use the repository after you run this action, remember to use the NewSha as input for
your `action/checkout@vX`
### Inputs: 
|*Name*|*Description*|*Type*|*Is Required?*|*Default Value (If not required)*|
|------|-------------|------|--------------|---------------------------------|
| new-version | Target Version to which to bump | string | true | N/A |
| bumpversion-cfg-path | Path to the .bumpversion.cfg file (From repo root) | string | false | .bumpversion.cfg |
### Outputs: 
|*Name*|*Description*|
|------|-------------|
| NewSha | Github SHA for commit after bump |
## Greeting Example for Reusable Workflows
**Workflow File**: [hello_world.yml](.github/workflows/hello_world.yml)  
**Description**: This workflow is an example to introduce developers to the concept of
reusable workflows.
### Inputs: 
|*Name*|*Description*|*Type*|*Is Required?*|*Default Value (If not required)*|
|------|-------------|------|--------------|---------------------------------|
| who_dis | Who are we greeting? | string | true | N/A |
| python_version | Which Python should greet them? | number | false | 3.9 |
