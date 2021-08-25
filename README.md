# Savapage-bin-SPEC

Spec files for the arch depended binaries of SavePage.

The results are not indented to be installed on a running system.  
Their existence are meant to be build-requirements for SavaPage.  

The rpm's install the binaries in `/opt/savapage-bin-%{_target}/` ,  
which (as an example) on arm 32bit expands to `/opt/savapage-bin-armv7l-linux/`

Note: (large) source files are not included in this repository. They can be downloaded from the SavaPage repositories (as documented in the SPEC files)

- [savapage-nss](https://gitlab.com/savapage/savapage-nss)
- [savapage-pam](https://gitlab.com/savapage/savapage-pam)
- [savapage-cups-notifier](https://gitlab.com/savapage/savapage-cups-notifier)
- [xmlrpcpp](https://gitlab.com/savapage/xmlrpcpp)