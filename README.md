# Frappe App Visualizer

A python app for visualizing class diagrams of a [Frappe App's](https://frappeframework.com/) doctypes using [PlantUML](https://plantuml.com/)

![Screenshot](https://github.com/yemikudaisi/frappe_viz/raw/master/docs/library_management.png)

## Dependencies

- [Python 3](https://www.python.org/download/releases/3.0/)
- [PlantUML](https://pypi.org/project/plantuml/)

## Installation
```
$ pip install frappeviz
```

## Usage
### Command Line
```
$ frappeviz [-h] [--output output-dir] [--format {txt,img,all}]
                 frappe-app-directory
```

#### Example
    $ frappeviz path/to/frappe/app/dir -o /path/to/output/dir -f img

### Module
```
>>> from frappeviz import generate_uml
>>> generate_uml('path/to/frappe/app/dir', '/path/to/output/dir' 'img')
```

### Arguments
- -h: help
- --output / -o: output directory
- --format / -f: Output format (txt | img | all)
- frappe directory

The UML for each module in the app is generated in separate files (PlantUML text and .png images) that shares the same name as the app's respective modules.

## Supported Environment
Tested on the following OS:
- Ubuntu OS
- macOS
