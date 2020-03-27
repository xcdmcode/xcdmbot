import subprocess
import threading
from github import Github
from config import config

gh = Github(config['github_token'])

repo_name = "xcdmcode/xcdmbot"

def get_long_hash(subprocess=subprocess):
    return subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8')

def check_for_updates():
    repo = gh.get_repo(repo_name)
    newest_hash = repo.get_commits()[0].sha.strip()
    current_hash = get_long_hash().strip()

    if newest_hash != current_hash:
        return True

    return False

def autoupdate():
    subprocess.run(['chmod', 'u+rx', 'update.sh'])
    subprocess.run(['bash', 'update.sh'])

def periodic_autoupdate():
    if check_for_updates():
        autoupdate()

    threading.Timer(300, periodic_autoupdate).start()