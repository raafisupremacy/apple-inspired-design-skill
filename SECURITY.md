# Security

This repository is a documentation-only agent skill. It contains Markdown guidance, static CSS/JSON tokens, and two local Python validators. It has no runtime dependency, install hook, post-install script, network client, telemetry, credential handling, or bundled executable.

## Safe installation

Install the skill through the skill manager or by reviewing the repository contents and placing the skill directory in the agent's skills directory. Installation should not require administrator privileges, environment secrets, or a package registry dependency.

## Agent boundaries

The skill instructs an agent to work within the user's selected project. It does not authorize access to unrelated files, credentials, network services, or external systems. Implementation requests still require the normal approval and review controls of the host agent.

## Local checks

The bundled validators use only Python's standard library and read files inside this repository. They do not write project files, access the network, execute subprocesses, or load third-party packages.

Report suspected malicious changes through the repository's issue tracker and include the commit or file path. Do not paste secrets into an issue.
