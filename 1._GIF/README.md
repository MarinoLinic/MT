Check information about the GIF version (first line of output says whether it's GIF 89a or GIF 87):

```bash
od -c file.gif | head -2
```

See general information about the GIF (4th and 5th figures are width and height, but should be first and second)

```bash
od -x file.gif | head -2
```
