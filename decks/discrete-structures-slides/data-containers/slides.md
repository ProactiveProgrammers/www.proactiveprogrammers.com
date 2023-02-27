---
# use the default theme
theme: default
# apply any windi css classes to the current slide
class: 'text-center'
# define the highlighter and the colorSchema
highlighter: prism
colorSchema: light
remoteAssets: false
# show line numbers in code blocks
lineNumbers: false
# define the fonts
fonts:
  # define the font for the body text
  sans: 'IBM Plex Sans'
  # define the serif font
  serif: 'IBM Plex Serif'
  # define the code font
  mono: 'IBM Plex Mono'
  # load several font weights
  weights: '200,400,500'
  # support the use of italics
  italic: true
---

[//]: # (Slide Start {{{)

# Discrete Structures

## Data Containers

<div class="container my-5">
  &nbsp;
</div>

### Gregory M. Kapfhammer

### www.proactiveprogrammers.com

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# <em>Okay</em>, what is this about?

<style>
  h2 {
    font-size: 36px;
    @apply text-orange-600 mb-2;
  }
</style>

<br>

<div v-click>

## Key Question

> How do I use the mathematical concepts of **ordered pairs**, **n-tuples**, and
> **lists** to implement functions with a clearly specified behavior to perform
> tasks like the **input** and **parsing** of a comma separated value (CSV)
> file?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some discrete mathematics and Python
> programming concepts, enabling the investigation of practical applications

</div>

<div v-click>

<div class="flex row">

<uim-rocket class="text-5xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Let's explore the use of data containers in Python!
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Understanding Ordered Pairs

<v-clicks>

-   Mathematical concepts yield predictable programs

-   Understanding the concept of an **ordered pair**:

    -   **Pair**: grouping of two entities

    -   **Ordered**: order of entities matters

    -   **Ordered Pair**: grouping of two entities for which order
        matters

    -   **Coordinate on Earth**: latitude and longitude are an ordered
        pair

    -   **Complex Numbers**: real and imaginary parts are an ordered
        pair

    -   An ordered pair is not the same as a set of two elements! Why?

-   Can we generalize to an ordered grouping beyond two entities? How?

</v-clicks>

[//]: # (Slide End }}})

---

# Practical Applications of Ordered Pairs

<v-clicks>

```
🔍 Times Square
  (40.7580° N, 73.9855° W)
  (40.7580, -73.9855)
🔍 Helsinki, Finland
  (60.1699° N, 24.9384° E)
  (60.1699, 24.9384)
```

- Specified according to the standard `(Latitude, Longitude)`

- Latitude and longitude provide a "global address" for a location

- Why does the order matter for these pairs of location data?

- How do you interpret the **positive** and **negative** numbers?

</v-clicks>

---

# Generalizing Ordered Pairs to n-Tuples

<v-clicks>

-   We could have an "ordered triple" or "ordered quadruple"

-   The n-tuple is the generic name for "tuples" of any size
    -   A 2-tuple is the same as an **ordered pair**
    -   A 3-tuple is the same as an **ordered triple**
    -   A 4-tuple is the same as an **ordered quadruple**
    -   n-tuples contain a **finite** number of entities

-   Write n-tuples with notation like $(1,2)$ or $(x,y,z)$

-   n-tuples enable the **creation of new mathematical objects**

-   While the type of entity in an n-tuple may be different, not every
    entity in the n-tuple must be different. This means that **duplicates are possible**!

- Any questions about the **progression** from **ordered pairs** to **n-tuples**?

</v-clicks>

---

# Defining n-Tuples in Python Programs

```python
pair = 3, 4
quadruple = "Story number", 3,
              "is", True

pair = (3, 4)
quadruple = ("Story number", 3,
              "is", True)
```

- The **same data type** is **not** a **requirement** for a tuple

- What are the **data types** of the values in these tuples?

- Which way is the **best** approach to **describing** these tuples?

---

# Special Tuples in the Python Language

<div class = "-mb-3">

```python
empty_tuple = ()
single_story = ("Story",)
single_number = (3,)
number = (3)
```

</div>

- Some tuples may not (yet) contain any data in them!

- Singleton tuples must use the comma notation

- What is the **difference** between a **tuple** and a **number**?
  - Conceptual difference
  - Syntactic difference

- How do we **put data into** and **take data out** of a tuple?

---

# Packing and Unpacking Tuples

```python
# pack a tuple into a variable
pair = (3,4)

# unpack the contents of a tuple
x, y = pair
(x, y) = pair

# unpack and perform simultaneous assignment
x, y = y, x
(x, y) = (y, x)
```

<div class="-mt-2">

Wait, what is the purpose of the last two statements? 🤔

</div>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are key aspects of storing data with tuples?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Tuples are an immutable data structure
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Tuples allow for the storage of duplicates
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Tuples store zero, one, or many values
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Comparison between tuples and lists?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Tuples are immutable and lists are not
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Both allow for the storage of duplicates
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Both store zero, one, or many values
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's explore the use of tuples in Python!
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Find the file in <a href = "https://proactiveprogrammers.com/live">Jupyter Lite</a> or
<a href = "https://githubtocolab.com/ProactiveProgrammers/www.proactiveprogrammers.com">Google Colab</a>!
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-1">
Go to the <code>data-containers/</code> directory
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Explore <code>explore-tuple-containers.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Files in Directories Can Store n-Tuples

<div class="border-2 rounded-2xl border-gray-700 bg-true-gray-300 p-5">

<pre>
tylernelson@gmail.com,Careers adviser
gregory02@medina-mayer.com,"Accountant, management"
jonesmiguel@hotmail.com,Health and safety inspector
rsanchez@yahoo.com,"Surveyor, planning and development"
hillfrank@ward-wood.com,"Scientist, physiological"
aaronhunter@gmail.com,"Surveyor, insurance"
kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer
</pre>

</div>

- **Comma separate value** (CSV) are frequently used in business and science!

- How can we **input** this file of n-tuples into a Python program?

- How do we parse each line based on a **delimiter**?

- How can the program handle **multiple-word** content with **commas**?

---

# Parsing CSV Files in Python

<div class="-mt-3">

```python {all|1|2|3-7|9|10-12|all}
contacts_list = []
for contact_line in csv.reader(
    contacts.splitlines(),
    quotechar='"',
    delimiter=",",
    quoting=csv.QUOTE_ALL,
    skipinitialspace=True,
):
    current_contact_job = contact_line[1]
    if job_description in
           current_contact_job.lower():
        contacts_list.append(contact_line)
```

</div>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Review of the Python code for CSV parsing
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
<code>splitlines</code> breaks the CSV file up into lines
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
<code>delimiter</code> defines the separator for the CSV file
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
<code>contact_line</code> is a single line in the CSV file
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Searching a CSV File with Python

<v-clicks>

<div class="border-2 rounded-2xl border-gray-700 bg-true-gray-300 p-5">

<pre>
tylernelson@gmail.com,Careers adviser
gregory02@medina-mayer.com,"Accountant, management"
jonesmiguel@hotmail.com,Health and safety inspector
rsanchez@yahoo.com,"Surveyor, planning and development"
hillfrank@ward-wood.com,"Scientist, physiological"
aaronhunter@gmail.com,"Surveyor, insurance"
kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer
</pre>

</div>

- What would happen if a person searched for "adviser"?

- What would happen if a person searched for "teacher"?

- Use existing **packages** and **functions** for CSV parsing

- What is most **challenging** about parsing CSV files?

</v-clicks>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are the challenges of parsing CSV files?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Handling missing values or values with delimiters
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Parsing files with corrupted data values
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Difficult to efficiently parse large CSV files
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Applications of Data Containers?

<v-clicks>

-   Programs frequently need to **input data** and **save** it in memory

-   The programs then take data from memory and **save** it to disk

-   Data that is commonly **input and output** by programs:

    -   Scientific **results** from running experiments

    -   Customer **preference** data at e-commerce sites

    -   Analysis of **trends** inside of a data set

-  Common to organize the data into a **list that stores lists**!

-  How is a list of lists similar to a **spreadsheet**?

-  How would you use a list to store a **word processing** document?

</v-clicks>

---

# Tuples are Worth Billions of Dollars!

<v-clicks>

-   Relational databases store **tuples** of data in **rows**

-   Introduction to **relational databases**:

    -   Databases contain **tables** of data

    -   A table consists of **rows** and **columns**

    -   Each **row** of a table is an **n-tuple**

    -   Database tables are specified by **schemas**

    -   Schemas define the **data types** for the **columns**

-   CSV files do not offer enough **structure** or **enforcement**; relational databases
provide an alternative in a relational database management system (**RDBMS**).

</v-clicks>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
How to select the correct data container?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-help-box class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Do you want to change the container's contents?
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-help-box class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
What type of data will the container need to store?
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-help-box class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
How will the containers nest inside of each other?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Using n-Tuples and Lists in Python

<v-clicks>

-   **n-tuples** and **lists** are frequently used in Python programs

-   Python programs can use **CSV files** and **databases**

-   Using n-tuples inside of a Python program:

    -   **Q1**: What is the difference between a **list** and a **tuple**?

    -   **Q2**: How do you **read** a CSV file from the file system?

    -   **Q3**: How do you **parse** a CSV file encoded in a string?

    -   **Q4**: How do you handle the **intricacies** of real-world CSV
        files?

    -   **Q5**: How can a Python program **use** a **relational database**?

-   Connections for n-tuple and applications in computing, business, and
science?

</v-clicks>
