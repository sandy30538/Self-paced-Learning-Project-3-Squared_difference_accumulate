
# coding: utf-8

# In[ ]:


from __future__ import print_function
from random import random
from random import seed
from random import uniform

import sys
import numpy as np

sys.path.append('/home/xilinx')
from pynq import Overlay
from pynq import allocate

if __name__ == "__main__":
    print("Entry:", sys.argv[0])
    print("System argument(s):", len(sys.argv))

    print("Start of \"" + sys.argv[0] + "\"")

    ol = Overlay("/home/xilinx/IPBitFile/diff_sq_acc.bit")
    ip = ol.diff_sq_acc_0
    
    outBuffer0 = allocate(shape=(1,), dtype=np.int32)

    # Assign Value
    a = []
    b = []
    for i in range(10):
        a.append(uniform(2.5, 10.0))
        b.append(uniform(2.5, 10.0))
        print("value " + str(i) + " is " + str(floating_point_value))

    # Write input a
    for i in range(10):
        ip.write(0x10 + i * 4, a[i])
    
    # Write input b
    for i in range(10):
        ip.write(0x18 + i * 4, b[i])

    ip.write(0x20, outBuffer0.device_address)
    ip.write(0x00, 0x01)
    while (ip.read(0x00) & 0x4) == 0x0:
        continue

    print("Result: " + str(outBuffer0))
    print("============================")
    print("Exit process")

