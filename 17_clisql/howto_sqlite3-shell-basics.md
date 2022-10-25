how-to :: sqlite3 shell basics
---
## Overview
The sqlite3 shell is a command line interface (CLI) that allows you to interact with a SQLite database in-memory or as a file, without having to install hundreds of megabytes of software. It is a great, lightweight tool for testing out SQL queries and learning how to use SQLite.

### Estimated Time Cost: 0.5 hours

### Prerequisites:
* SQLite3 installed on your computer
* Willingness to learn (!)
* A good markdown renderer (this document doesn't look nice when raw)

### Pathway to Success
Open up your terminal and type `sqlite3`. You should see something like this:
```ansi
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
<i>Wait, you're going a bit too fast. Can you explain that command in more depth? Specifically, what are the <code>TEXT</code> and <code>INTEGER</code> parts?</i>
</div>
<br>
<br>
<div>
<img src="https://cdn.thdr.me/stuycs/thluffy.png" width="50" height="50" style="margin-right: 15px" align="left">
<i>Yes! The <code>CREATE TABLE</code> command is used to create a new table in the database. The first argument is the name of the table, which you'll be using when you want to retrieve data from it. The second argument is a list of columns, which are the different pieces of data you want to store. Each column has a name and a type. The type is used to tell SQLite what kind of data you're storing in that column. For example, if you want to store a person's name, you would use the <code>TEXT</code> type. If you want to store a person's age, you would use the <code>INTEGER</code> type. Other common types are <code>REAL</code> (for floating point numbers) and <code>BLOB</code> (for binary data). A full list of types can be found <a href="https://www.sqlite.org/datatype3.html">here</a>.
</i>
</div>


Now that we have a table, we can insert data into it. We can do this using the `INSERT INTO` command. You would provide the name of the table, the names of the columns you want to insert data into, and the data itself. Here's an example:
```sql
sqlite> INSERT INTO students (name, age) VALUES ("Thluffy", 15);
```
<div>
<img src="https://cdn.thdr.me/stuycs/me.png" width="50" height="50" style="margin-right: 15px" align="left">
<i>I'm still a bit confused. What does the <code>VALUES</code> part do?</i>
</div>
<br>
<br>
<div>
<img src="https://cdn.thdr.me/stuycs/thluffy.png" width="50" height="50" style="margin-right: 15px" align="left">
<i>Great question! The <code>VALUES</code> part is used to specify the data you want to insert into the table. Since we specified the names of the columns we want to insert data into, we need to provide the same number of values. The values are provided in the same order as the columns. So in this case, we're inserting the name "Thluffy" into the <code>name</code> column and the age 15 into the <code>age</code> column.
</i>
</div>


And that's it! It really is all that simple. You've just created a table and inserted data into it. You can see the data you've inserted by using the `SELECT` command. Here's an example:
```sql
sqlite> SELECT * FROM students;
```

<div>
<img src="https://cdn.thdr.me/stuycs/me.png" width="50" height="50" style="margin-right: 15px" align="left">
<i>What does the <code>*</code> do?</i>
</div>
<br>
<br>
<div>
<img src="https://cdn.thdr.me/stuycs/thluffy.png" width="50" height="50" style="margin-right: 15px" align="left">
<i>The <code>*</code> is a wildcard that tells SQLite to select all columns. You can also specify specific columns if you want to. For example, if you only wanted to select the <code>name</code> column, you would use <code>SELECT name FROM students;</code>.
</i>
</div>

### Let's continue!
*(**Note**: This is extra information beyond the scope of this assignment. Feel free to skip this section if you want to.)*

You can also use the `WHERE` clause to filter the results. Here's an example:
```sql
sqlite> SELECT * FROM students WHERE age > 10;
```

<div>
<img src="https://cdn.thdr.me/stuycs/me.png" width="50" height="50" style="margin-right: 15px" align="left">
<i>What other kinds of filters can I use?</i>
</div>
<br>
<br>
<div>
<img src="https://cdn.thdr.me/stuycs/thluffy.png" width="50" height="50" style="margin-right: 15px" align="left">
<i>There are a lot of different filters you can use. Some of the ones I see most often are <code>LIKE</code>, <code>IN</code>, and <code>NOT</code>. You can find a full list of filters <a href="https://www.sqlite.org/lang_expr.html">here</a>.
</i>
</div>


What if you want to update data in a table? You can do this using the `UPDATE` command. Here's an example:
```sql
sqlite> UPDATE students SET age = 21 WHERE name = "Thluffy";
```

<div>
<img src="https://cdn.thdr.me/stuycs/me.png" width="50" height="50" style="margin-right: 15px" align="left">
<i>I'd love to see some more examples of the <code>UPDATE</code> command.</i>
</div>
<br>
<br>
<div>
<img src="https://cdn.thdr.me/stuycs/thluffy.png" width="50" height="50" style="margin-right: 15px" align="left">
<i>Here are a few more examples:
<ul>
<li><code>UPDATE students SET age = 21;</code> - This will update the age of all students to 21.</li>
<li><code>UPDATE students SET age = age + 1;</code> - This will increment the age of all students by 1.</li>
<li><code>UPDATE students SET age = age + 1 WHERE name = "Thluffy";</code> - This will increment the age of Thluffy by 1.</li>
</ul>
</i>
</div>


And finally, there's always a chance that you'll want to delete data from a table. You can do this using the `DELETE` command. Here's an example:
```sql
sqlite> DELETE FROM students WHERE name = "Thluffy";
```

<div>
<img src="https://cdn.thdr.me/stuycs/me.png" width="50" height="50" style="margin-right: 15px" align="left">
<i>How do I delete all the data in a table?</i>
</div>
<br>
<br>
<div>
<img src="https://cdn.thdr.me/stuycs/thluffy.png" width="50" height="50" style="margin-right: 15px" align="left">
<i>You can use the <code>DELETE</code> command without a <code>WHERE</code> clause to delete all the data in a table. For example, <code>DELETE FROM students;</code> will delete all the data in the <code>students</code> table. Be careful though, because once you delete data, it's gone forever!
</i>
</div>

### Pro tips
*(**Note**: This is extra information beyond the scope of this assignment. Feel free to skip this section if you want to.)*

- SQLite CLI contains numerous shell commands that can be used to perform various tasks. Some of the most useful ones are:
  - `.mode` - This command can be used to change the output mode of the CLI. The choices are ascii, csv, column, html, insert, line, list, tabs, and tcl. The default mode is ascii.
  - `.headers` - This command can be used to toggle the display of column names. The default is on.
  - `.help` - This command can be used to display a list of all the available shell commands.
  - `.exit` - This command can be used to exit the CLI.
  - `.tables` - This command can be used to display a list of all the tables in the database.
  - `.schema` - This command can be used to display the schema of a table. For example, `.schema students` will display the schema of the students table.
  - `.dump` - This command can be used to display the contents of the database. This is useful if you want to save the contents of the database to a file.
  - `.import` - This command can be used to import data from a file into a table. For example, `.import students.csv students` will import the data from the students.csv file into the students table.
  - `.output` - This command can be used to redirect the output of a command to a file. For example, `.output students.csv` will redirect the output of the `SELECT` command to the students.csv file.
  - `.read` - This command can be used to execute a SQL script. For example, `.read students.sql` will execute the SQL commands in the students.sql file.
- You can use the `LIMIT` clause to limit the number of rows returned by a query. Here's an example:
  ```sql
  sqlite> SELECT * FROM students LIMIT 5;
  ```
- One of the most useful features of SQLite is the ability to create views. Views are virtual tables that are created using a query. Here's an example:
  ```sql
  sqlite> CREATE VIEW students_over_10 AS SELECT * FROM students WHERE age > 10;
  ```
  You can then use the `SELECT` command to query the view:
  ```sql
  sqlite> SELECT * FROM students_over_10;
  ```
- Queries can be nested. Here's an example:
  ```sql
  sqlite> SELECT * FROM students WHERE age > (SELECT AVG(age) FROM students);
  ```
- SQLite supports a wide variety of functions. Here's a list of some of the most useful ones:
  - `ABS()` - Returns the absolute value of a number.
  - `AVG()` - Returns the average value of a column.
  - `COUNT()` - Returns the number of rows in a table.
  - `LOWER()` - Converts a string to lowercase.
  - `MAX()` - Returns the maximum value of a column.
  - `MIN()` - Returns the minimum value of a column.
  - `ROUND()` - Rounds a number to a specified number of decimal places.
  - `SUM()` - Returns the sum of a column.
  - `UPPER()` - Converts a string to uppercase.
### Check your understanding
1. Create a table named `krewes` with the following columns:
    - `name` (text)
    - `course` (text)
    - `grade` (integer)
2. Insert a couple of your favorite krewemates (no pun intended) into the table.
3. Update the grade of one of your krewemates to 100.
4. Unfortunately, one of your krewemates is the impostor. Delete them from the table.

### Resources
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [SQLite Practice](https://sqliteonline.com/)

### Images
- [Me (William)](https://cdn.thdr.me/stuycs/me.png)
- [Thluffy](https://cdn.thdr.me/stuycs/thluffy.png)

---

Accurate as of (last update): 2022-10-24

#### Contributors:  
William Vongphanith (content, review, formatting v2, images)   
Julia Lee (content, review, formatting v1)  
Jeffrey Zou (content, review, formatting v1) 