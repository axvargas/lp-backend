# Lenguajes de Programacioon - Dart CR7 version

## Prerequisites
python3.8 or greater

## Create virtual environment and install requirements
### Windows
```
py -m virtualenv venv
```
or
```
py -m venv venv
```
then
```
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Linux
```
py -m virtualenv venv
```
or
```
py -m venv venv
```
then
```
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

## Run backend server
Being inside the project directory run the next commands
### Windows
```
python -m manage runserver
```

### Linux
```
python3 -m manage runserver
```

# Test the backend
The endpoint to test the Dart CR7 version analyzer is
```
http://127.0.0.1:8000/api/analyzer/
```

You should make a POST request with the following body

```
{
    "code" : "int cadena == | 'hello';"
}
```
Where code is the string you want to analyze