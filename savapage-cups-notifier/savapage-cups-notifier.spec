%global version 1.3.0
%global releastag  %{version}.20210809


%global binname savapage-notifier

Name:           savapage-cups-notifier
Version:        %{version}
Release:        1%{?dist}
Summary:        CUPS notifier for SavaPage
License:        AGPL-3.0-or-later
URL:            https://www.savapage.org/
Source0:        https://gitlab.com/savapage/%{name}/-/archive/%{releastag}/%{name}-%{releastag}.tar.gz
Source1:        https://gitlab.com/savapage/xmlrpcpp/-/archive/%{releastag}/xmlrpcpp-%{releastag}.tar.gz

BuildRequires: cups-devel
BuildRequires: libstdc++-static

%description
CUPS notifier for SavaPage


%prep
%setup -q -T -b 1 -n xmlrpcpp-%{releastag}
%setup -q -n %{name}-%{releastag}

# patch the makefile of savapage-cups-notifier to find xmlrpcpp-%%{releastag}
/bin/sed -i "s/..\/xmlrpcpp/..\/xmlrpcpp-%{releastag}/" makefile


%build
#build xmlrpcpp first
cd  %{_builddir}/xmlrpcpp-%{releastag}
%{make_build} all

#now build savapage-cups-notifier
cd  %{_builddir}/%{name}-%{releastag}
%{make_build} all

%install
mkdir -p %{buildroot}/opt/savapage-bin-%{_target}/
install -m 755 target/%{binname} %{buildroot}/opt/savapage-bin-%{_target}/%{binname}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
/opt/savapage-bin-%{_target}/%{binname}

%changelog
* Wed Aug 25 2021 Mark Verlinde <mark.verlinde@gmail.com> 1.3.0-1
- First Build