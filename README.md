Covergen
=========

How To Install It
-------------

Tutorial
-------------
First, start by creating a new directory and entering the directory.
```bash
mkdir example
cd example
```
Then, write the following in example.json.
```JSON
{
  "awesome":"I am awesome"
}
```

After that, write the following and save it in tutorial.coverletter

```python3
import example

To whom it may concern,

{example[awesome]}

Best regards,
Javed Nissar
 ```

 The following command will compile the .coverletter file depicted above to a
 .coverletter.output file.
 ```bash
 ./covergen compile tutorial.coverletter
 ```
The previous command will create a file named tutorial.coverletter.output that
should contain the following text
```
To whom it may concern,

I am awesome

Best regards,
Javed Nissar
```
Explanation of Cover Letter Template Format
--------------
All cover letters have the .coverletter file extension, these cover letters are
written so that they have two types of lines, import lines and text lines.
```python3
import example #an import line
Hello world #a text line
```
Import lines are for importing new data and text lines have any variables within
them replaced with data obtained from the imports. This feature is demonstrated
below.
```python3
import example #an import line

I don't but I do like {example[favorite]}.
```
In this example, ```{example[favorite]}``` refers to the data contained in the
JSON file example at the key 'favorite'. This JSON file could be written as
follows.
```JSON
{
  "favorite":"JSON"
}
```
