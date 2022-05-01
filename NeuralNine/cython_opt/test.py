import main
import time

start_python = time.time()
print(main.find_primes_in_python(50000))
end_python = time.time()

print(end_python-start_python)

start_cython = time.time()
print(main.find_primes_in_cython(50000))
end_cython = time.time()

print(end_cython-start_cython)

print((end_python-start_python) // (end_cython-start_cython))
