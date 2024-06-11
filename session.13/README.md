# Session 13 - 12/06/24

## NoSQL - Document Database - Neo4J

### Task 1 Setup

Start a new graph database server:

```docker run --name neo --publish=7474:7474 --publish=7687:7687 --env=NEO4J_AUTH=none -d neo4j```
 
Check that everything is running ok by visiting:

`http://localhost:7474`

Use the GUI to connect to the server and then:

### Task 2

- Lists all available databases (`:dbs`)
- Connect to the `neo4j` database with (`:use <db>`)
- Show an overview of the database (`CALL db.schema.visualization()`) 

More info at:
[https://neo4j.com/docs/cypher-manual/4.0/](https://neo4j.com/docs/cypher-manual/4.0/)

and

[https://neo4j.com/developer/get-started/](https://neo4j.com/developer/get-started/)

### Task 3

Connect to the running Neo4J with the browser.

Start by following the introduction steps of neo4j by working through their "Movie Graph" tutorial (`:play movie graph`). 

You can also look here for a step-by-step guide:
[https://neo4j.com/developer/cypher/guide-cypher-basics/](https://neo4j.com/developer/cypher/guide-cypher-basics/)

Make sure to execute (and verify) the CREATE-Step before trying anything else of this exercise. 

> Note: DO NOT RUN the Clean-up step before completing the exercise. Otherwise, you won't have data to work with!!

1. Show all nodes and their relationships in your database
2. Output the amount of created nodes
3. Output the amount of created relationships
4. Find all titles of movies in the database
5. Return all people who acted in the Movie with the title "Sleepless in Seattle"
6. Return all actors who acted besides "Keanu Reeves"
7. Print out the node and the number of its relationships of the node with the largest amount of relationships
8. Insert a new movie which is not already in the database, including its actors, director(s), and a producer

## Semi-Structured Data

### Task 1 Setup

Find helpful information, tutorials, and examples of DTD, XSD, XPath and XQuery at the following link:
[https://www.w3schools.com/xml/](https://www.w3schools.com/xml/)

Verification of DTD and XSD can be done via: [https://www.xmlvalidation.com/](https://www.xmlvalidation.com/)

Verification of XPath and XQuery can be done via: 
[http://xpather.com/](http://xpather.com/) or 
[https://www.videlibri.de/cgi-bin/xidelcgi](https://www.videlibri.de/cgi-bin/xidelcgi)

### Task 2: DTD
Create a DTD for the given XML File:

```xml
<breakfast_menu>
        <food>
               <name>Belgian Waffles</name>
               <price>$5.95</price>
               <description>Two famous Belgian Waffles with plenty of real maple syrup</description>
               <calories>650</calories>
        </food>
        <food>
               <name>Strawberry Belgian Waffles</name>
               <price>$7.95</price>
               <description>Light Belgian waffles covered with strawberries</description>
               <calories>900</calories>
        </food>
        <food>
               <name>Berry-Berry Belgian Waffles</name>
               <price>$8.95</price>
               <description>Light Belgian waffles covered with fresh berries and cream</description>
               <calories>900</calories>
        </food>
        <food>
               <name>French Toast</name>
               <price>$4.50</price>
               <description>Thick slices made from our homemade sourdough bread</description>
               <calories>600</calories>
        </food>
        <food>
               <name>Homestyle Breakfast</name>
               <price>$6.95</price>
               <description>Two eggs, bacon or sausage, toast, and hash browns</description>
               <calories>950</calories>
        </food>
</breakfast_menu>
```

### Task 3: XPath

Based on the XML from Task 1, write the following XPaths and their results:

1. Find the 2nd food-Element of the XML
2. Find the name-Element of the last food of the XML
3. Find only the name of the last food of the XML (without tags)
4. Find all foods with calories below 900

### Task 4: XQuery
Based on the XML from Task 1 formulate the following XQuery. Write them down as well as their results.

1. Return the name of every food above 750 calories
2. Return the name and price of each food, ordered by the price in ascending order, to fill a prepared HTML-Table (`<table></table`) with the data. (Make the result look something like this: ```<tr><td>name</td><td>price</td></tr><tr>...```)
3. Return every food if its name starts with a "B"
4. Return for all distinct values of calories as a separate HTML paragraph (`<p></p>`) including their own heading (`<h2></h2>`) and an ordered html list (`<ol></ol>`) of the names of all foods with exactly that many calories. 

    The result is supposed to look like this (actual result has to contain all 5 foods):
    
    ```HTML
    <p>
        <h2>Calories: 900</h2>
        <ol>
            <li>
                <name>Strawberry Belgian Waffles</name>
            </li>
            <li>
                <name>Berry-Berry Belgian Waffles</name>
            </li>
        </ol>
    </p>
    ```