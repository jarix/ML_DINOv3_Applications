"""
A script that sets an environment variable for the project based on the operating system.
"""

import os
import sys


# Environment Variables to set
ENV_VAR_NAME_1 = "DINOv3_REPO"
ENV_VAR_NAME_2 = "DINOv3_WEIGHTS"


def set_env_variables():
    """
    Detects the operating system and sets the ENV_TEST environment variable.
    """
    if sys.platform.startswith('win'):
        # Windows
        print(f"Running in {sys.platform} ...")
        os.environ[ENV_VAR_NAME_1] = "/MyGithubPlayground/dinov3"
        os.environ[ENV_VAR_NAME_2] = "/Pretrained_Models\dinov3"

    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        # Linux or macOS
        print(f"Running in {sys.platform} ...")
        os.environ[ENV_VAR_NAME_1] = "~/MyGithubPlayground/dinov3"
        os.environ[ENV_VAR_NAME_2] = "~/Pretrained_Models\dinov3"

    else:
        print(f"*** ERROR: Unsupported operating system: {sys.platform}")
        sys.exit()

    print(f"Environment variable '{ENV_VAR_NAME_1}' set to '{os.environ.get(ENV_VAR_NAME_1)}'")
    print(f"Environment variable '{ENV_VAR_NAME_2}' set to '{os.environ.get(ENV_VAR_NAME_2)}'")


if __name__ == "__main__":
    set_env_variables()
    # You can verify the variable within the same script or a child process.
    # Note: This environment variable will only be set for the current process
    # and any child processes spawned by it. It will not persist after the script exits.
    print(f"Verifying {ENV_VAR_NAME_1}: {os.getenv(ENV_VAR_NAME_1)}")
    print(f"Verifying {ENV_VAR_NAME_2}: {os.getenv(ENV_VAR_NAME_2)}")


