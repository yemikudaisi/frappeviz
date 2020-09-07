# frappe-app-viz

A python app for visualizing class diagram of a [Frappe App's](https://frappeframework.com/) doctypes using [PlantUml](https://plantuml.com/)

## Usage

```python main.py path/to/frappe/app/folder```

The output files will be equivalent to the total amount of modules that contains doctype (i.e the UML for each module in the app is generated in a separate file that shares the same name as the module name)

## TODO
- Add support image output
- Add support for selecting specific modules
