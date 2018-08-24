# Database of Art Historians API
> Small API for Database of Art Historians Project

![](header.png)

## Installation

Setup the Application:

```sh
pip -r requirements.txt
python create_db.py
python fill_db.py
```

Running the Application:
```
python app.py

navitate to:
localhost:5000/api/historian
```

## Usage example

Query All Historians:<br>
curl http://127.0.0.1:5000/api/historian/30

Query Historian #30:<br>
curl http://127.0.0.1:5000/api/historian/30

Search for Historian with name like "Anthony":<br>
curl \ -G \ -H "Content-type: application/json" \ -d "q={\"filters\":[{\"name\":\"name\",\"op\":\"like\",\"val\":\"%Anthony%\"}]}" \ http://127.0.0.1:5000/api/historian

_For more examples and usage, please refer to the [Wiki][wiki]._

## Release History
* 0.0.1
    * Work in progress

## Meta

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/dukewired/database_art_historians_api](https://github.com/dukewired/database_art_historians_api/)

## Contributing

1. Fork it (<https://github.com/dukewired/database_art_historians_api/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
