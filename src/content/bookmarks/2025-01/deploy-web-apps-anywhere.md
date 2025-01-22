---
title: "Kamal：无缝部署网页应用的开源工具"
slug: deploy-web-apps-anywhere
description: |
  Kamal是一款开源工具，旨在通过Docker简化网页应用的部署过程。无论是在自己的硬件还是云端，Kamal都能实现快速、零停机时间的部署，给予用户卓越的可移植性，让开发者拥有更大的灵活性。
tags: 
  - dev
  - tool
  - docker
  - webdev
  - opensource
pubDatetime: 2025-01-22T11:07:34+08:00
ogImage: https://kamal-deploy.org/assets/images/opengraph.png
---

[原文链接](https://kamal-deploy.org/)

---

## Vision

In the past decade+, there’s been an explosion in commercial offerings that make deploying web apps easier. Heroku kicked it off with an incredible offering that stayed ahead of the competition seemingly forever. These days we have excellent alternatives like Fly.io and Render. And hosted Kubernetes is making things easier too on AWS, GCP, Digital Ocean, and elsewhere. But these are all offerings that have you renting computers in the cloud at a premium. If you want to run on your own hardware, or even just have a clear migration path to do so in the future, you need to carefully consider how locked in you get to these commercial platforms. Preferably before the bills swallow your business whole!

Kamal seeks to bring the advance in ergonomics pioneered by these commercial offerings to deploying web apps anywhere. Whether that’s low-cost cloud options without the managed-service markup from the likes of Digital Ocean, Hetzner, OVH, etc, or it’s your own colocated bare metal. To Kamal, it’s all the same. Feed the config file a list of IP addresses with vanilla Ubuntu servers that have seen no prep beyond an added SSH key, and you’ll be running in literally minutes.

This approach gives you enormous portability. You can have your web app deployed on several clouds at ease like this. Or you can buy the baseline with your own hardware, then deploy to a cloud before a big seasonal spike to get more capacity. When you’re not locked into a single provider from a tooling perspective, there are a lot of compelling options available.

Ultimately, Kamal is meant to compress the complexity of going to production using open source tooling that isn’t tied to any commercial offering. Not to zero, mind you. You’re probably still better off with a fully managed service if basic Linux or Docker is still difficult, but as soon as those concepts are familiar, you’ll be ready to go with Kamal.

***

### Why not just run Capistrano, Kubernetes or Docker Swarm?

Kamal basically is Capistrano for Containers, without the need to carefully prepare servers in advance. No need to ensure that the servers have just the right version of Ruby or other dependencies you need. That all lives in the Docker image now. You can boot a brand new Ubuntu (or whatever) server, add it to the list of servers in Kamal, and it’ll be auto-provisioned with Docker, and run right away. Docker’s layer caching also speeds up deployments with less mucking about on the server. And the images built for Kamal can be used for CI or later introspection.

Kubernetes is a beast. Running it yourself on your own hardware is not for the faint of heart. It’s a fine option if you want to run on someone else’s platform, either transparently [like Render](https://thenewstack.io/render-cloud-deployment-with-less-engineering/) or explicitly on AWS/GCP, but if you’d like the freedom to move between cloud and your own hardware, or even mix the two, Kamal is much simpler. You can see everything that’s going on, it’s just basic Docker commands being called.

Docker Swarm is much simpler than Kubernetes, but it’s still built on the same declarative model that uses state reconciliation. Kamal is intentionally designed around imperative commands, like Capistrano.

Ultimately, there are a myriad of ways to deploy web apps, but this is the toolkit we’ve used at [37signals](https://37signals.com/) to bring [HEY](https://www.hey.com/) and all our other formerly cloud-hosted applications [home to our own hardware](https://world.hey.com/dhh/we-have-left-the-cloud-251760fb) — without losing the advantages of modern containerization tooling.

***

### Name

Kamal is named after [the ancient Arab navigational tool](https://exploration.marinersmuseum.org/object/kamal/) used by sailors to keep course by determining their latitude via the Pole Star. (Kamal was formerly known as MRSK).

![A person uses a Kamal, an ancient Arab navigational tool, to measure the angle between the horizon and the Pole Star at night by the sea.](https://kamal-deploy.org/assets/images/kamal.png)


