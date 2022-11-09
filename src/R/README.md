# R Support

## Setup 
Generate the shared object file that R can consume.
```bash
make r
```

Inside `main.r` we show an example of GNOLL usage.

- Load in the shared object
- Delete the temporary file that contains GNOLL output
- Call GNOLL
- Parse result

## Notes
This example uses the .C function which is usually not recommended. The recommended way to call C code in R is through the .Call() function. See [#368](https://github.com/ianfhunter/GNOLL/issues/368)