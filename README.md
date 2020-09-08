# frappe-app-viz

A python app for visualizing class diagram of a [Frappe App's](https://frappeframework.com/) doctypes using [PlantUml](https://plantuml.com/)

## Requirements

- [Python 3](https://www.python.org/download/releases/3.0/)
- [PlantUML](https://pypi.org/project/plantuml/)

## Usage

```
$ pip install -r requirements.txt
$ python main.py path/to/frappe/app/dir -o /path/to/output/dir
```

### Arguments
- frappe folder path
- --output - output folder

The output files will be equivalent to the total amount of modules that contains doctype (i.e the UML for each module in the app is generated in a separate file that shares the same name as the module name)

## TODO
- [x] Add support for output folder argument
- [ ] Generate UML in current working directory if output folder argument is not passed
- [ ] Add support for selecting specific modules within an app
