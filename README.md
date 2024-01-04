

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/amirkhatami888/PyAdaptiMesh)](https://github.com/amirkhatami888/PyAdaptiMesh/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/amirkhatami888/PyAdaptiMesh)](https://github.com/amirkhatami888/PyAdaptiMesh/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/amirkhatami888/PyAdaptiMesh)](https://github.com/amirkhatami888/PyAdaptiMesh/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/amirkhatami888/PyAdaptiMesh)](https://github.com/amirkhatami888/PyAdaptiMesh/pulls)
![Header Image](https://pyadaptimesh.ir/pyadaptiMesh.jpg)

#PyAdaptiMesh
**PyAdaptiMesh** is a high-performance software solution for optimizing tools in  Adaptive finite element method(AFEM). It is designed to enhance the efficiency of FEA simulations by reducing computational costs and significantly improving execution speed.

## Key Features

- **High-Performance Data Transfer**: PyAdaptiMesh leverages parallel processing on both CPU and GPU to accelerate data transfer between old and new meshes.

- **Support for Large Datasets**: It is capable of handling large quantities of elements, making it suitable for complex simulations.

- **User-Friendly Interface**: PyAdaptiMesh provides a user-friendly Python interface that integrates seamlessly with popular FEA libraries.

- **Efficient Error Reduction**: By improving data transfer efficiency, PyAdaptiMesh contributes to more accurate and efficient FEA simulations.

## Getting Started

To get started with PyAdaptiMesh, follow these steps:

### Installation

 1.Clone the PyAdaptiMesh repository to your local machine:

   ```sh
   git clone https://github.com/your-username/pyadaptimesh.git

   ```
2. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```  

### Usage

this software use two way for using :
1. use the python code in the main.py file and run GUI.py file base on PySide6
2. use the this in the terminal or cmd
for use this software for Calculating information at a point in the domain using both CPU 
```sh

python main_CPU_transferpoint.py CSV_file_name.csv Input_file_name.inp X Y
```
for use this software for Calculating information at a point in the domain using both GPU 
```sh
python main_GPU_transferpoint.py CSV_file_name.csv Input_file_name.inp X Y
```
for Transferring displacement gradient information from one Mesh to another using CPU
```sh
python main_CPU_transferMesh.py CSV_file_name.csv Input_file_name.inp datFile_name.dat save_directory 
```
for Transferring displacement gradient information from one Mesh to another using GPU
```sh
python main_GPU_transferMesh.py CSV_file_name.csv Input_file_name.inp datFile_name.dat save_directory thread_x thread_y
```
for Transferring displacement gradient information from one Mesh to another using GPU and CPU
```sh
python main_GPU_parallel_transferMesh.py CSV_file_name.csv Input_file_name.inp datFile_name.dat save_directory thread_x thread_y number_of_core_for_CPU
```
for use autoMesh Genreation base on adptive finite element method and transfer information from one mesh to another on GPU
```sh
python main_GPU_auto_generateMesh.py CSV_file_name.csv Input_file_name.inp IGES_file_name.igs save_directory  max_iteration_number ratio_selection
```
for use autoMesh Genreation base on adptive finite element method and transfer information from one mesh to another on CPU
```sh
python main_CPU_auto_generateMesh.py CSV_file_name.csv Input_file_name.inp IGES_file_name.igs save_directory  max_iteration_number ratio_selection
```
for ploting and calculating estimation error on mesh on GPU
```sh
python main_GPU_plotError.py CSV_file_name.csv Input_file_name.inp save_directory
```
for ploting and calculating estimation error on mesh on CPU
```sh
python main_CPU_plotError.py CSV_file_name.csv Input_file_name.inp save_directory
```

## License
PyAdaptiMesh is licensed under the MIT License.

