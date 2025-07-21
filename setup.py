from setuptools import setup

if __name__ == "__main__":
    try:
        setup()
    except Exception as e:
        print(
            "\nAn error occurred while building the project.\n"
            "Please make sure you have the latest versions of the following packages installed:\n"
            "  - setuptools\n"
            "  - setuptools_scm\n"
            "  - wheel\n"
            "\nYou can update them using:\n"
            "  pip install -U setuptools setuptools_scm wheel\n"
        )
        raise e
