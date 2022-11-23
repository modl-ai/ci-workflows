# ci-workflows
Repository of Reusable Workflows

## Welcome!! 
This is a list of reusable workflows that we commonly utilize at modl.ai

## Disclaimer
:warning::warning::warning:  
**MODLERS PLEASE BE AWARE**: This is a public repository because GitHub requires us to put shared workflows in Public repositories.
Do not discuss anything private or potentially confidential in this repository.  
:warning::warning::warning:  


## Using these workflows
In order to use any of these workflows - You just need to follow the usual ['Calling Reusable Workflows'](https://docs.github.com/en/actions/using-workflows/reusing-workflows#calling-a-reusable-workflow) instructions.

For example, if you wanted to call our `hello_world` workflow - You'd add the following yml:
```yaml
on:
  pull_request:
    branches: [main]

jobs:
  call-remote-wf:
    uses: modl-ai/ci-workflows/.github/workflows/hello_world.yml@v1 ## Make sure you're pointing to the right version / branch 
    with:
      who_dis: "It's a me, Mario!"
      python_version: 3.8
```

Please look into the [WORKFLOWS](./WORKFLOWS.md) file to get a list of all the supported workflows and their respective parameters.
