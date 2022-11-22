import importlib
import rtlobs
import subprocess

from rtlobs import collect as col
from rtlobs import post_process as post

#Command to enable bias-T to power LNA
#(environment variable may not be needed in the future)
ENABLE_BIAST_COMMAND = 'LD_LIBRARY_PATH=/usr/local/lib rtl_biast -b 1'

#
# Enable bias-T
#
print("Enabling bias-T to power LNA")
biast_process = subprocess.Popen(
    ENABLE_BIAST_COMMAND,
    shell=True
)
biast_process.wait()

f, p = col.run_spectrum_int(8192, 2048, 49.6, 2.23e6, 1.420e9, 10)

fig, ax = post.plot_spectrum(f,p, savefig='/home/tele/Pictures/spectrum_int.png')
fig.show()
