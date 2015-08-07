Title: Zimbra Auto Provisioning from FreeIPA
Date: 2015-08-07
Tags: zimbra, freeipa, ldap
Category: sysadmin

After quite a few days struggling to configure a Zimbra server so that it automatically fetches users from our freeIPA (LDAP) server, I finally managed to have a configuration which works. I got help from a bunch of pages like [this](http://imanudin.net/2014/12/09/zimbra-external-ad-automatically-create-mailboxes-zimbra-with-lazy-mode-auto-provisioning/) and [this](https://www.zimbra.com/docs/ne/8.0.2/administration_guide/wwhelp/wwhimpl/js/html/wwhelp.htm#href=ZCS_8_0_2_Admin_Guide.Auto_Provisioning_New_Accounts_from_External_LDAP.html) one. This comes after you fix the external LDAP authentication and probably also external GAL configuration on your Zimbra server.

`zmprov` gives you a nice terminal to configure the server:

    $ su - zimbra
    $ zmprov

This is the set of commands I used to set it up:

    prov> md mysampledomain.net zimbraAutoProvAccountNameMap "uid"
    prov> md mysampledomain.net zimbraAutoProvAttrMap "givenName=givenName"
    prov> md mysampledomain.net +zimbraAutoProvAttrMap "sn=sn"
    prov> md mysampledomain.net zimbraAutoProvBatchSize 80
    prov> md mysampledomain.net zimbraAutoProvLdapAdminBindDn "uid=mail_server,cn=users,cn=accounts,dc=mysampledomain,dc=net"
    prov> md mysampledomain.net zimbraAutoProvLdapAdminBindPassword "myverysecretpassword"
    prov> md mysampledomain.net zimbraAutoProvLdapBindDn "uid=mail_server,cn=users,cn=accounts,dc=mysampledomain,dc=net"
    prov> md mysampledomain.net zimbraAutoProvLdapSearchBase "cn=accounts,dc=mysampledomain,dc=net"
    prov> md mysampledomain.net zimbraAutoProvLdapSearchFilter "(&(ObjectClass=person))"
    prov> md mysampledomain.net zimbraAutoProvLdapStartTlsEnabled TRUE
    prov> md mysampledomain.net zimbraAutoProvLdapURL "ldaps://ipa.mysampledomain.net:636"
    prov> md mysampledomain.net zimbraAutoProvPollingInterval "10m"
    prov> md mysampledomain.net zimbraAutoProvScheduledDomains "mysampledomain.net"
    prov> md mysampledomain.net zimbraAutoProvMode "EAGER"

To diagnose why the system wasn't working, I also had to figure out where the log files are, and how to produce more logs. Oddly enough, they're not in `/var/log`, and instead they are written by default in `/opt/zimbra/log/mailbox.log`, or other related files in that folder. I added `log4j.logger.zimbra.autoprov=TRACE` at the end of my `/opt/zimbra/conf/log4j.properties` file, which will be overwritten next time I restart the services using the configurations in `/opt/zimbra/conf/log4j.properties.in`. Finally to make the logging system reload the logging configuration, you need to run `zmprov rlog`. You find more info [here](http://wiki.zimbra.com/wiki/Using_log4j_to_Configure_mailboxd_Logging).