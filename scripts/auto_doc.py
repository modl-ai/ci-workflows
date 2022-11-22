import yaml
import argparse
import glob
import os

def input_to_md(name, details, header_lvl='####'):
    default = details.get('default', 'N/A')
    if len(default) == 0 or str.isspace(default):
        default = '[Empty String]'
    result = f"""| {name} | {details.get('description', 'Missing Description - Please Talk to the Author of the Workflow to add a description')} | {details.get('type', 'Missing Type - This is probably an error')} | {details.get('required', False)} | { default }"""

    return result


def output_to_md(name, details, header_lvl='####'):
    result = f"""| {name} | {details.get('description', 'Missing Description - Please Talk to the Author of the Workflow to add a description')} |"""
    return result



def workflow_to_doc(workflow_yml):
    ## Get Metadata of the Workflow
    name = workflow_yml['name']

    print(f'## {name}')

    ## Get Inputs from workflow and create the corresponding text
    inputs = workflow_yml['on']['workflow_call'].get('inputs', {}) ## We can allow for no inputs, but not for lacking on or workflow_call 
    if len(inputs):
        print("### Inputs: ")
        print("|*Name*|*Description*|*Type*|*Is Required?*|*Default Value (If not required)*|")
        print("|----|----|----|----|----|")
    for (input_name, input_details) in inputs.items():
        print(input_to_md(input_name, input_details))

    ## Get Outputs from workflow and create the corresponding text
    outputs = workflow_yml['on']['workflow_call'].get('outputs', {}) ## We can allow for no outputs, but not for lacking on or workflow_call 
    if len(outputs):
        print("### Outputs: ")
        print("|*Name*|*Description*|")
        print("|----|----|----|----|----|")
    for (output_name, output_details) in outputs.items():
        print(output_to_md(output_name, output_details))

    print('##')



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
        loaded_yml = yaml.load(wf_file, yaml.BaseLoader)

        if not 'name' in loaded_yml:
            loaded_yml['name'] = file_name 

        workflow_to_doc(loaded_yml)
