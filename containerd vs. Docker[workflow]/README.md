# 🐳 How Docker, containerd, and Kubernetes Work Together

This document explains the internal architecture and flow between Docker, containerd, runc, and Kubernetes.

---
`
## What’s a container?
Before diving into what containerd is, I should briefly review what containers are. Simply put, containers are processes with added isolation and resource management. Containers have their own virtualized operating system with access to host system resources. 

Containers also use operating system kernel features. They use namespaces to provide isolation and cgroups to limit and monitor resources like CPU, memory, and network bandwidth. As you can imagine, container internals are complex, and not everyone has the time or energy to become an expert in the low-level bits. This is where container runtimes, like containerd, can help.

What’s containerd?
In short, containerd is a runtime built to run containers. This open source tool builds on top of operating system kernel features and improves container management with an abstraction layer, which manages namespaces, cgroups, union file systems, networking capabilities, and more. This way, developers don’t have to handle the complexities directly. 

In March 2017, Docker pulled its core container runtime into a standalone project called containerd and donated it to the Cloud Native Computing Foundation (CNCF).  By February 2019, containerd had reached the Graduated maturity level within the CNCF, representing its significant development, adoption, and community support. Today, developers recognize containerd as an industry-standard container runtime known for its scalability, performance, and stability.

Containerd is a high-level container runtime with many use cases. It’s perfect for handling container workloads across small-scale deployments, but it’s also well-suited for large, enterprise-level environments (including Kubernetes). 

A key component of containerd’s robustness is its default use of Open Container Initiative (OCI)-compliant runtimes. By using runtimes such as runc (a lower-level container runtime), containerd ensures standardization and interoperability in containerized environments. It also efficiently deals with core operations in the container life cycle, including creating, starting, and stopping containers.

`

## 🔧 Overview of Components

| Component     | Role                                                                 |
|---------------|----------------------------------------------------------------------|
| **Docker CLI** | Command-line interface to build, run, and manage containers         |
| **Docker Engine** | Main service that manages images, networking, volumes, etc.     |
| **containerd** | A lightweight container runtime used by Docker and Kubernetes      |
| **runc**       | Low-level runtime that creates and starts containers using Linux kernel features |
| **Kubernetes** | Container orchestration tool that manages containerized applications |
| **Linux Kernel** | Provides namespaces, cgroups, and other features for container isolation |

---

## 📦 Docker Internals

When you run a Docker command like:

```bash
docker run nginx
```
```
[ Docker CLI ]
      ↓
[ Docker Engine ]
      ↓
[ containerd ]
      ↓
[ runc ]
      ↓
[ Linux Kernel (namespaces, cgroups) ]
      ↓
[ Container (nginx) ]
- Docker CLI talks to the Docker Engine.

- Docker Engine delegates container lifecycle to containerd.

- containerd uses runc to create and run containers.

- runc uses Linux kernel features to isolate and manage resources.
```
```
☸️ Kubernetes + containerd (No Docker)
When using Kubernetes (v1.24+), Docker is not used at all. Kubernetes talks directly to containerd.

scss

[ Kubernetes (kubelet) ]
      ↓ (CRI)
[ containerd ]
      ↓
[ runc ]
      ↓
[ Linux Kernel ] (namespaces, cgroups, etc.)
      ↓
[ Container ]

- Kubernetes uses CRI (Container Runtime Interface) to communicate with containerd.

- containerd pulls the image and runs the container using runc.

- This approach is more lightweight and efficient.


Cloud	Runtime Used by Kubernetes
Google GKE	containerd
AWS EKS	containerd
Azure AKS	containerd (previously Moby)
Minikube	containerd, CRI-O, or Docker (you choose)
```
```
 What is runc?
runc is a lightweight, low-level CLI tool that actually creates and runs containers using Linux kernel features. (Written In	Go)

It’s the container runtime that talks directly to the Linux kernel to isolate and start containers.

🔍 In simple terms:
If Docker or Kubernetes are like "container managers", then:

containerd is like the container "supervisor".

runc is the worker that actually builds the container jail. 🛠️

📦 What does runc do?
It uses Linux kernel features like:

1.Namespaces → To isolate the container (network, PID, mount, etc.)

2.cgroups → To control how much CPU or memory a container can use

3.chroot and mount → To create the container filesystem

```

https://www.docker.com/blog/containerd-vs-docker/