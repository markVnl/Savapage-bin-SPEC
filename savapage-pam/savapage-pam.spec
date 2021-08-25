%global version 1.3.0
%global releastag  %{version}.20210809       

Name:           savapage-pam
Version:        %{version}
Release:        1%{?dist}
Summary:        Savapage PAM utillety
License:        AGPL-3.0-or-later
URL:            https://www.savapage.org/
Source0:        https://gitlab.com/savapage/%{name}/-/archive/%{releastag}/%{name}-%{releastag}.tar.gz

BuildRequires: pam-devel
BuildRequires: libstdc++-static

%description
Module for savapage to authenticate a GNU/Linux user with PAM
(Pluggable Authentication Modules).

%prep
%setup -q -n %{name}-%{releastag}

%build
%{make_build} all

%install
mkdir -p %{buildroot}/opt/savapage-bin-%{_target}/ 
install -m 755 target/%{name} %{buildroot}/opt/savapage-bin-%{_target}/%{name}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
/opt/savapage-bin-%{_target}/%{name}

%changelog
* Wed Aug 25 2021 Mark Verlinde <mark.verlinde@gmail.com> 1.3.0-1
- First Build