%global version 1.3.0
%global releastag  %{version}.20210809       

Name:           savapage-nss
Version:        %{version}
Release:        1%{?dist}
Summary:        Savapage ns-switch utillety
License:        AGPL-3.0-or-latermake-releastag
URL:            https://www.savapage.org/
Source0:        https://gitlab.com/savapage/%{name}/-/archive/%{releastag}/%{name}-%{releastag}.tar.gz

BuildRequires: libstdc++-static

%description
Module for savapage to retrieve information about GNU/Linux 
users and groups using the Name Service Switch.


%prep
%setup -q -n %{name}-%{releastag}

%build
%{make_build} all

%install
mkdir -p %{buildroot}/opt/savapage-bin-armv7l/ 
install -m 755 target/%{name} %{buildroot}/opt/savapage-bin-armv7l/%{name}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
/opt/savapage-bin-armv7l/%{name}

%changelog
* Wed Aug 25 2021 Mark Verlinde <mark.verlinde@gmail.com> 1.3.0-1
- First Build