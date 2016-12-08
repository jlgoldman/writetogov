# WriteToGov

Source code for https://www.writetogov.com/, a tool for easily contacting one's elected representatives.

### Setting Up

#### Python Environment and Dependencies

It's highly recommended to use [virtualenv](https://virtualenv.pypa.io/en/stable/).
Create a virtual environment, clone the repo into it, activate the virtualenv, and install requirements.

```bash
virtualenv WriteToGov
cd WriteToGov
git clone https://github.com/jlgoldman/writetogov.git
cd writetogov
# Activate the virtualenv and set the PROJECTPATH environment variable
source env.sh
pip install -r requirements.txt
```

#### Local Configuration Constants

Create a file called `config/constants_override.py`. All variables in this file override
default values found in `config/constants.py`, but `constants_override.py` is kept out of
the GitHub repo so is appropriate for local secrets and settings.

Only the following should be needed in `constants_override.py` for most uses:

```python
DEBUG = True
HOST = 'localhost:5000'
HTTPS = False
# Generate once with import os; os.urandom(24)
FLASK_SECRET_KEY = '...'
# Generate once with import os; os.urandom(24)
PUBLIC_ID_ENCRYPTION_KEY ='...'
# Register for a Google Cloud Console project, go to the Credentials section,
# generate an API key, and enable Google Maps JavaScript API and
# Google Places API Web Service.
GOOGLE_MAPS_API_KEY = '...'
```

#### Setup the Database

Install [PostreSQL](https://wiki.postgresql.org/wiki/Detailed_installation_guides).

Install [PostGIS](http://postgis.net/install/). PostGIS is the geospatial extension for PostgreSQL;
writetogov stores polygons for Congressional districts using PostGIS Geography column types, and
looks up a user's Congressional district from the latlng returned by Google Maps from their address,
using a spatial query.

Create a database called `writetogov`. If using a different name or a non-local database,
override `SQLALCHEMY_DATABASE_URI` in `constants_override.py` with the name and location
of your database.

```bash
createdb writetogov
```

Import the latest database snapshot, which contains data for Congressional districts and representatives,
as well as empty tables for `issue`, `reminder`, etc. Find the latest snapshot in the `data/` directory,
at this writing `writetogov.20161207.sql.zip`.

```bash
unzip data/writetogov.20161207.sql.zip
psql -d writetogov -f writetogov.20161207.sql
```

### Running

```bash
python main.py
```

This runs a debug server on port 5000; then just go to [http://localhost:5000](http://localhost:5000).
