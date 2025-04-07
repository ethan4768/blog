---
title: "NodePass：一款安全、高效的TCP/UDP隧道解决方案"
slug: nodepass-secure-tunneling-solution
description: |
  NodePass是一款优秀且高效的TCP/UDP隧道解决方案，通过预先建立的TLS/TCP连接，在网络限制下提供快速、可靠的访问。它的服务器-客户端架构为开发人员和系统管理员提供了强大而易用的工具来解决复杂的网络挑战，同时兼顾安全性和性能。
tags: 
  - API
  - tool
  - network
  - security
pubDatetime: 2025-04-07T15:05:55+08:00
ogImage: https://repository-images.githubusercontent.com/905638090/a2d0e613-4be7-4f55-9d1f-30c0beafa234
---

[原文链接](https://github.com/yosebyte/nodepass)

---

# 🔗 NodePass

[](#-nodepass)

[![GitHub release](https://camo.githubusercontent.com/eaa5714c1f4c8a697df021bc4f5969e8166613f1d943b9ce6e41d5a7884dfde5/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f796f7365627974652f6e6f646570617373)](https://github.com/yosebyte/nodepass/releases) [![Go Version](https://camo.githubusercontent.com/5885e350f292c970b2585a8aa878ae786ca5732547af5b3111fa97f9b1c58eae/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f676f2d6d6f642f676f2d76657273696f6e2f796f7365627974652f6e6f646570617373)](https://golang.org/) [![Go Report Card](https://camo.githubusercontent.com/418f3a8c680751c85a0c84d8dc39a7ed76f49336e3380b5bc6064f8bc4bbede7/68747470733a2f2f676f7265706f7274636172642e636f6d2f62616467652f6769746875622e636f6d2f796f7365627974652f6e6f646570617373)](https://goreportcard.com/report/github.com/yosebyte/nodepass)

[![nodepass](https://camo.githubusercontent.com/11949cebf5f7555ef73d4ffa46e5d671c0361abb7a30aaa95830210b05859ef4/68747470733a2f2f63646e2e796f62632e64652f6173736574732f6e6f6465706173732e706e67)](https://camo.githubusercontent.com/11949cebf5f7555ef73d4ffa46e5d671c0361abb7a30aaa95830210b05859ef4/68747470733a2f2f63646e2e796f62632e64652f6173736574732f6e6f6465706173732e706e67)

**Language**: [English](https://github.com/yosebyte/nodepass/blob/main/README.md) | [简体中文](https://github.com/yosebyte/nodepass/blob/main/README_zh.md)

NodePass is an elegant, efficient TCP tunneling solution that creates secure communication bridges between network endpoints. By establishing an unencrypted TCP control channel, NodePass facilitates seamless data transfer through otherwise restricted network environments while offering configurable security options for the data channel. Its server-client architecture allows for flexible deployment scenarios, enabling access to services across firewalls, NATs, and other network barriers. With its intelligent connection pooling, minimal resource footprint, and straightforward command syntax, NodePass provides developers and system administrators with a powerful yet easy-to-use tool for solving complex networking challenges without compromising on security or performance.

## 📋 Table of Contents

[](#-table-of-contents)

* [Features](#-features)

* [Requirements](#-requirements)

* [Installation](#-installation)

  * [Option 1: Pre-built Binaries](#-option-1-pre-built-binaries)
  * [Option 2: Using Go Install](#-option-2-using-go-install)
  * [Option 3: Building from Source](#%EF%B8%8F-option-3-building-from-source)
  * [Option 4: Using Container Image](#-option-4-using-container-image)
  * [Option 5: Using Management Script](#-option-5-using-management-script)

* [Usage](#-usage)

  * [Server Mode](#%EF%B8%8F-server-mode)
  * [Client Mode](#-client-mode)

* [Configuration](#%EF%B8%8F-configuration)

  * [Log Levels](#-log-levels)
  * [Environment Variables](#-environment-variables)

* [Examples](#-examples)

  * [Basic Server Setup with TLS Options](#-basic-server-setup-with-tls-options)
  * [Connecting to a NodePass Server](#-connecting-to-a-nodepass-server)
  * [Database Access Through Firewall](#-database-access-through-firewall)
  * [Secure Microservice Communication](#-secure-microservice-communication)
  * [IoT Device Management](#-iot-device-management)
  * [Multi-environment Development](#-multi-environment-development)
  * [Container Deployment](#-container-deployment)

* [How It Works](#-how-it-works)

* [Data Transmission Flow](#-data-transmission-flow)

* [Signal Communication Mechanism](#-signal-communication-mechanism)

* [Connection Pool Architecture](#-connection-pool-architecture)

* [Common Use Cases](#-common-use-cases)

* [Troubleshooting](#-troubleshooting)

  * [Connection Issues](#-connection-issues)
  * [Performance Optimization](#-performance-optimization)

* [Contributing](#-contributing)

* [Discussion](#-discussion)

* [License](#-license)

* [Stargazers](#-stargazers)

## ✨ Features

[](#-features)

[![nodepass](https://camo.githubusercontent.com/c2f989f851a8f4aef203ac4560f8999ac62f964861b6e65de6876611be188739/68747470733a2f2f63646e2e796f62632e64652f6173736574732f6e702d636c692e706e67)](https://camo.githubusercontent.com/c2f989f851a8f4aef203ac4560f8999ac62f964861b6e65de6876611be188739/68747470733a2f2f63646e2e796f62632e64652f6173736574732f6e702d636c692e706e67)

* **🔄 Dual Operating Modes**: Run as a server to accept connections or as a client to initiate them
* **🌐 TCP/UDP Protocol Support**: Tunnels both TCP and UDP traffic for complete application compatibility
* **🔒 Flexible TLS Options**: Three security modes for data channel encryption
* **🔐 Automatic TLS Policy Adoption**: Client automatically adopts the server's TLS security policy
* **🔌 Efficient Connection Pooling**: Optimized connection management with configurable pool sizes
* **📊 Flexible Logging System**: Configurable verbosity with five distinct logging levels
* **🛡️ Resilient Error Handling**: Automatic connection recovery and graceful shutdowns
* **📦 Single-Binary Deployment**: Simple to distribute and install with minimal dependencies
* **⚙️ Zero Configuration Files**: Everything is specified via command-line arguments and environment variables
* **🚀 Low Resource Footprint**: Minimal CPU and memory usage even under heavy load
* **♻️ Automatic Reconnection**: Seamlessly recovers from network interruptions
* **🧩 Modular Architecture**: Clean separation between client, server, and common components
* **🔍 Comprehensive Debugging**: Detailed connection tracing and signal monitoring
* **⚡ High-Performance Data Exchange**: Optimized bidirectional data transfer mechanism
* **🧠 Smart Connection Management**: Intelligent handling of connection states and lifecycles
* **📈 Scalable Semaphore System**: Prevents resource exhaustion during high traffic
* **🛠️ Configurable Pool Dynamics**: Adjust connection pool behavior based on workload
* **🔌 One-Time Connection Pattern**: Enhanced security through non-reused connections
* **📡 Dynamic Port Allocation**: Automatically manages port assignments for secure communication

## 📋 Requirements

[](#-requirements)

* Go 1.24 or higher (for building from source)
* Network connectivity between server and client endpoints
* Admin privileges may be required for binding to ports below 1024

## 📥 Installation

[](#-installation)

### 💾 Option 1: Pre-built Binaries

[](#-option-1-pre-built-binaries)

Download the latest release for your platform from our [releases page](https://github.com/yosebyte/nodepass/releases).

### 🔧 Option 2: Using Go Install

[](#-option-2-using-go-install)

```
go install github.com/yosebyte/nodepass/cmd/nodepass@latest
```

### 🛠️ Option 3: Building from Source

[](#️-option-3-building-from-source)

```
# Clone the repository
git clone https://github.com/yosebyte/nodepass.git

# Build the binary
cd nodepass
go build -o nodepass ./cmd/nodepass

# Optional: Install to your GOPATH/bin
go install ./cmd/nodepass
```

### 🐳 Option 4: Using Container Image

[](#-option-4-using-container-image)

NodePass is available as a container image on GitHub Container Registry:

```
# Pull the container image
docker pull ghcr.io/yosebyte/nodepass:latest

# Run in server mode
docker run -d --name nodepass-server -p 10101:10101 -p 8080:8080 \
  ghcr.io/yosebyte/nodepass server://0.0.0.0:10101/0.0.0.0:8080

# Run in client mode
docker run -d --name nodepass-client \
  -e MIN_POOL_CAPACITY=32 \
  -e MAX_POOL_CAPACITY=512 \
  -p 8080:8080 \
  ghcr.io/yosebyte/nodepass client://nodepass-server:10101/127.0.0.1:8080
```

### 📜 Option 5: Using Management Script

[](#-option-5-using-management-script)

For Linux systems, you can use our interactive management script for easy installation and service management:

```
bash <(curl -sL https://cdn.yobc.de/shell/nodepass.sh)
```

This script provides an interactive menu to:

* Install or update NodePass
* Create and configure multiple nodepass services
* Manage (start/stop/restart/delete) nodepass services
* Set up systemd services automatically
* Configure client and server modes with customizable options

## 🚀 Usage

[](#-usage)

NodePass creates a tunnel with an unencrypted TCP control channel and configurable TLS encryption options for the data exchange channel. It operates in two complementary modes:

### 🖥️ Server Mode

[](#️-server-mode)

```
nodepass server://<tunnel_addr>/<target_addr>?log=<level>&tls=<mode>&crt=<cert_file>&key=<key_file>
```

* `tunnel_addr`: Address for the TCP tunnel endpoint (control channel) that clients will connect to (e.g., 10.1.0.1:10101)

* `target_addr`: Address where the server listens for incoming connections (TCP and UDP) that will be tunneled to clients (e.g., 10.1.0.1:8080)

* `log`: Log level (debug, info, warn, error, fatal)

* `tls`: TLS encryption mode for the target data channel (0, 1, 2)

  * `0`: No TLS encryption (plain TCP/UDP)
  * `1`: Self-signed certificate (automatically generated)
  * `2`: Custom certificate (requires `crt` and `key` parameters)

* `crt`: Path to certificate file (required when `tls=2`)

* `key`: Path to private key file (required when `tls=2`)

In server mode, NodePass:

1. Listens for TCP tunnel connections (control channel) on `tunnel_addr`
2. Listens for incoming TCP and UDP traffic on `target_addr`
3. When a connection arrives at `target_addr`, it signals the connected client through the unencrypted TCP tunnel
4. Creates a data channel for each connection with the specified TLS encryption level

Example:

```
# No TLS encryption for data channel
nodepass server://10.1.0.1:10101/10.1.0.1:8080?log=debug&tls=0

# Self-signed certificate (auto-generated)
nodepass server://10.1.0.1:10101/10.1.0.1:8080?log=debug&tls=1

# Custom domain certificate
nodepass server://10.1.0.1:10101/10.1.0.1:8080?log=debug&tls=2&crt=/path/to/cert.pem&key=/path/to/key.pem
```

### 📱 Client Mode

[](#-client-mode)

```
nodepass client://<tunnel_addr>/<target_addr>?log=<level>
```

* `tunnel_addr`: Address of the NodePass server's tunnel endpoint to connect to (e.g., 10.1.0.1:10101)
* `target_addr`: Local address where traffic will be forwarded to (e.g., 127.0.0.1:8080)
* `log`: Log level (debug, info, warn, error, fatal)

In client mode, NodePass:

1. Connects to the server's unencrypted TCP tunnel endpoint (control channel) at `tunnel_addr`
2. Listens for signals from the server through this control channel
3. When a signal is received, establishes a data connection with the TLS security level specified by the server
4. Creates a local connection to `target_addr` and forwards traffic

Example:

```
# Connect to a NodePass server and automatically adopt its TLS security policy
nodepass client://10.1.0.1:10101/127.0.0.1:8080?log=info
```

## ⚙️ Configuration

[](#️-configuration)

NodePass uses a minimalist approach with command-line parameters and environment variables:

### 📝 Log Levels

[](#-log-levels)

* `debug`: Verbose debugging information - shows all operations and connections
* `info`: General operational information (default) - shows startup, shutdown, and key events
* `warn`: Warning conditions - only shows potential issues that don't affect core functionality
* `error`: Error conditions - shows only problems that affect functionality
* `fatal`: Critical conditions - shows only severe errors that cause termination

### 🔧 Environment Variables

[](#-environment-variables)

| Variable            | Description                              | Default | Example                          |
| ------------------- | ---------------------------------------- | ------- | -------------------------------- |
| `SEMAPHORE_LIMIT`   | Maximum number of concurrent connections | 1024    | `export SEMAPHORE_LIMIT=2048`    |
| `MIN_POOL_CAPACITY` | Minimum connection pool size             | 16      | `export MIN_POOL_CAPACITY=32`    |
| `MAX_POOL_CAPACITY` | Maximum connection pool size             | 1024    | `export MAX_POOL_CAPACITY=4096`  |
| `UDP_DATA_BUF_SIZE` | Buffer size for UDP packets              | 8192    | `export UDP_DATA_BUF_SIZE=16384` |
| `UDP_READ_TIMEOUT`  | Timeout for UDP read operations          | 5s      | `export UDP_READ_TIMEOUT=10s`    |
| `REPORT_INTERVAL`   | Interval for health check reports        | 5s      | `export REPORT_INTERVAL=10s`     |
| `SERVICE_COOLDOWN`  | Cooldown period before restart attempts  | 5s      | `export SERVICE_COOLDOWN=3s`     |
| `SHUTDOWN_TIMEOUT`  | Timeout for graceful shutdown            | 5s      | `export SHUTDOWN_TIMEOUT=10s`    |

## 📚 Examples

[](#-examples)

### 🔐 Basic Server Setup with TLS Options

[](#-basic-server-setup-with-tls-options)

```
# Start a server with no TLS encryption for data channel
nodepass server://0.0.0.0:10101/127.0.0.1:8080?log=debug&tls=0

# Start a server with auto-generated self-signed certificate
nodepass server://0.0.0.0:10101/127.0.0.1:8080?log=debug&tls=1

# Start a server with custom domain certificate
nodepass server://0.0.0.0:10101/127.0.0.1:8080?log=debug&tls=2&crt=/path/to/cert.pem&key=/path/to/key.pem
```

### 🔌 Connecting to a NodePass Server

[](#-connecting-to-a-nodepass-server)

```
# Connect to a server (automatically adopts the server's TLS security policy)
nodepass client://server.example.com:10101/127.0.0.1:8080

# Connect with debug logging
nodepass client://server.example.com:10101/127.0.0.1:8080?log=debug
```

### 🗄 Database Access Through Firewall

[](#-database-access-through-firewall)

```
# Server side (outside secured network) with TLS encryption
nodepass server://:10101/127.0.0.1:5432?tls=1

# Client side (inside the firewall)
nodepass client://server.example.com:10101/127.0.0.1:5432
```

### 🔒 Secure Microservice Communication

[](#-secure-microservice-communication)

```
# Service A (providing API) with custom certificate
nodepass server://0.0.0.0:10101/127.0.0.1:8081?log=warn&tls=2&crt=/path/to/service-a.crt&key=/path/to/service-a.key

# Service B (consuming API)
nodepass client://service-a:10101/127.0.0.1:8082
```

### 📡 IoT Device Management

[](#-iot-device-management)

```
# Central management server
nodepass server://0.0.0.0:10101/127.0.0.1:8888?log=info&tls=1

# IoT device
nodepass client://mgmt.example.com:10101/127.0.0.1:80
```

### 🧪 Multi-environment Development

[](#-multi-environment-development)

```
# Production API access tunnel
nodepass client://tunnel.example.com:10101/127.0.0.1:3443

# Development environment
nodepass server://tunnel.example.com:10101/127.0.0.1:3000

# Testing environment
nodepass server://tunnel.example.com:10101/127.0.0.1:3001?log=warn&tls=1
```

### 🐳 Container Deployment

[](#-container-deployment)

```
# Create a network for the containers
docker network create nodepass-net

# Deploy NodePass server with self-signed certificate
docker run -d --name nodepass-server \
  --network nodepass-net \
  -p 10101:10101 \
  ghcr.io/yosebyte/nodepass server://0.0.0.0:10101/web-service:80?log=info&tls=1

# Deploy a web service as target
docker run -d --name web-service \
  --network nodepass-net \
  nginx:alpine

# Deploy NodePass client
docker run -d --name nodepass-client \
  -p 8080:8080 \
  ghcr.io/yosebyte/nodepass client://nodepass-server:10101/127.0.0.1:8080?log=info

# Access the web service via http://localhost:8080
```

## 🔍 How It Works

[](#-how-it-works)

NodePass creates a network architecture with separate channels for control and data:

1. **Control Channel (Tunnel)**:

   * Unencrypted TCP connection between client and server
   * Used exclusively for signaling and coordination
   * Maintains persistent connection for the lifetime of the tunnel

2. **Data Channel (Target)**:

   * Configurable TLS encryption options:

     * **Mode 0**: Unencrypted data transfer (fastest, least secure)
     * **Mode 1**: Self-signed certificate encryption (good security, no verification)
     * **Mode 2**: Verified certificate encryption (highest security, requires valid certificates)

   * Created on-demand for each connection or datagram

   * Used for actual application data transfer

3. **Server Mode Operation**:

   * Listens for control connections on the tunnel endpoint
   * When traffic arrives at the target endpoint, signals the client via the control channel
   * Establishes data channels with the specified TLS mode when needed

4. **Client Mode Operation**:

   * Connects to the server's control channel
   * Listens for signals indicating incoming connections
   * Creates data connections using the TLS security level specified by the server
   * Forwards data between the secure channel and local target

5. **Protocol Support**:

   * **TCP**: Full bidirectional streaming with persistent connections
   * **UDP**: Datagram forwarding with configurable buffer sizes and timeouts

## 🔄 Data Transmission Flow

[](#-data-transmission-flow)

NodePass establishes a bidirectional data flow through its tunnel architecture, supporting both TCP and UDP protocols:

### Server-Side Flow

[](#server-side-flow)

1. **Connection Initiation**:

   ```
   [Target Client] → [Target Listener] → [Server: Target Connection Created]
   ```

   * For TCP: Client establishes persistent connection to target listener
   * For UDP: Server receives datagrams on UDP socket bound to target address

2. **Signal Generation**:

   ```
   [Server] → [Generate Unique Connection ID] → [Signal Client via Unencrypted TCP Tunnel]
   ```

   * For TCP: Generates a `//<connection_id>#1` signal
   * For UDP: Generates a `//<connection_id>#2` signal when datagram is received

3. **Connection Preparation**:

   ```
   [Server] → [Create Remote Connection in Pool with Configured TLS Mode] → [Wait for Client Connection]
   ```

   * Both protocols use the same connection pool mechanism with unique connection IDs
   * TLS configuration applied based on the specified mode (0, 1, or 2)

4. **Data Exchange**:

   ```
   [Target Connection] ⟷ [Exchange/Transfer] ⟷ [Remote Connection]
   ```

   * For TCP: Uses `conn.DataExchange()` for continuous bidirectional data streaming
   * For UDP: Individual datagrams are forwarded with configurable buffer sizes

### Client-Side Flow

[](#client-side-flow)

1. **Signal Reception**:

   ```
   [Client] → [Read Signal from TCP Tunnel] → [Parse Connection ID]
   ```

   * Client differentiates between TCP and UDP signals based on URL scheme

2. **Connection Establishment**:

   ```
   [Client] → [Retrieve Connection from Pool] → [Connect to Remote Endpoint]
   ```

   * Connection management is protocol-agnostic at this stage

3. **Local Connection**:

   ```
   [Client] → [Connect to Local Target] → [Establish Local Connection]
   ```

   * For TCP: Establishes persistent TCP connection to local target
   * For UDP: Creates UDP socket for datagram exchange with local target

4. **Data Exchange**:

   ```
   [Remote Connection] ⟷ [Exchange/Transfer] ⟷ [Local Target Connection]
   ```

   * For TCP: Uses `conn.DataExchange()` for continuous bidirectional data streaming
   * For UDP: Reads single datagram, forwards it, waits for response with timeout, then returns response

### Protocol-Specific Characteristics

[](#protocol-specific-characteristics)

* **TCP Exchange**:

  * Persistent connections for full-duplex communication
  * Continuous data streaming until connection termination
  * Error handling with automatic reconnection

* **UDP Exchange**:

  * One-time datagram forwarding with configurable buffer sizes (`UDP_DATA_BUF_SIZE`)
  * Read timeout control for response waiting (`UDP_READ_TIMEOUT`)
  * Optimized for low-latency, stateless communications

Both protocols benefit from the same secure signaling mechanism through the TCP tunnel, ensuring protocol-agnostic control flow with protocol-specific data handling.

## 📡 Signal Communication Mechanism

[](#-signal-communication-mechanism)

NodePass uses a sophisticated URL-based signaling protocol through the TCP tunnel:

### Signal Types

[](#signal-types)

1. **Tunnel Signal**:

   * Format: `//<port>#<tls>`
   * Purpose: Informs the client about the server's remote endpoint port and tls code
   * Timing: Sent on tunnel handshake

2. **TCP Launch Signal**:

   * Format: `//<connection_id>#1`
   * Purpose: Requests the client to establish a TCP connection for a specific ID
   * Timing: Sent when a new TCP connection to the target service is received

3. **UDP Launch Signal**:

   * Format: `//<connection_id>#2`
   * Purpose: Requests the client to handle UDP traffic for a specific ID
   * Timing: Sent when UDP data is received on the target port

### Signal Flow

[](#signal-flow)

1. **Signal Generation**:

   * Server creates URL-formatted signals for specific events
   * Signal is terminated with a newline character for proper parsing

2. **Signal Transmission**:

   * Server writes signals to the TCP tunnel connection
   * Uses a mutex to prevent concurrent writes to the tunnel

3. **Signal Reception**:

   * Client uses a buffered reader to read signals from the tunnel
   * Signals are trimmed and parsed into URL format

4. **Signal Processing**:

   * Client places valid signals in a buffered channel (signalChan)
   * A dedicated goroutine processes signals from the channel
   * Semaphore pattern prevents signal overflow

5. **Signal Execution**:

   * Remote signals update the client's remote address configuration
   * Launch signals trigger the `clientOnce()` method to establish connections

### Signal Resilience

[](#signal-resilience)

* Buffered channel with configurable capacity prevents signal loss during high load
* Semaphore implementation ensures controlled concurrency
* Error handling for malformed or unexpected signals

## 🔌 Connection Pool Architecture

[](#-connection-pool-architecture)

NodePass implements an efficient connection pooling system for managing network connections:

### Pool Design

[](#pool-design)

1. **Pool Types**:

   * **Client Pool**: Pre-establishes connections to the remote endpoint
   * **Server Pool**: Manages incoming connections from clients

2. **Pool Components**:

   * **Connection Storage**: Thread-safe map of connection IDs to net.Conn objects
   * **ID Channel**: Buffered channel for available connection IDs
   * **Capacity Management**: Dynamic adjustment based on usage patterns
   * **Connection Factory**: Customizable connection creation function

### Connection Lifecycle

[](#connection-lifecycle)

1. **Connection Creation**:

   * Connections are created up to the configured capacity
   * Each connection is assigned a unique ID
   * IDs and connections are stored in the pool

2. **Connection Acquisition**:

   * Client retrieves connections using connection IDs
   * Server retrieves the next available connection from the pool
   * Connections are validated before being returned

3. **Connection Usage**:

   * Connection is removed from the pool when acquired
   * Used for data exchange between endpoints
   * No connection reuse (one-time use model)

4. **Connection Termination**:

   * Connections are closed after use
   * Resources are properly released
   * Error handling ensures clean termination

### Pool Management

[](#pool-management)

1. **Capacity Control**:

   * `MIN_POOL_CAPACITY`: Ensures minimum available connections
   * `MAX_POOL_CAPACITY`: Prevents excessive resource consumption
   * Dynamic scaling based on demand patterns

2. **Pool Managers**:

   * `ClientManager()`: Maintains the client connection pool
   * `ServerManager()`: Manages the server connection pool

3. **One-Time Connection Pattern**: Each connection in the pool follows a one-time use pattern:

   * Created and placed in the pool
   * Retrieved once for a specific data exchange
   * Never returned to the pool (prevents potential data leakage)
   * Properly closed after use

4. **Automatic Pool Size Adjustment**:

   * Pool capacity dynamically adjusts based on real-time usage patterns
   * If connection creation success rate is low (<20%), capacity decreases to minimize resource waste
   * If connection creation success rate is high (>80%), capacity increases to accommodate higher traffic
   * Gradual scaling prevents oscillation and provides stability
   * Respects configured minimum and maximum capacity boundaries
   * Scales down during periods of low activity to conserve resources
   * Scales up proactively when traffic increases to maintain performance
   * Self-tuning algorithm that adapts to varying network conditions
   * Separate adjustment logic for client and server pools to optimize for different traffic patterns

5. **Efficiency Considerations**:

   * Pre-establishment reduces connection latency
   * Connection validation ensures only healthy connections are used
   * Proper resource cleanup prevents connection leaks
   * Interval-based pool maintenance balances resource usage with responsiveness
   * Optimized connection validation with minimal overhead

## 💡 Common Use Cases

[](#-common-use-cases)

* **🚪 Remote Access**: Access services on private networks from external locations without VPN infrastructure. Ideal for accessing development servers, internal tools, or monitoring systems from remote work environments.

* **🧱 Firewall Bypass**: Navigate through restrictive network environments by establishing tunnels that use commonly allowed ports (like 443). Perfect for corporate environments with strict outbound connection policies or public Wi-Fi networks with limited connectivity.

* **🏛️ Legacy System Integration**: Connect modern applications to legacy systems securely without modifying the legacy infrastructure. Enables gradual modernization strategies by providing secure bridges between old and new application components.

* **🔒 Secure Microservice Communication**: Establish encrypted channels between distributed components across different networks or data centers. Allows microservices to communicate securely even across public networks without implementing complex service mesh solutions.

* **📱 Remote Development**: Connect to development resources from anywhere, enabling seamless coding, testing, and debugging against internal development environments regardless of developer location. Supports modern distributed team workflows and remote work arrangements.

* **☁️ Cloud-to-On-Premise Connectivity**: Link cloud services with on-premise infrastructure without exposing internal systems directly to the internet. Creates secure bridges for hybrid cloud architectures that require protected communication channels between environments.

* **🌍 Geographic Distribution**: Access region-specific services from different locations, overcoming geographic restrictions or testing region-specific functionality. Useful for global applications that need to operate consistently across different markets.

* **🧪 Testing Environments**: Create secure connections to isolated testing environments without compromising their isolation. Enables QA teams to access test systems securely while maintaining the integrity of test data and configurations.

* **🔄 API Gateway Alternative**: Serve as a lightweight alternative to full API gateways for specific services. Provides secure access to internal APIs without the complexity and overhead of comprehensive API management solutions.

* **🔒 Database Protection**: Enable secure database access while keeping database servers completely isolated from direct internet exposure. Creates a secure middle layer that protects valuable data assets from direct network attacks.

* **🌐 Cross-Network IoT Communication**: Facilitate communication between IoT devices deployed across different network segments. Overcomes NAT, firewall, and routing challenges common in IoT deployments spanning multiple locations.

* **🛠️ DevOps Pipeline Integration**: Connect CI/CD pipelines securely to deployment targets in various environments. Ensures build and deployment systems can securely reach production, staging, and testing environments without compromising network security.

## 🔧 Troubleshooting

[](#-troubleshooting)

### 📜 Connection Issues

[](#-connection-issues)

* Verify firewall settings allow both TCP and UDP traffic on the specified ports
* Check that the tunnel address is correctly specified in client mode
* Ensure TLS certificates are properly generated
* Increase log level to debug for more detailed connection information
* Verify network stability between client and server endpoints
* For UDP tunneling issues, check if your application requires specific UDP packet size configurations
* For high-volume UDP applications, consider increasing the UDP\_DATA\_BUF\_SIZE
* If UDP packets seem to be lost, try adjusting the UDP\_READ\_TIMEOUT value
* Check for NAT traversal issues if operating across different networks
* Inspect system resource limits (file descriptors, etc.) if experiencing connection failures under load
* Verify DNS resolution if using hostnames for tunnel or target addresses

### 🚀 Performance Optimization

[](#-performance-optimization)

#### Connection Pool Tuning

[](#connection-pool-tuning)

* Adjust `MIN_POOL_CAPACITY` based on your minimum expected concurrent connections

  * Too low: Increased latency during traffic spikes as new connections must be established
  * Too high: Wasted resources maintaining idle connections
  * Recommended starting point: 25-50% of your average concurrent connections

* Configure `MAX_POOL_CAPACITY` to handle peak loads while preventing resource exhaustion

  * Too low: Connection failures during traffic spikes
  * Too high: Potential resource exhaustion affecting system stability
  * Recommended starting point: 150-200% of your peak concurrent connections

* Set `SEMAPHORE_LIMIT` based on expected peak concurrent tunneled sessions

  * Too low: Rejected connections during traffic spikes
  * Too high: Potential memory pressure from too many concurrent goroutines
  * Recommended range: 1000-5000 for most applications, higher for high-throughput scenarios

#### Network Configuration

[](#network-configuration)

* Optimize TCP settings on both client and server:

  * Adjust TCP keepalive intervals for long-lived connections
  * Consider TCP buffer sizes for high-throughput applications
  * Enable TCP BBR congestion control algorithm if available

#### Resource Allocation

[](#resource-allocation)

* Ensure sufficient system resources on both client and server:

  * Monitor CPU usage during peak loads
  * Track memory consumption for connection management
  * Verify sufficient network bandwidth between endpoints

#### Monitoring Recommendations

[](#monitoring-recommendations)

* Implement connection tracking to identify bottlenecks
* Monitor connection establishment success rates
* Track data transfer rates to identify throughput issues
* Measure connection latency to optimize user experience

#### Advanced Scenarios

[](#advanced-scenarios)

* For high-throughput applications:

  ```
  export MIN_POOL_CAPACITY=64
  export MAX_POOL_CAPACITY=4096
  export SEMAPHORE_LIMIT=8192
  export REPORT_INTERVAL=2s
  ```

* For low-latency applications:

  ```
  export MIN_POOL_CAPACITY=32
  export MAX_POOL_CAPACITY=1024
  export SEMAPHORE_LIMIT=2048
  export REPORT_INTERVAL=1s
  ```

* For resource-constrained environments:

  ```
  export MIN_POOL_CAPACITY=8
  export MAX_POOL_CAPACITY=256
  export SEMAPHORE_LIMIT=512
  export REPORT_INTERVAL=10s
  ```

## 👥 Contributing

[](#-contributing)

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 💬 Discussion

[](#-discussion)

Thank you to all the developers and users in the [NodeSeek](https://www.nodeseek.com/post-295115-1) community for your feedbacks. Feel free to reach out anytime with any technical issues.

## 📄 License

[](#-license)

This project is licensed under the MIT License - see the [LICENSE](https://github.com/yosebyte/nodepass/blob/main/LICENSE) file for details.

## ⭐ Stargazers

[](#-stargazers)

[![Stargazers over time](https://camo.githubusercontent.com/5192631d3fe201687088f0da2315248ffbf6410e31797e8060753f2886ebfec8/68747470733a2f2f7374617263686172742e63632f796f7365627974652f6e6f6465706173732e7376673f76617269616e743d6164617074697665)](https://starchart.cc/yosebyte/nodepass)


