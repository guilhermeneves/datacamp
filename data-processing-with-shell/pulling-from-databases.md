# SQLTOCSV
**It's part of csvkit library**
Sample sintax:
```
sql2csv --db "sqlite:///spotify.db" \
        --query "SELECT * FROM DB" \
        > SPOTI.CSV
```
for postgres o mysql -> postgres:/// or mysql:///

There is also the **csvsql** command that can be issued against csv files to run as SQL statement, it's not recommend for large files or complex queries

`csvsql --query "SELECT * FROM database LIMIT 1` database.csv

you can also pipe to csvlook

`csvsql --query "SELECT * FROM dataset LIMIT 1" \ dataset.csv | csvlook`

multiple files

```
# Store SQL query as shell variable
sql_query="SELECT ma.*, p.popularity FROM Spotify_MusicAttributes ma INNER JOIN Spotify_Popularity p ON ma.track_id = p.track_id"

# Join 2 local csvs into a new csv using the saved SQL
csvsql --query "$sql_query" Spotify_Popularity.csv Spotify_FullData.csv > Spotify_FullData.csv

# Preview newly created file
csvstat Spotify_FullData.csv

```

better use csvstack before.

**Using Variable**

```
# Store SQL query as shell variable
sqlquery="SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1"

# Apply SQL query to Spotify_MusicAttributes.csv
csvsql --query "$sqlquery" Spotify_MusicAttributes.csv

```

Getting values that is repeated:
list_c="track_id danceability duration_ms instrumentalness loudness tempo time_signature track_id popularity"
`echo $list_c | uniq -c | awk '$1==1 {print $2}'`

## Connecting to local database

```
sql2csv --db "postgresql://postgres:1234@127.0.0.1:5432/sandboxdb" --query "SELECT A.id, A.name, A.description, B.id, B.name, B.description FROM sandbox.parent_table A INNER JOIN sandbox.child_table B ON A.id=B.parent_table_id"
```

# Pushing data back to DB

```
csvsql --db "sqlite:///Spotify.db"
       --insert Spotfi.csv

```
**--no-inference**: Disable type inference

**--no-constraints**: Generate schema without length limits or null checks