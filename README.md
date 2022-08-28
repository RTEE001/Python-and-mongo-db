Python and MongoDB (256)
For raw project instructions see: http://syllabus.africacode.net/projects/python-specific/mongo/

## Setup

- Create a ".env" file in the main directory
- Have the variables DATABASE_NAME, HOST, USERNAME, PASSWORD
- Assign values to the variables, for this project, the DATABASE_NAME is "UmuziProspects, the host can be any valid host, but for this project simply "localhost:27017" will do. The USERNAME and PASSWORD can be anything of your choice, used in the docker file.
- Install the requirements from the main directory using

```
pip3 install -r requirements.txt
```

- get the docker running using

```
docker compose up
```

- Run the source script from the src directory

```
python3 mongo_db.py
```

- If you need a GUI representation, you can download mongo compass, where you will use the default connection string

```
mongodb://<HOST>
```
