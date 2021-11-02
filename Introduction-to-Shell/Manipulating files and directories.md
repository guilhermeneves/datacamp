# Basic Commands

cd, ls, pwd


## Copy
How can I copy files?

You will often want to copy files, move them into other directories to organize them, or rename them. One command to do this is cp, which is short for "copy". If original.txt is an existing file, then:

cp original.txt duplicate.txt

creates a copy of original.txt called duplicate.txt. If there already was a file called duplicate.txt, it is overwritten. If the last parameter to cp is an existing directory, then a command like:

cp seasonal/autumn.csv seasonal/winter.csv backup

copies all of the files into that directory.


## Move

Last parameter the folder
mv seasonal/sprin.csv seasonal/summer.csv backup

## rm and mv

mv can also rename folder
rmdir to remove dir, with option -r to delete all files

## LESS, MORE, CAT,HEAD AND TAIL

**LESS**
How can I view a file's contents piece by piece?

You can use cat to print large files and then scroll through the output, but it is usually more convenient to page the output. The original command for doing this was called more, but it has been superseded by a more powerful command called less. (This kind of naming is what passes for humor in the Unix world.) When you less a file, one page is displayed at a time; you can press spacebar to page down or type q to quit.

If you give less the names of several files, you can type :n (colon and a lower-case 'n') to move to the next file, :p to go back to the previous one, or :q to quit.

Note: If you view solutions to exercises that use less, you will see an extra command at the end that turns paging off so that we can test your solutions efficiently.

**HEAD**

How can I look at the start of a file?

The first thing most data scientists do when given a new dataset to analyze is figure out what fields it contains and what values those fields have. If the dataset has been exported from a database or spreadsheet, it will often be stored as comma-separated values (CSV). A quick way to figure out what it contains is to look at the first few rows.

We can do this in the shell using a command called head. As its name suggests, it prints the first few lines of a file (where "a few" means 10), so the command:

head seasonal/summer.csv

`head -n 3 seasonal/summer.csv`

displays:

Date,Tooth
2017-01-11,canine
2017-01-18,wisdom
2017-01-21,bicuspid
2017-02-02,molar
2017-02-27,wisdom
2017-02-27,wisdom
2017-03-07,bicuspid
2017-03-15,wisdom
2017-03-20,canine

What does head do if there aren't 10 lines in the file? (To find out, use it to look at the top of people/agarwal.txt.)

## LS

`LS -F -R`: Returns the structure of subdirect.

## Man Command - help

How can I get help for a command?

To find out what commands do, people used to use the man command (short for "manual"). For example, the command man head brings up this information:

HEAD(1)               BSD General Commands Manual              HEAD(1)

NAME
     head -- display first lines of a file

SYNOPSIS
     head [-n count | -c bytes] [file ...]

DESCRIPTION
     This filter displays the first count lines or bytes of each of
     the specified files, or of the standard input if no files are
     specified.  If count is omitted it defaults to 10.

     If more than a single file is specified, each file is preceded by
     a header consisting of the string ``==> XXX <=='' where ``XXX''
     is the name of the file.

SEE ALSO
     tail(1)

man automatically invokes less, so you may need to press spacebar to page through the information and :q to quit.

The one-line description under NAME tells you briefly what the command does, and the summary under SYNOPSIS lists all the flags it understands. Anything that is optional is shown in square brackets [...], either/or alternatives are separated by |, and things that can be repeated are shown by ..., so head's manual page is telling you that you can either give a line count with -n or a byte count with -c, and that you can give it any number of filenames.

The problem with the Unix manual is that you have to know what you're looking for. If you don't, you can search Stack Overflow, ask a question on DataCamp's Slack channels, or look at the SEE ALSO sections of the commands you already know.

## CUT For selecting columns/lines from a file


How can I select columns from a file?

head and tail let you select rows from a text file. If you want to select columns, you can use the command cut. It has several options (use man cut to explore them), but the most common is something like:

cut -f 2-5,8 -d , values.csv

which means "select columns 2 through 5 and columns 8, using comma as the separator". cut uses -f (meaning "fields") to specify columns and -d (meaning "delimiter") to specify the separator. You need to specify the latter because some files may use spaces, tabs, or colons to separate columns.

What command will select the first column (containing dates) from the file spring.csv?

Another one:
```
echo "abcdefghi" | cut -c2-6
bcdef

```


## How can I repeat commands?

One of the biggest advantages of using the shell is that it makes it easy for you to do things over again. If you run some commands, you can then press the up-arrow key to cycle back through them. You can also use the left and right arrow keys and the delete key to edit them. Pressing return will then run the modified command.

Even better, history will print a list of commands you have run recently. Each one is preceded by a serial number to make it easy to re-run particular commands: just type !55 to re-run the 55th command in your history (if you have that many). You can also re-run a command by typing an exclamation mark followed by the command's name, such as !head or !cut, which will re-run the most recent use of that command.##

## How can I select lines containing specific values?

head and tail select rows, cut selects columns, and grep selects lines according to what they contain. In its simplest form, grep takes a piece of text followed by one or more filenames and prints all of the lines in those files that contain that text. For example, grep bicuspid seasonal/winter.csv prints lines from winter.csv that contain "bicuspid".

grep can search for patterns as well; we will explore those in the next course. What's more important right now is some of grep's more common flags:

    -c: print a count of matching lines rather than the lines themselves
    -h: do not print the names of files when searching multiple files
    -i: ignore case (e.g., treat "Regression" and "regression" as matches)
    -l: print the names of files that contain matches, not the matches
    -n: print line numbers for matching lines
    -v: invert the match, i.e., only show lines that don't match

## Paste

paste command can merge two files:
`paste -d , file1 file2

## Save files, output command

tail -n 5 file > archive.csv

## RUn commands in sequence (PIPE)

What's a better way to combine commands?

Using redirection to combine commands has two drawbacks:

    It leaves a lot of intermediate files lying around (like top.csv).
    The commands to produce your final result are scattered across several lines of history.

The shell provides another tool that solves both of these problems at once called a pipe. Once again, start by running head:

head -n 5 seasonal/summer.csv

Instead of sending head's output to a file, add a vertical bar and the tail command without a filename:

head -n 5 seasonal/summer.csv | tail -n 3

The pipe symbol tells the shell to use the output of the command on the left as the input to the command on the right.

How can I combine many commands?

You can chain any number of commands together. For example, this command:

cut -d , -f 1 seasonal/spring.csv | grep -v Date | head -n 10

will:

    select the first column from the spring data;
    remove the header line containing the word "Date"; and
    select the first 10 lines of actual data.

# How can I count the records in a file?

The command wc (short for "word count") prints the number of characters, words, and lines in a file. You can make it print only one of these using -c, -w, or -l respectively.

Count lines
ex: grep word file.csv | wc -l

# How can I specify many files at once?

Most shell commands will work on multiple files if you give them multiple filenames. For example, you can get the first column from all of the seasonal data files at once like this:

cut -d , -f 1 seasonal/winter.csv seasonal/spring.csv seasonal/summer.csv seasonal/autumn.csv

But typing the names of many files over and over is a bad idea: it wastes time, and sooner or later you will either leave a file out or repeat a file's name. To make your life better, the shell allows you to use wildcards to specify a list of files with a single expression. The most common wildcard is *, which means "match zero or more characters". Using it, we can shorten the cut command above to this:

cut -d , -f 1 seasonal/*

or:

cut -d , -f 1 seasonal/*.csv

The shell has other wildcards as well, though they are less commonly used:

    ? matches a single character, so 201?.txt will match 2017.txt or 2018.txt, but not 2017-01.txt.
    [...] matches any one of the characters inside the square brackets, so 201[78].txt matches 2017.txt or 2018.txt, but not 2016.txt.
    {...} matches any of the comma-separated patterns inside the curly brackets, so {*.txt, *.csv} matches any file whose name ends with .txt or .csv, but not files whose names end with .pdf.

# How can I sort lines of text?

As its name suggests, sort puts data in order. By default it does this in ascending alphabetical order, but the flags -n and -r can be used to sort numerically and reverse the order of its output, while -b tells it to ignore leading blanks and -f tells it to fold case (i.e., be case-insensitive). Pipelines often use grep to get rid of unwanted records and then sort to put the remaining records in order.

#How can I remove duplicate lines?

Another command that is often used with sort is uniq, whose job is to remove duplicated lines. More specifically, it removes adjacent duplicated lines. If a file contains:

2017-07-03
2017-07-03
2017-08-03
2017-08-03

then uniq will produce:

2017-07-03
2017-08-03

but if it contains:

2017-07-03
2017-08-03
2017-07-03
2017-08-03

then uniq will print all four lines. The reason is that uniq is built to work with very large files. In order to remove non-adjacent lines from a file, it would have to keep the whole file in memory (or at least, all the unique lines seen so far). By only removing adjacent duplicates, it only has to keep the most recent unique line in memory.

example:

cut -d , -f 2 seasonal/winter.csv | grep -v Tooth | sort | uniq -c

# How does the shell store information?
Like other programs, the shell stores information in variables. Some of these, called environment variables, are available all the time. Environment variables' names are conventionally written in upper case, and a few of the more commonly-used ones are shown below.

Variable	Purpose	Value
HOME	User's home directory	/home/repl
PWD	Present working directory	Same as pwd command
SHELL	Which shell program is being used	/bin/bash
USER	User's ID	repl
To get a complete list (which is quite long), you can type set in the shell.

Use set and grep with a pipe to display the value of HISTFILESIZE, which determines how many old commands are stored in your command history. What is its value?

# How can I print a variable's value?
A simpler way to find a variable's value is to use a command called echo, which prints its arguments. Typing

echo hello DataCamp!
prints

hello DataCamp!
If you try to use it to print a variable's value like this:

echo USER
it will print the variable's name, USER.

To get the variable's value, you must put a dollar sign $ in front of it. Typing

echo $USER
prints

repl
This is true everywhere: to get the value of a variable called X, you must write $X. (This is so that the shell can tell whether you mean "a file named X" or "the value of a variable named X".)
In order to get the os system env var:
`echo $OSTYPE`

# How else does the shell store information?
The other kind of variable is called a shell variable, which is like a local variable in a programming language.

To create a shell variable, you simply assign a value to a name:

training=seasonal/summer.csv
without any spaces before or after the = sign. Once you have done this, you can check the variable's value with:

echo $training
seasonal/summer.csv

# How can I repeat a command many times?
Shell variables are also used in loops, which repeat commands many times. If we run this command:

for filetype in gif jpg png; do echo $filetype; done
it produces:

gif
jpg
png
Notice these things about the loop:

The structure is for …variable… in …list… ; do …body… ; done
The list of things the loop is to process (in our case, the words gif, jpg, and png).
The variable that keeps track of which thing the loop is currently processing (in our case, filetype).
The body of the loop that does the processing (in our case, echo $filetype).
Notice that the body uses $filetype to get the variable's value instead of just filetype, just like it does with any other shell variable. Also notice where the semi-colons go: the first one comes between the list and the keyword do, and the second comes between the body and the keyword done.


## How can I record the names of a set of files?
People often set a variable using a wildcard expression to record a list of filenames. For example, if you define datasets like this:

datasets=seasonal/*.csv
you can display the files' names later using:

for filename in $datasets; do echo $filename; done
This saves typing and makes errors less likely.

If you run these two commands in your home directory, how many lines of output will they print?

files=seasonal/*.csv
for f in $files; do echo $f; done

# How can I do many things in a single loop?
The loops you have seen so far all have a single command or pipeline in their body, but a loop can contain any number of commands. To tell the shell where one ends and the next begins, you must separate them with semi-colons:

for f in seasonal/*.csv; do echo $f; head -n 2 $f | tail -n 1; done
seasonal/autumn.csv
2017-01-05,canine
seasonal/spring.csv
2017-01-25,wisdom
seasonal/summer.csv
2017-01-11,canine
seasonal/winter.csv
2017-01-03,bicuspid
Suppose you forget the semi-colon between the echo and head commands in the previous loop, so that you ask the shell to run:

for f in seasonal/*.csv; do echo $f head -n 2 $f | tail -n 1; done
What will the shell do?

# Nano Editor

How can I edit a file?
Unix has a bewildering variety of text editors. For this course, we will use a simple one called Nano. If you type nano filename, it will open filename for editing (or create it if it doesn't already exist). You can move around with the arrow keys, delete characters using backspace, and do other operations with control-key combinations:

Ctrl + K: delete a line.
Ctrl + U: un-delete a line.
Ctrl + O: save the file ('O' stands for 'output'). You will also need to press Enter to confirm the filename!
Ctrl + X: exit the editor.

# How can I pass filenames to scripts? ** Arguments
A script that processes specific files is useful as a record of what you did, but one that allows you to process any files you want is more useful. To support this, you can use the special expression $@ (dollar sign immediately followed by at-sign) to mean "all of the command-line parameters given to the script".

For example, if unique-lines.sh contains sort $@ | uniq, when you run:

bash unique-lines.sh seasonal/summer.csv
the shell replaces $@ with seasonal/summer.csv and processes one file. If you run this:

bash unique-lines.sh seasonal/summer.csv seasonal/autumn.csv
it processes two data files, and so on.

As a reminder, to save what you have written in Nano, type Ctrl + O to write the file out, then Enter to confirm the filename, then Ctrl + X to exit the editor.

# How can I process a single argument?
As well as $@, the shell lets you use $1, $2, and so on to refer to specific command-line parameters. You can use this to write commands that feel simpler or more natural than the shell's. For example, you can create a script called column.sh that selects a single column from a CSV file when the user provides the filename as the first parameter and the column as the second:

cut -d , -f $2 $1
and then run it using:

bash column.sh seasonal/autumn.csv 1
Notice how the script uses the two parameters in reverse order.

The script get-field.sh is supposed to take a filename, the number of the row to select, the number of the column to select, and print just that field from a CSV file. For example:

bash get-field.sh seasonal/summer.csv 4 2
should select the second field from line 4 of seasonal/summer.csv. Which of the following commands should be put in get-field.sh to do that?