## bump_version.yml
### Inputs: 
|*Name*|*Description*|*Type*|*Is Required?*|*Default Value (If not required)*|
|------|-------------|------|--------------|---------------------------------|
| new-version | Target Version to which to bump | string | true | N/A |
| bumpversion-cfg-path | Path to the .bumpversion.cfg file (From repo root) | string | false | .bumpversion.cfg |
### Outputs: 
|*Name*|*Description*|
|------|-------------|
| NewSha | Github SHA for commit after bump |
##
## hello_world.yml
### Inputs: 
|*Name*|*Description*|*Type*|*Is Required?*|*Default Value (If not required)*|
|------|-------------|------|--------------|---------------------------------|
| who_dis | Who are we greeting? | string | true | N/A |
| python_version | Missing Description - Please Talk to the Author of the Workflow to add a description | number | false | 3.9 |
##
## Publish Images to Docker
### Inputs: 
|*Name*|*Description*|*Type*|*Is Required?*|*Default Value (If not required)*|
|------|-------------|------|--------------|---------------------------------|
| image-name | Name of the image to be published (image-name:[image-version-prefix]image-version will be the final format for the tag) | string | true | N/A |
| image-version-prefix | Optional prefix for the image version (image-name:[image-version-prefix]image-version will be the final format for the tag) | string | false | [Empty String] |
| image-version | Image version (image-name:[image-version-prefix]image-version will be the final format for the tag) | string | true | N/A |
| update-latest | Do you also want to publish image-name:[image-version-prefix]latest? | boolean | false | false |
| dockerfile-path | Path to the Dockerfile to use | string | false | ./Dockerfile |
| checkout-at-sha | Which commit hash should we use for checkout | string | false | ${{ github.sha }} |
##
## calc_new_versions.yml
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
##
