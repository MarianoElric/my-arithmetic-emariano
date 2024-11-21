# my-arithmetic-emariano

[![PyPI - Version](https://img.shields.io/pypi/v/my-arithmetic-emariano.svg)](https://pypi.org/project/my-arithmetic-emariano)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/my-arithmetic-emariano.svg)](https://pypi.org/project/my-arithmetic-emariano)

-----

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [License](#license)

## Description

This project is an exercise for La Rochelle Université that focuses on experimenting with GitLab CI/CD. The goal is to gain hands-on experience with runners, pipelines, and jobs. The project utilizes various tools and technologies, including Docker, GitLab Runner, Hatch, Hatch-VC, and GitLab itself.

The project is designed to be executed on an Ubuntu machine. It provides a comprehensive learning opportunity for understanding the concepts and workflows involved in setting up and running CI/CD pipelines using GitLab.

To get started with this project, make sure you have the necessary dependencies installed on your Ubuntu machine. This includes Docker, GitLab Runner, Hatch, and Hatch-VC. Once the dependencies are set up, you can clone the project repository from GitLab and navigate to the project directory.

Inside the project directory, you will find the necessary configuration files and scripts to set up your CI/CD environment. The `.gitlab-ci.yml` file defines the pipeline stages and jobs. You can customize these files according to your specific requirements.

To execute the pipeline, you need to register a runner on your Ubuntu machine and configure it to connect to your GitLab instance. This can be done by following the instructions provided in the GitLab Runner documentation. Once the runner is set up and connected, you can trigger the pipeline execution by pushing changes to the repository or manually triggering a pipeline run from the GitLab UI.

## Installation

To get started with this project, follow these steps:

1. Install Docker on your Ubuntu machine by following the official Docker documentation.
2. Install GitLab Runner on your Ubuntu machine by following the official GitLab Runner documentation.
3. Install Hatch and Hatch-VC on your Ubuntu machine by following the respective documentation for each tool.
4. Clone the project repository from GitLab to your local machine.
5. Navigate to the project directory.

## Usage

Once you have completed the installation steps, you can start using this project:

1. Configure the GitLab Runner to connect to your GitLab instance.
2. Customize the `.gitlab-ci.yml` file to define your desired pipeline stages and jobs.
3. Customize the `Dockerfile` to specify the container environment for job execution.
4. Push changes to the repository or manually trigger a pipeline run from the GitLab UI to execute the pipeline.

## License

This project is licensed under the MIT License. For more information, please refer to the [LICENSE](LICENSE) file.


## Installation

```console
pip install my-arithmetic-emariano
```

## License

`my-arithmetic-emariano` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
