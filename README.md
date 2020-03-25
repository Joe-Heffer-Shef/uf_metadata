# Urban Flows Observatory Metadata tools

## Installation

Using pip:

```bash
$ pip install git+https://github.com/Joe-Heffer-Shef/ufmetadata.git
```

Using Conda:

```yaml
name: my_environment
channels:
  - defaults
dependencies:
  - python
  - pip
  - pip:
    - git+https://github.com/Joe-Heffer-Shef/ufmetadata.git
```

## Usage

To view the documentation in Python:

```python
import ufmetadata.assets

help(ufmetadata.assets.Site)
help(ufmetadata.assets.Sensor)
```
