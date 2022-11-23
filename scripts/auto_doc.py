import yaml
import argparse
import glob
import os

def input_to_md(name, details, header_lvl='####'):
    default = details.get('default', 'N/A')
    if len(default) == 0 or str.isspace(default):
        default = '[Empty String]'
    result = f"""| {name} | {details.get('description', 'Missing Description - Please Talk to the Author of the Workflow to add a description')} | {details.get('type', 'Missing Type - This is probably an error')} | {details.get('required', False)} | { default } |"""

    return result


def output_to_md(name, details, header_lvl='####'):
    result = f"""| {name} | {details.get('description', 'Missing Description - Please Talk to the Author of the Workflow to add a description')} |"""
    return result

def secret_to_md(name, details, headler_lvl='####'):
    result = f"""\
| {name} | {details.get('description', 'Missing Description - Please Talk to the Author of the Workflow to add a description')} |\
  {details.get('required', False)} |"""
    return result



def workflow_to_doc(workflow_yml):
    ## Get Metadata of the Workflow
    name = workflow_yml['name']

    print(f'## {name}')
    print(f"**Workflow File**: [{workflow_yml['file_name']}]({workflow_yml['full_path']})  ")
    print(f"**Description**: {workflow_yml['verbose_desc']}")

    ## Get Inputs from workflow and create the corresponding text
    inputs = workflow_yml['on']['workflow_call'].get('inputs', {}) ## We can allow for no inputs, but not for lacking on or workflow_call 
    if len(inputs):
        print("### Inputs: ")
        print("|*Name*|*Description*|*Type*|*Is Required?*|*Default Value (If not required)*|")
        print("|------|-------------|------|--------------|---------------------------------|")
    for (input_name, input_details) in inputs.items():
        print(input_to_md(input_name, input_details))

    ## Get Outputs from workflow and create the corresponding text
    outputs = workflow_yml['on']['workflow_call'].get('outputs', {}) ## We can allow for no outputs, but not for lacking on or workflow_call 
    if len(outputs):
        print("### Outputs: ")
        print("|*Name*|*Description*|")
        print("|------|-------------|")
    for (output_name, output_details) in outputs.items():
        print(output_to_md(output_name, output_details))

    ## Get Secrets from workflow and create the corresponding text
    secrets = workflow_yml['on']['workflow_call'].get('secrets', {}) ## We can allow for no secrets, but not for lacking on or workflow_call 
    if len(secrets):
        print("### Secrets: ")
        print("|*Name*|*Description*|*Is Required?*")
        print("|------|-------------|-------------|")
    for (secret_name, secret_details) in secrets.items():
        print(secret_to_md(secret_name, secret_details))


def extract_desc_comment(lines):
    desc = [] 
    start_token = '<--DESC-->'
    end_token   = '<!--DESC-->'
    started = False
    ended = False

    ## First skip all lines that arent relevant until
    ## we find the description start token
    for i in range(0, len(lines)):
        l = lines[i]
        if l[0] == '#' and start_token in l:
            started = True
            break

    ## Grab all comments after the start token, and up until
    ## we find the end token
    for j in range(i+1, len(lines)): 
        l = lines[j]

        if l[0] == '#':
            if end_token in l:
                ## Flatten the list of lines into one
                desc = '\n'.join(desc)
                ended = True
                break

            desc.append(l[1:].strip())

    if not started:
        desc = "No Description Provided"

    if started and not ended:
        ## This is an incorrect
        desc = "Description is incorrectly formatted - This is an error"

    return desc


if __name__ == '__main__':
    ## List all available workflows in the workflows dir 

    parser = argparse.ArgumentParser(prog='Auto Doc for Workflows',
                                     description = 'Turns the ymls in .github/workflows into a summary WORKFLOWS.md')
    parser.add_argument('-w', '--workflows_path', default='../.github/workflows')
    args = parser.parse_args()

    workflows_path = args.workflows_path

    workflows = glob.glob(os.path.join(workflows_path, '*.yml'))

    for wf_file_path in workflows:
        file_name = os.path.basename(wf_file_path)

        if file_name == 'auto_doc_workflow.yml': ## Don't document the workflow triggering the docs :P
            continue

        wf_file = open(wf_file_path)

        lines = wf_file.readlines()

        description = extract_desc_comment(lines)

        ## Rejoin the lines so the yaml library can read it as a single string
        loaded_yml = yaml.load('\n'.join(lines), yaml.BaseLoader)

        loaded_yml['file_name'] = file_name
        loaded_yml['full_path'] = wf_file_path
        loaded_yml['verbose_desc'] = description

        if not 'name' in loaded_yml:
            loaded_yml['name'] = file_name 

        workflow_to_doc(loaded_yml)
