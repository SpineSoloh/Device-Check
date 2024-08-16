# -*- coding: utf-8 -*-
"""12nd

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rA6RKQEV0bXUbjkA-BCJNYQpyBlMaCh1
"""

import GPUtil

gpus = GPUtil.getGPUs()
for gpu in gpus:
    print(f"GPU {gpu.id} usage: {gpu.load * 100}%")