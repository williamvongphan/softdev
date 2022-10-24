how-to :: sqlite3 shell basics
---
## Overview
The sqlite3 shell is a command line interface (CLI) that allows you to interact with a SQLite database in-memory or as a file, without having to install hundreds of megabytes of software. It is a great, lightweight tool for testing out SQL queries and learning how to use SQLite.

### Estimated Time Cost: 0.5 hours

### Prerequisites:
* SQLite3 installed on your computer
* Willingness to learn (!)

### Pathway to Success
Open up your terminal and type `sqlite3`. You should see something like this:
```
SQLite version 3.39.4 2022-09-29 15:55:41
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite>
```

This is the sqlite3 shell. You can type SQL commands here and see the results. Before we can do anything, we need to have some place to store our data. We can create a table using the `CREATE TABLE` command. Here's an example:
```sql
sqlite> CREATE TABLE students (name TEXT, age INTEGER);
```

<div>
<img src="https://cdn.thdr.me/stuycs/me.png" width="50" height="50" style="margin-right: 15px" align="left">
<blockquote>Wait, can you explain that command in more depth? Specifically, what are the <code>TEXT</code> and <code>INTEGER</code> parts?</blockquote>
</div>
<br>
<div>
<img src="https://cdn.thdr.me/stuycs/thluffy.png" width="50" height="50" style="margin-right: 15px" align="left">
<blockquote>Yes! The <code>CREATE TABLE</code> command is used to create a new table in the database. The first argument is the name of the table, which you'll be using when you want to retrieve data from it. The second argument is a list of columns, which are the different pieces of data you want to store. Each column has a name and a type. The type is used to tell SQLite what kind of data you're storing in that column. For example, if you want to store a person's name, you would use the <code>TEXT</code> type. If you want to store a person's age, you would use the <code>INTEGER</code> type. Other common types are <code>REAL</code> (for floating point numbers) and <code>BLOB</code> (for binary data). A full list of types can be found <a href="https://www.sqlite.org/datatype3.html">here</a>.</blockquote>
</div>