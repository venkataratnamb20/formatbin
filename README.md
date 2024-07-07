[![formatbin-dev](https://github.com/venkataratnamb20/formatbin/actions/workflows/dev.yml/badge.svg)](https://github.com/venkataratnamb20/formatbin/actions/workflows/dev.yml)

# FormatBin

## Execution Steps


## Requirements
### input files

- input.txt (<filename>.txt)
file containing a column of binary data in multiples of `n`.
### output files

Following files contains xor(transform(data, `mxn`), transformed_shifted_by_1). n and file numbers are given by user.
- input_01.txt
- input_02.txt
- input_03.txt
- input_04.txt
- input_05.txt
- input_06.txt
- input_07.txt
- input_08.txt
- input_09.txt
- input_<n>.txt

#### Other output files

Following files contains 

- input_a.txt
    sum(xor(data, shifted_by_1))
- input_b.txt
    xor(data, shifted_by_1) transformed back to `nx1`
- input_c.txt
    xor(input_data, shifted_by_1)