# Frappe App Visualizer

A python app for visualizing class diagrams of a [Frappe App's](https://frappeframework.com/) doctypes using [PlantUML](https://plantuml.com/)

![Screenshot](https://github.com/yemikudaisi/frappe_viz/raw/master/docs/library_management.png)

## Dependencies

- [Python 3](https://www.python.org/download/releases/3.0/)
- [PlantUML](https://pypi.org/project/plantuml/)

## Usage

```
$ git clone https://github.com/yemikudaisi/frappe-app-viz.git
$ cd frappe-app-viz
$ pip install -r requirements.txt
$ python main.py path/to/frappe/app/dir -o /path/to/output/dir
```

### Arguments
- frappe folder path
- --output : output folder

The UML for each module in the app is generated in separate files (PlantUML text and .png images) that shares the same name as the app's respective modules.

## TODO
- [x] Add support for output folder argument
- [ ] Add support for selecting specific modules within an app
