# **Technical Requirements for Playground Host System**

**Purpose:** The host system must be capable of building and executing a Singularity container that includes tools for geospatial analysis, semantic web development, RDF processing, and data science tasks. This includes downloading and running large Java and Python-based software stacks like Apache Jena Fuseki, JupyterLab, and Firefox.

---

## 1. **Supported Host Platforms**

| Operating System  | Support Status      | Notes                                                                              |
| ----------------- | ------------------- | ---------------------------------------------------------------------------------- |
| **Linux**         | ✅ Fully Supported  | Native Singularity support                                                         |
| **macOS**         | ⚠️ Indirect Support | Requires a Linux VM or remote Linux system (Singularity is not natively supported) |
| **Windows 10/11** | ⚠️ Indirect Support | Requires WSL2 (Windows Subsystem for Linux) or Linux VM                            |

> **Note:** [Singularity](https://docs.sylabs.io/guides/latest/admin-guide/installation.html) is a Linux-native container platform. macOS and Windows users must use:

- A Linux Virtual Machine (e.g., Ubuntu via VirtualBox, VMware, or Parallels)
- [WSL2](https://documentation.ubuntu.com/wsl/en/latest/howto/install-ubuntu-wsl2/) with a Linux distribution (Windows only)
- Remote Linux access (e.g., via SSH)

---

## 2. **Minimum Hardware Requirements**

| Component      | Minimum       | Recommended                                          |
| -------------- | ------------- | ---------------------------------------------------- |
| **CPU**        | 2-core x86_64 | 4-core x86_64                                        |
| **RAM**        | 4 GB          | 8 GB or more                                         |
| **Disk Space** | 3 GB free     | 10+ GB (to account for container image and datasets) |

---

## 3. **Software Requirements by Platform**

### A. **Linux (Native)**

| Requirement     | Description                         |
| --------------- | ----------------------------------- |
| **Kernel**      | v4.18 or newer                      |
| **[Singularity](https://docs.sylabs.io/guides/latest/admin-guide/installation.html)** | v3.7 or newer                       |
| **sudo access** | Required to build `.sif` containers |
| **Tools**       | `wget`, `curl`, `bash`, `tar`       |

### B. **macOS**

| Requirement         | Description                          |
| ------------------- | ------------------------------------ |
| **VM software**     | e.g., VirtualBox, VMware, Parallels  |
| **Linux guest OS**  | Ubuntu 20.04+ or similar             |
| **Terminal access** | Required to run and manage container |

### C. **Windows 10/11**

| Requirement  | Description                                |
| ------------ | ------------------------------------------ |
| **[WSL2](https://documentation.ubuntu.com/wsl/en/latest/howto/install-ubuntu-wsl2/)**     | Required (with Ubuntu or Debian installed) |
| **Optional** | Alternatively, use a full Linux VM         |

---

## 4. **Network Requirements**

| Requirement               | Description                                                                  |
| ------------------------- | ---------------------------------------------------------------------------- |
| **Internet Access**       | Required for downloading base image, packages, and dependencies during build |
| **Estimated Data Usage**  | ~1.5–2.5 GB during initial container build                                   |
| **Recommended Bandwidth** | 10 Mbps or higher for smooth and timely downloads                            |

> If you will be building frequently or distributing regularly, consider caching container layers or using prebuilt `.sif` files to reduce repeated downloads.

---

## 5. **User Permissions**

| Task                | Requirement                                        |
| ------------------- | -------------------------------------------------- |
| **Build container** | Root access (`sudo`) or rootless Singularity setup |
| **Run container**   | Standard user privileges                           |

---
