---
title: "Sanic: 快速构建和运行高效的Web应用程序"
slug: sanic-web-framework
description: |
  Sanic 是一个用于构建高性能HTTP服务器的Python 3.9+ Web框架。它利用了Python 3.5中引入的`async/await`语法，实现非阻塞代码，提高速度。支持ASGI，易于扩展和部署。
tags: 
  - API
  - dev
  - Python
pubDatetime: 2025-03-27T11:49:16+08:00
ogImage: https://repository-images.githubusercontent.com/59720190/d803ca00-616c-11e9-86e0-d26ba19c9170
---

[原文链接](https://github.com/sanic-org/sanic)

---

[![Sanic | Build fast. Run fast.](https://raw.githubusercontent.com/sanic-org/sanic-assets/master/png/sanic-framework-logo-400x97.png)](https://raw.githubusercontent.com/sanic-org/sanic-assets/master/png/sanic-framework-logo-400x97.png)

[]()

## Sanic | Build fast. Run fast.

[](#sanic--build-fast-run-fast)

| Build   | [![Tests](https://github.com/sanic-org/sanic/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/sanic-org/sanic/actions/workflows/tests.yml)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Docs    | [![UserGuide](https://camo.githubusercontent.com/56fec7d7a786db24deafd354ccac4bb4f15f0829c5d3c6c56e7b9c40ed366144/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f7573657225323067756964652d73616e69632d666630303638)](https://sanic.dev/) [![Documentation](https://camo.githubusercontent.com/e74fbf1c25e70b89d957d84d41ee254fb4f3d6f41fd5076bccb81f67732b183a/68747470733a2f2f72656164746865646f63732e6f72672f70726f6a656374732f73616e69632f62616467652f3f76657273696f6e3d6c6174657374)](http://sanic.readthedocs.io/en/latest/?badge=latest)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Package | [![PyPI](https://camo.githubusercontent.com/0a222cca0664f793b4fe975bed7e4840f366a6294d2ab291bebe2227da96e7cc/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f73616e69632e737667) ](https://pypi.python.org/pypi/sanic/)[![PyPI version](https://camo.githubusercontent.com/1bde5fd630882f5ef6beec09599852286b07c3e9af2e839f3f156afd7d7b4d98/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f73616e69632e737667) ](https://pypi.python.org/pypi/sanic/)[![PyPI Wheel](https://camo.githubusercontent.com/0df6221770c8d012b6bb2c02b07778c11132da0272fe7d4efe2823bb9d42db0c/68747470733a2f2f696d672e736869656c64732e696f2f707970692f776865656c2f73616e69632e737667) ](https://pypi.python.org/pypi/sanic)[![Supported implementations](https://camo.githubusercontent.com/601b898e1a6fae450c06b3c57fd0a1e929c4db94f6cbed1ca1bab31cb128b75e/68747470733a2f2f696d672e736869656c64732e696f2f707970692f696d706c656d656e746174696f6e2f73616e69632e737667) ](https://pypi.python.org/pypi/sanic)[![Code style ruff](https://camo.githubusercontent.com/85813a933fe0ac2d6b96e56d1b0a2be49da820a108ed0b586abd5f53864042e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d727566662d3030303030302e737667)](https://docs.astral.sh/ruff/) |
| Support | [![Forums](https://camo.githubusercontent.com/ac720bfb49441f65d1fe6817e33e0c417d69c9524af20c1748a05e3311238490/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f666f72756d732d636f6d6d756e6974792d6666303036382e737667) ](https://community.sanicframework.org/)[![Discord](https://camo.githubusercontent.com/4e7f97ac59b3abd557e5be15ed288856714bc9b73b36114214f526e5b7fafa68/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f3831323232313138323539343132313732383f6c6f676f3d646973636f7264266c6162656c3d446973636f726426636f6c6f723d353836354632)](https://discord.gg/FARQzAEMAA) [![Awesome Sanic List](https://camo.githubusercontent.com/8693bde04030b1670d5097703441005eba34240c32d1df1eb82a5f0d6716518e/68747470733a2f2f63646e2e7261776769742e636f6d2f73696e647265736f726875732f617765736f6d652f643733303566333864323966656437386661383536353265336136336531353464643865383832392f6d656469612f62616467652e737667)](https://github.com/mekicha/awesome-sanic)                                                                                                                                                                                                                                                                                                                |
| Stats   | [![Downloads](https://camo.githubusercontent.com/b08219b0b9d4a50ec58be3125e5ffc9dbd6d445b56c96109908333838e7abdc9/68747470733a2f2f696d672e736869656c64732e696f2f707970692f646d2f73616e69632e737667) ](https://pepy.tech/project/sanic)[![Downloads](https://camo.githubusercontent.com/8493f23bdeca65636a42a9b22ce69efc87f16612fb59cc01361273b5963a7c4e/68747470733a2f2f696d672e736869656c64732e696f2f707970692f64772f73616e69632e737667) ](https://pepy.tech/project/sanic)[![Downloads](https://camo.githubusercontent.com/450ec9dff716bbf3069ba795a18207372ea063b6a1411c04ce47852bda34ee2c/68747470733a2f2f696d672e736869656c64732e696f2f636f6e64612f646e2f636f6e64612d666f7267652f73616e69632e737667)](https://anaconda.org/conda-forge/sanic)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

Sanic is a **Python 3.9+** web server and web framework that's written to go fast. It allows the usage of the `async/await` syntax added in Python 3.5, which makes your code non-blocking and speedy.

Sanic is also ASGI compliant, so you can deploy it with an [alternative ASGI webserver](https://sanicframework.org/en/guide/deployment/running.html#asgi).

[Source code on GitHub](https://github.com/sanic-org/sanic/) | [Help and discussion board](https://community.sanicframework.org/) | [User Guide](https://sanicframework.org) | [Chat on Discord](https://discord.gg/FARQzAEMAA)

The project is maintained by the community, for the community. **Contributions are welcome!**

The goal of the project is to provide a simple way to get up and running a highly performant HTTP server that is easy to build, to expand, and ultimately to scale.

[]()

### Sponsor

[](#sponsor)

Check out [open collective](https://opencollective.com/sanic-org) to learn more about helping to fund Sanic.

[]()

### Installation

[](#installation)

`pip install sanic`

> Sanic makes use of `uvloop` and `ujson` to help with performance. If you do not want to use those packages, simply add an environmental variable `SANIC_NO_UVLOOP=true` or `SANIC_NO_UJSON=true` at install time.
>
> ```
> $ export SANIC_NO_UVLOOP=true
> $ export SANIC_NO_UJSON=true
> $ pip install --no-binary :all: sanic
> ```

Note

If you are running on a clean install of Fedora 28 or above, please make sure you have the `redhat-rpm-config` package installed in case if you want to use `sanic` with `ujson` dependency.

[]()

### Hello World Example

[](#hello-world-example)

```
from sanic import Sanic
from sanic.response import json

app = Sanic("my-hello-world-app")

@app.route('/')
async def test(request):
    return json({'hello': 'world'})
```

Sanic can now be easily run from CLI using `sanic hello.app`.

```
[2018-12-30 11:37:41 +0200] [13564] [INFO] Goin' Fast @ http://127.0.0.1:8000
[2018-12-30 11:37:41 +0200] [13564] [INFO] Starting worker [13564]
```

And, we can verify it is working: `curl localhost:8000 -i`

```
HTTP/1.1 200 OK
Connection: keep-alive
Keep-Alive: 5
Content-Length: 17
Content-Type: application/json

{"hello":"world"}
```

**Now, let's go build something fast!**

Minimum Python version is 3.9.

[]()

### Documentation

[](#documentation)

User Guide, Changelog, and API Documentation can be found at [sanic.dev](https://sanic.dev).

[]()

### Questions and Discussion

[](#questions-and-discussion)

[Ask a question or join the conversation](https://community.sanicframework.org/).

[]()

### Contribution

[](#contribution)

We are always happy to have new contributions. We have [marked issues good for anyone looking to get started](https://github.com/sanic-org/sanic/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner), and welcome [questions on the forums](https://community.sanicframework.org/). Please take a look at our [Contribution guidelines](https://github.com/sanic-org/sanic/blob/master/CONTRIBUTING.rst).


