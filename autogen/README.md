# Running Agentic AI Applications on Intel® Core™ Ultra Processor using AutoGen and IPEX-LLM/Ollama  

## Device under Test   
Processor: Intel® Core™ Ultra 7 165H (22 Cores)  
iGPU: Intel® Arc™ Graphics (OpenCL Driver: 24.17.29377.6)   
RAM: 64GB   
Disk Capacity: 2TB
OS: Ubuntu 22.04 (Kernel: 6.5.0-18-generic)   
Python: 3.10.12   
ipex-llm: 2.2.0b20241001   
pyautogen: 0.3.0   

## Activating GPU Driver   
1. Activate iGPU by adding the following line to /etc/default/grub   
```
GRUB_CMDLINE_LINUX="i915.force_probe=7d55"
```
2. Update grub and reboot the system
```
sudo update-grub
```

## Installation Steps   

1. Install oneAPI
```
wget -O- https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEYINTEL-
SW-PRODUCTS.PUB | gpg --dearmor | sudo tee
/usr/share/keyrings/oneapi-archive-keyring.gpg > /dev/null

echo "deb [signed-by=/usr/share/keyrings/oneapi-archivekeyring.
gpg] https://apt.repos.intel.com/oneapi all main" | sudo
tee /etc/apt/sources.list.d/oneAPI.list   

sudo apt update   
sudo apt install intel-oneapi-common-vars=2024.0.0-49406 \
intel-oneapi-common-oneapi-vars=2024.0.0-49406 \
intel-oneapi-diagnostics-utility=2024.0.0-49093 \
intel-oneapi-compiler-dpcpp-cpp=2024.0.2-49895 \
intel-oneapi-dpcpp-ct=2024.0.0-49381 \
intel-oneapi-mkl=2024.0.0-49656 \
intel-oneapi-mkl-devel=2024.0.0-49656 \
intel-oneapi-mpi=2021.11.0-49493 \
intel-oneapi-mpi-devel=2021.11.0-49493 \
intel-oneapi-dal=2024.0.1-25 \
intel-oneapi-dal-devel=2024.0.1-25 \
intel-oneapi-ippcp=2021.9.1-5 \
intel-oneapi-ippcp-devel=2021.9.1-5 \
intel-oneapi-ipp=2021.10.1-13 \
intel-oneapi-ipp-devel=2021.10.1-13 \
intel-oneapi-tlt=2024.0.0-352 \
intel-oneapi-ccl=2021.11.2-5 \
intel-oneapi-ccl-devel=2021.11.2-5 \
intel-oneapi-dnnl-devel=2024.0.0-49521 \
intel-oneapi-dnnl=2024.0.0-49521 \
intel-oneapi-tcm-1.0=1.0.0-435
```
3. Create a Python virtual environment and activate it   
```
python3 -m venv autogen_venv   
source autogen_venv/bin/activate   
```

4. Upgrade the pip version and install autogen   
```
python -m pip install pip --upgrade   
pip install pyautogen   
```

5. Install [ipex-llm](https://github.com/intel-analytics/ipex-llm/blob/main/docs/mddocs/Quickstart/ollama_quickstart.md)   
```
pip install --pre --upgrade ipex-llm[cpp]  
```

6. Initialize Ollama  
```
init-ollama   
```
  
7. Start Ollama service   
```
export OLLAMA_NUM_GPU=999   
export ZES_ENABLE_SYSMAN=1   
source /opt/intel/oneapi/setvars.sh   
export SYCL_CACHE_PERSISTENT=1   
export SYCL_PI_LEVEL_ZERO_USE_IMMEDIATE_COMMANDLISTS=1    
./ollama serve
```

8. Open a new terminal and download the required LLMs ([Mistral-7B-v0.3](https://huggingface.co/mistralai/Mistral-7B-v0.3), [CodeLlama-7b-hf](https://huggingface.co/codellama/CodeLlama-7b-hf)) using ollama
```
./ollama run mistral:latest
./ollama run codellama:latest   
```

