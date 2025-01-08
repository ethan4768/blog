---
title: "Rclone: 高效同步文件至云存储的命令行工具"
slug: rclone-cloud-file-sync
description: |
  Rclone 是一个强大的命令行程序，可帮助用户将文件同步至各大云存储服务。支持超过70种云存储提供商，具备文件备份、恢复、镜像、迁移等多种强大功能。Rclone 还能实现加密，保证文件安全，并能与多种存储服务无缝对接。
tags: 
  - AI
  - dev
  - tool
  - opensource
pubDatetime: 2025-01-08T20:13:25+08:00
ogImage: 
---

[原文链接](https://rclone.org/)

---

![rclone logo](https://rclone.org/img/logo_on_light__horizontal_color.svg)

* [About rclone](#about)
* [What can rclone do for you?](#what)
* [What features does rclone have?](#features)
* [What providers does rclone support?](#providers)
* [Download](https://rclone.org/downloads/)
* [Install](https://rclone.org/install/)

## [**](#about)About rclone

Rclone is a command-line program to manage files on cloud storage. It is a feature-rich alternative to cloud vendors' web storage interfaces. [Over 70 cloud storage products](#providers) support rclone including S3 object stores, business & consumer file storage services, as well as standard transfer protocols.

Rclone has powerful cloud equivalents to the unix commands rsync, cp, mv, mount, ls, ncdu, tree, rm, and cat. Rclone's familiar syntax includes shell pipeline support, and `--dry-run` protection. It is used at the command line, in scripts or via its [API](https://rclone.org/rc).

Users call rclone *"The Swiss army knife of cloud storage"*, and *"Technology indistinguishable from magic"*.

Rclone really looks after your data. It preserves timestamps and verifies checksums at all times. Transfers over limited bandwidth; intermittent connections, or subject to quota can be restarted, from the last good file transferred. You can [check](https://rclone.org/commands/rclone_check/) the integrity of your files. Where possible, rclone employs server-side transfers to minimise local bandwidth use and transfers from one provider to another without using local disk.

Virtual backends wrap local and cloud file systems to apply [encryption](https://rclone.org/crypt/), [compression](https://rclone.org/compress/), [chunking](https://rclone.org/chunker/), [hashing](https://rclone.org/hasher/) and [joining](https://rclone.org/union/).

Rclone [mounts](https://rclone.org/commands/rclone_mount/) any local, cloud or virtual filesystem as a disk on Windows, macOS, linux and FreeBSD, and also serves these over [SFTP](https://rclone.org/commands/rclone_serve_sftp/), [HTTP](https://rclone.org/commands/rclone_serve_http/), [WebDAV](https://rclone.org/commands/rclone_serve_webdav/), [FTP](https://rclone.org/commands/rclone_serve_ftp/) and [DLNA](https://rclone.org/commands/rclone_serve_dlna/).

Rclone is mature, open-source software originally inspired by rsync and written in [Go](https://golang.org/). The friendly support community is familiar with varied use cases. Official Ubuntu, Debian, Fedora, Brew and Chocolatey repos. include rclone. For the latest version [downloading from rclone.org](https://rclone.org/downloads/) is recommended.

Rclone is widely used on Linux, Windows and Mac. Third-party developers create innovative backup, restore, GUI and business process solutions using the rclone command line or API.

Rclone does the heavy lifting of communicating with cloud storage.

## [**](#what)What can rclone do for you?

Rclone helps you:

* Backup (and encrypt) files to cloud storage
* Restore (and decrypt) files from cloud storage
* Mirror cloud data to other cloud services or locally
* Migrate data to the cloud, or between cloud storage vendors
* Mount multiple, encrypted, cached or diverse cloud storage as a disk
* Analyse and account for data held on cloud storage using [lsf](https://rclone.org/commands/rclone_lsf/), [ljson](https://rclone.org/commands/rclone_lsjson/), [size](https://rclone.org/commands/rclone_size/), [ncdu](https://rclone.org/commands/rclone_ncdu/)
* [Union](https://rclone.org/union/) file systems together to present multiple local and/or cloud file systems as one

## [**](#features)Features

* Transfers

  * MD5, SHA1 hashes are checked at all times for file integrity
  * Timestamps are preserved on files
  * Operations can be restarted at any time
  * Can be to and from network, e.g. two different cloud providers
  * Can use multi-threaded downloads to local disk

* [Copy](https://rclone.org/commands/rclone_copy/) new or changed files to cloud storage

* [Sync](https://rclone.org/commands/rclone_sync/) (one way) to make a directory identical

* [Bisync](https://rclone.org/bisync/) (two way) to keep two directories in sync bidirectionally

* [Move](https://rclone.org/commands/rclone_move/) files to cloud storage deleting the local after verification

* [Check](https://rclone.org/commands/rclone_check/) hashes and for missing/extra files

* [Mount](https://rclone.org/commands/rclone_mount/) your cloud storage as a network disk

* [Serve](https://rclone.org/commands/rclone_serve/) local or remote files over [HTTP](https://rclone.org/commands/rclone_serve_http/)/[WebDav](https://rclone.org/commands/rclone_serve_webdav/)/[FTP](https://rclone.org/commands/rclone_serve_ftp/)/[SFTP](https://rclone.org/commands/rclone_serve_sftp/)/[DLNA](https://rclone.org/commands/rclone_serve_dlna/)

* Experimental [Web based GUI](https://rclone.org/gui/)

## [**](#providers)Supported providers

(There are many others, built on standard protocols such as WebDAV or S3, that work out of the box.)

* 1Fichier [Home](https://1fichier.com/) [Config](https://rclone.org/fichier/)
* Akamai Netstorage [Home](https://www.akamai.com/us/en/products/media-delivery/netstorage.jsp) [Config](https://rclone.org/netstorage/)
* Alibaba Cloud (Aliyun) Object Storage System (OSS) [Home](https://www.alibabacloud.com/product/oss/) [Config](https://rclone.org/s3/#alibaba-oss)
* Amazon S3 [Home](https://aws.amazon.com/s3/) [Config](https://rclone.org/s3/)
* Backblaze B2 [Home](https://www.backblaze.com/cloud-storage) [Config](https://rclone.org/b2/)
* Box [Home](https://www.box.com/) [Config](https://rclone.org/box/)
* Ceph [Home](http://ceph.com/) [Config](https://rclone.org/s3/#ceph)
* China Mobile Ecloud Elastic Object Storage (EOS) [Home](https://ecloud.10086.cn/home/product-introduction/eos/) [Config](https://rclone.org/s3/#china-mobile-ecloud-eos)
* Arvan Cloud Object Storage (AOS) [Home](https://www.arvancloud.ir/en/products/cloud-storage) [Config](https://rclone.org/s3/#arvan-cloud-object-storage-aos)
* Citrix ShareFile [Home](http://sharefile.com/) [Config](https://rclone.org/sharefile/)
* Cloudflare R2 [Home](https://blog.cloudflare.com/r2-open-beta/) [Config](https://rclone.org/s3/#cloudflare-r2)
* DigitalOcean Spaces [Home](https://www.digitalocean.com/products/object-storage/) [Config](https://rclone.org/s3/#digitalocean-spaces)
* Digi Storage [Home](https://storage.rcs-rds.ro/) [Config](https://rclone.org/koofr/#digi-storage)
* Dreamhost [Home](https://www.dreamhost.com/cloud/storage/) [Config](https://rclone.org/s3/#dreamhost)
* Dropbox [Home](https://www.dropbox.com/) [Config](https://rclone.org/dropbox/)
* Enterprise File Fabric [Home](https://storagemadeeasy.com/about/) [Config](https://rclone.org/filefabric/)
* Fastmail Files [Home](https://www.fastmail.com/) [Config](https://rclone.org/webdav/#fastmail-files)
* Files.com [Home](https://www.files.com/) [Config](https://rclone.org/filescom/)
* FTP [Home](https://en.wikipedia.org/wiki/File_Transfer_Protocol) [Config](https://rclone.org/ftp/)
* Gofile [Home](https://gofile.io/) [Config](https://rclone.org/gofile/)
* Google Cloud Storage [Home](https://cloud.google.com/storage/) [Config](https://rclone.org/googlecloudstorage/)
* Google Drive [Home](https://www.google.com/drive/) [Config](https://rclone.org/drive/)
* Google Photos [Home](https://www.google.com/photos/about/) [Config](https://rclone.org/googlephotos/)
* HDFS [Home](https://hadoop.apache.org/) [Config](https://rclone.org/hdfs/)
* Hetzner Storage Box [Home](https://www.hetzner.com/storage/storage-box) [Config](https://rclone.org/sftp/#hetzner-storage-box)
* HiDrive [Home](https://www.strato.de/cloud-speicher/) [Config](https://rclone.org/hidrive/)
* HTTP [Home](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) [Config](https://rclone.org/http/)
* ImageKit [Home](https://imagekit.io/) [Config](https://rclone.org/imagekit/)
* Internet Archive [Home](https://archive.org/) [Config](https://rclone.org/internetarchive/)
* Jottacloud [Home](https://www.jottacloud.com/en/) [Config](https://rclone.org/jottacloud/)
* IBM COS S3 [Home](http://www.ibm.com/cloud/object-storage) [Config](https://rclone.org/s3/#ibm-cos-s3)
* IDrive e2 [Home](https://www.idrive.com/e2/?refer=rclone) [Config](https://rclone.org/s3/#idrive-e2)
* IONOS Cloud [Home](https://cloud.ionos.com/storage/object-storage) [Config](https://rclone.org/s3/#ionos)
* Koofr [Home](https://koofr.eu/) [Config](https://rclone.org/koofr/)
* Leviia Object Storage [Home](https://www.leviia.com/object-storage) [Config](https://rclone.org/s3/#leviia)
* Liara Object Storage [Home](https://liara.ir/landing/object-storage) [Config](https://rclone.org/s3/#liara-object-storage)
* Linkbox [Home](https://linkbox.to/) [Config](https://rclone.org/linkbox/)
* Linode Object Storage [Home](https://www.linode.com/products/object-storage/) [Config](https://rclone.org/s3/#linode)
* Magalu [Home](https://magalu.cloud/object-storage/) [Config](https://rclone.org/s3/#magalu)
* Mail.ru Cloud [Home](https://cloud.mail.ru/) [Config](https://rclone.org/mailru/)
* Memset Memstore [Home](https://www.memset.com/cloud/storage/) [Config](https://rclone.org/swift/)
* Mega [Home](https://mega.nz/) [Config](https://rclone.org/mega/)
* Memory [Home](https://rclone.org/memory/) [Config](https://rclone.org/memory/)
* Microsoft Azure Blob Storage [Home](https://azure.microsoft.com/en-us/services/storage/blobs/) [Config](https://rclone.org/azureblob/)
* Microsoft Azure Files Storage [Home](https://azure.microsoft.com/en-us/services/storage/files/) [Config](https://rclone.org/azurefiles/)
* Microsoft OneDrive [Home](https://onedrive.live.com/) [Config](https://rclone.org/onedrive/)
* Minio [Home](https://www.minio.io/) [Config](https://rclone.org/s3/#minio)
* Nextcloud [Home](https://nextcloud.com/) [Config](https://rclone.org/webdav/#nextcloud)
* OVH [Home](https://www.ovh.co.uk/public-cloud/storage/object-storage/) [Config](https://rclone.org/swift/)
* Blomp Cloud Storage [Home](https://rclone.org/swift/) [Config](https://rclone.org/swift/)
* OpenDrive [Home](https://www.opendrive.com/) [Config](https://rclone.org/opendrive/)
* OpenStack Swift [Home](https://docs.openstack.org/swift/latest/) [Config](https://rclone.org/swift/)
* Oracle Cloud Storage Swift [Home](https://docs.oracle.com/en-us/iaas/integration/doc/configure-object-storage.html) [Config](https://rclone.org/swift/)
* Oracle Object Storage [Home](https://www.oracle.com/cloud/storage/object-storage) [Config](https://rclone.org/oracleobjectstorage/)
* ownCloud [Home](https://owncloud.org/) [Config](https://rclone.org/webdav/#owncloud)
* pCloud [Home](https://www.pcloud.com/) [Config](https://rclone.org/pcloud/)
* Petabox [Home](https://petabox.io/) [Config](https://rclone.org/s3/#petabox)
* PikPak [Home](https://mypikpak.com/) [Config](https://rclone.org/pikpak/)
* Pixeldrain [Home](https://pixeldrain.com/) [Config](https://rclone.org/pixeldrain/)
* premiumize.me [Home](https://premiumize.me/) [Config](https://rclone.org/premiumizeme/)
* put.io [Home](https://put.io/) [Config](https://rclone.org/putio/)
* Proton Drive [Home](https://proton.me/drive) [Config](https://rclone.org/protondrive/)
* QingStor [Home](https://www.qingcloud.com/products/storage) [Config](https://rclone.org/qingstor/)
* Qiniu Cloud Object Storage (Kodo) [Home](https://www.qiniu.com/en/products/kodo) [Config](https://rclone.org/s3/#qiniu)
* Quatrix by Maytech [Home](https://www.maytech.net/products/quatrix-business) [Config](https://rclone.org/quatrix/)
* Rackspace Cloud Files [Home](https://www.rackspace.com/cloud/files) [Config](https://rclone.org/swift/)
* rsync.net [Home](https://rsync.net/products/rclone.html) [Config](https://rclone.org/sftp/#rsync-net)
* Scaleway [Home](https://www.scaleway.com/object-storage/) [Config](https://rclone.org/s3/#scaleway)
* Seafile [Home](https://www.seafile.com/) [Config](https://rclone.org/seafile/)
* Seagate Lyve Cloud [Home](https://www.seagate.com/gb/en/services/cloud/storage/) [Config](https://rclone.org/s3/#lyve)
* SeaweedFS [Home](https://github.com/chrislusf/seaweedfs/) [Config](https://rclone.org/s3/#seaweedfs)
* SFTP [Home](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol) [Config](https://rclone.org/sftp/)
* Sia [Home](https://sia.tech/) [Config](https://rclone.org/sia/)
* SMB / CIFS [Home](https://en.wikipedia.org/wiki/Server_Message_Block) [Config](https://rclone.org/smb/)
* StackPath [Home](https://www.stackpath.com/products/object-storage/) [Config](https://rclone.org/s3/#stackpath)
* Storj [Home](https://storj.io/) [Config](https://rclone.org/storj/)
* Synology [Home](https://c2.synology.com/en-global/object-storage/overview) [Config](https://rclone.org/s3/#synology-c2)
* SugarSync [Home](https://sugarsync.com/) [Config](https://rclone.org/sugarsync/)
* Tencent Cloud Object Storage (COS) [Home](https://intl.cloud.tencent.com/product/cos) [Config](https://rclone.org/s3/#tencent-cos)
* Uloz.to [Home](https://uloz.to/) [Config](https://rclone.org/ulozto/)
* Uptobox [Home](https://uptobox.com/) [Config](https://rclone.org/uptobox/)
* Wasabi [Home](https://wasabi.com/) [Config](https://rclone.org/s3/#wasabi)
* WebDAV [Home](https://en.wikipedia.org/wiki/WebDAV) [Config](https://rclone.org/webdav/)
* Yandex Disk [Home](https://disk.yandex.com/) [Config](https://rclone.org/yandex/)
* Zoho WorkDrive [Home](https://www.zoho.com/workdrive/) [Config](https://rclone.org/zoho/)
* The local filesystem [Home](https://rclone.org/local/) [Config](https://rclone.org/local/)

## [**](#virtual-providers)Virtual providers

These backends adapt or modify other storage providers:

* Alias: Rename existing remotes [Home](https://rclone.org/alias/) [Config](https://rclone.org/alias/)

* Cache: Cache remotes (DEPRECATED) [Home](https://rclone.org/cache/) [Config](https://rclone.org/cache/)

* Chunker: Split large files [Home](https://rclone.org/chunker/) [Config](https://rclone.org/chunker/)

* Combine: Combine multiple remotes into a directory tree [Home](https://rclone.org/combine/) [Config](https://rclone.org/combine/)

* Compress: Compress files [Home](https://rclone.org/compress/) [Config](https://rclone.org/compress/)

* Crypt: Encrypt files [Home](https://rclone.org/crypt/) [Config](https://rclone.org/crypt/)

* Hasher: Hash files [Home](https://rclone.org/hasher/) [Config](https://rclone.org/hasher/)

* Union: Join multiple remotes to work together [Home](https://rclone.org/union/) [Config](https://rclone.org/union/)

## [**](#links)Links

* [Home page](https://rclone.org/)
* [GitHub project page for source and bug tracker](https://github.com/rclone/rclone)
* [Rclone Forum](https://forum.rclone.org/)
* [Downloads](https://rclone.org/downloads/)


