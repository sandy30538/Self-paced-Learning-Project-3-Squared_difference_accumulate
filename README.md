# Self-paced-Learning-Project-3-Squared_difference_accumulate

<br />
<p align="center">

  <h3 align="center">MSOC-HLS Self-paced Learning Project_ - Squared Difference Accumulate</h3>
  
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Usage](#usage)
* [Algorithm](#Algorithm)
* [References](#References)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->
## About The Project
The github repository for hls projects - Squared Difference Accumulate

**Directory structure**
* **README.md** - introduce the project, algorithm, usage, reference and contact information
* **code/**
  * original - The original code from Xilinx application note open source 
  * final - The optimized kernel code is in this directory, also including Python host code 
* **impl/** - result of the implementation, e.g. HLS csynth report
     
<!-- USAGE EXAMPLES -->
## Usage
1. Open Vivado HLS
    * We use **Xilinx ZedBoard Evaluation and Development Kit** to evaulate this project 
    * Add fp_accum.cpp, fp_accum.h into **Source file**
    * Add fp_accum_test.cpp into **Test Bench**

2. Run C Simulation, Run Synthesis, Run Cosimulation, Export IP
3. Open Vivado 2019.2
4. Import IP and create Block design
5. Generate Bitstream
6.Using PYNQ to control Zedboard


## Algorithm
There are 10 random numbers in a[k] and b[k] respectively.  
The Squared difference accumulator calculates **Result = **(a[0]-b[0])^2 + (a[1]-b[1])^2 + ... + (a[9]-b[9])^2  

## References
* [Xilinx HLx_Examples](https://github.com/Xilinx/HLx_Examples)
* [[xhls] FP_accum](https://github.com/Xilinx/HLx_Examples/tree/master/Math/fp_accum)

<!-- CONTACT -->
## Contact
* F07943023@ntu.edu.tw
