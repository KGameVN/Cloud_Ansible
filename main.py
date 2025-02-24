import subprocess

def run_ansible_playbook(inventory, playbook):
    command = ["ansible-playbook", "-i", inventory, playbook]
    process = subprocess.run(command, capture_output=True, text=True)
    
    print("STDOUT:", process.stdout)
    print("STDERR:", process.stderr)

if __name__ == "__main__":
    inventory_file = ".hosts.yml"  # Define your Ansible inventory file
    playbook_file = "./Functions/show_vlans.yml"  # Define your playbook file

    run_ansible_playbook(inventory_file, playbook_file)
