from setuptools import setup, find_packages

setup(
    name="transformers_config",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "transformers",                 # Added transformers dependency
        "numpy>=1.17",
        "dataclasses",
        "huggingface_hub",
        "packaging",
        "filelock",
        "requests",
        "tqdm>=4.27",
        "sacremoses",
        "regex!=2019.12.17",
        "protobuf",
        "tokenizers>=0.11.1,!=0.11.3,<0.13",
        "pyyaml>=5.1",
        "safetensors",
        "fsspec",
        # Add any other necessary dependencies here
    ],
    # ... other setup configurations ...
)

