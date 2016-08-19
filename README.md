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

 The following command will compile the .coverletter file depicted above to a .coverletter.output file.
 ```bash
 ./covergen compile tutorial.coverletter
 ```
The previous command will create a file named tutorial.coverletter.output that should contain the following text
```
To whom it may concern,

I am awesome

Best regards,
Javed Nissar
```
Explanation of Cover Letter Template Format
--------------

How It Works
--------------
