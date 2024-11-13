# MLPeta
This is a  HPC Machine learning Challenge/Experiment for Parallel & Distributed Vectorization/Embedding 1 Petabyte of raw data from Storage into VectorDB.

### Allowed Resources
Allowed resources are 
1. OnPrem=Ubuntu with 10 x NVIDIA A100
2. GCP a2-ultragpu-8g/g2-standard-96/nvidia-tesla-v100 https://cloud.google.com/compute/docs/gpus#a100-gpus
3. AWS  EKS/EC2 P4/G4/G4ad https://aws.amazon.com/blogs/aws/now-available-ec2-instances-g4-with-nvidia-t4-tensor-core-gpus/

### Suggested Tools

1. Kubernetes (Auto Scaled Pods&Nodes)
2. Ray
3. Slurm ( https://github.com/SchedMD/slurm )
3. Python
4. Tensorflow

### For K8s
Slurm Helm Chart 
https://github.com/stackhpc/slurm-k8s-cluster/tree/main/slurm-cluster-chart
https://github.com/SchedMD/slurm

### General Suggestions
Use Python decorators 
Use MultiThreading
Use asyncio 

### The Flow
1. Read Storage (./storage/read.py)
2. Train
3. Store


### DrawIO
- Available draw-io diagram base for your use


### Resources

https://medium.com/@55_learning/integrate-slurm-with-kubernetes-2637d9250fdd

### Inspiration 

https://www.storagereview.com/news/storagereview-lab-breaks-pi-calculation-world-record-with-over-202-trillion-digits

### Solution
