# Advanced String Methods In Python

Let's take a look at more of the ways Python facilitates string methods

```
myStr = 'That is Alice's cat'
```

The above doesn't work, python thinks the string ends after the e in alice, and the rest s cat is just invalid python syntax

An easy workaround is to always use double quotes or use double quotes when you know for certain a string will contain a single quote char ' somewhere

```
myStr = "That is Alice's cat"
```

However in some instances you may need to use both double and single quotes within a string:

```
# To do this use an escape character: '\'

myStr = 'That is Alice\'s cat and the cat says "meow"'
```
