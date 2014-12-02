windows-starter-kit
===================
![](https://s3.amazonaws.com/qubell-images/nopCommerce_logo.png)

Installs and configures nopCommerce Store.

[![Install](https://raw.github.com/qubell-bazaar/component-skeleton/master/img/install.png)](https://express.qubell.com/applications/upload?metadataUrl=https://raw.github.com/jollyrojer/windows-starter-kit/master/meta.yml)

Features
--------
 - Installs and configures nopCommerce ASP.NET (MVC) based demo Store on MS IIS 8 with MS SQL 2008 (or higher) backend database.

Configurations
--------------
 - nopCommerce 3.40, MS Windows 2012 R2 Server (us-east-1/ami-c49c0dac), AWS EC2 m3.medium, Administrator
 - nopCommerce 3.40, MS Windows 2012 R2 Server (us-west-1/ami-45332200), AWS EC2 m3.medium, Administrator
 
Pre-requisites
--------------
 - Configured Cloud Account a in chosen environment
 - Either installed Chef on target compute OR launch under root
 - Internet access from target compute:
   - Cloudera CDH and CM distribution
   - S3 bucket with Chef recipes: qubell-starter-kit-artifacts
   
Implementation notes
--------------------
 - Installation is based on Qubell components:
   - https://github.com/qubell-bazaar/component-iis
   - https://github.com/qubell-bazaar/component-mssql

Configuration parameters
------------------------
- input.db-user: Desired database user
- input.db-user-password: Database user password
- input.pool-name: IIS Pool name
- input.app-name: IIS App name
- input.admin-email: Store admin email
- input.admin-pass: Store admin password
- input.site-source-url: nopCommerce sources download URL
