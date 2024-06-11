# Solutions

## Semi-Structured Data

### Task 2: Create a DTD for the given XML File:

```xml
<!DOCTYPE breakfast_menu [
    <!ELEMENT breakfast_menu (food+)>
    <!ELEMENT food (name, price, description, calories)>
    <!ELEMENT name (#PCDATA)>
    <!ELEMENT price (#PCDATA)>
    <!ELEMENT description (#PCDATA)>
    <!ELEMENT calories(#PCDATA)>
]>
```

Notes:

- the XML has only elements and no attributes, so there's no ATTLIST entry
- One might argue food* vs food+ because it is not clear whether zero elements is possible. But definitively it's a list/sequence
- there are no ID/IDREF nor optional elements (so no #IMPLIED, or ?)

### Task 3: XPath

1. Find the 2nd food-Element of the XML

    ```
    /breakfast_menu/food[2]
```

2. Find the name-Element of the last food of the XML

    ```
/breakfast_menu/food[5]//name -> Works only on our XML snippet
```
```
/breakfast_menu/food[last()]//name -> More robust
```
```
/breakfast_menu/food[last()]/name -> Even more robust
```

3. Find only the name of the last food of the XML (without tags)

    ```
/breakfast_menu/food[last()]/name/text()
```

4. Find all foods with calories below 900
    
    ```
/breakfast_menu/food[calories<900]
```
    
    ```
//food[calories<900]
```

### Task 4: XQuery

1. Return the name of every food above 750 calories

    ```
    xquery version "3.1";
for $food in /breakfast_menu/food
where $food/calories > 750
return $food/name
    ```

    ```
xquery version "3.1";
for $food in //food[calories>750]
return $food/name
    ```

    ```
xquery version "3.1";
for $name in //food[calories>750]/name
return $name
    ```

    ```
xquery version "3.1";
let $names := //food[calories>750]/name
return $names
    ```

    
2. Return the name and price of each food, ordered by the price in ascending order, to fill a prepared HTML-Table (`<table></table`) with the data. (Make the result look something like this: ```<tr><td>name</td><td>price</td></tr><tr>...```)

    >>NOTE: We aim to generate ONLY the content of the table

    ```
    xquery version "3.1";
for $food in /breakfast_menu/food
order by $food/price
  let $name := $food/name
  let $price := $food/price
  return string-join( ("<tr><td>", $name, "</td><td>", $price, "</tr>"), "")
```

    ```
xquery version "3.1";
for $food in /breakfast_menu/food
order by $food/price
return string-join( ("<tr><td>", $food/name, "</td><td>", $food/price, "</tr>"), "")
```

3. Return every food if its name starts with a "B"

    ```
xquery version "3.1";
for $food in /breakfast_menu/food
where starts-with($food/name, "B")
return $food
```
    >> NOTE: use the function `starts-with`

4. Return for all distinct values of calories as a separate HTML paragraph (`<p></p>`) including their own heading (`<h2></h2>`) and an ordered html list (`<ol></ol>`) of the names of all foods with exactly that many calories. 

    ```
    xquery version "3.1";
for $calories in distinct-values(//calories)
order by $calories
let $foods := (
        for $food in //food
        where $food/calories = $calories
        return string-join(("<li>", $food/name, "</li>"), "")
)
return string-join(("<p><h2>Calories: ", $calories,"</h2>",
"<ol>", $foods, "</ol>",
"</p>"), "")
```

    >> NOTE: Use a subquery between `(` and `)`
