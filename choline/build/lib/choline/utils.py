import os

def cholinePath(local_path, remote_path):
    is_remote = os.environ.get('cholineremote')
    if is_remote:
        return remote_path
    else:
        return local_path
