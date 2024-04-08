Name:           obs-service-install_packages
Summary:        An OBS source service: tool for installing packages
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
Version:        0.1.0
Release:        1
Source:         %name-%version.tar.gz
#Requires:       rpm
Requires:       dnf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

It supports installing packages.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/lib/obs/service
install -m 0755 install_packages         %{buildroot}/usr/lib/obs/service
install -m 0644 install_packages.service %{buildroot}/usr/lib/obs/service
install -m 0644 -t %{buildroot}/usr/lib/obs/service *.rpm

%files
%defattr(-,root,root)
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
* Thu Apr 4 2024 Takahiro Ono <takahiro.ono@miraclelinux.com> - 0.1.0-1
- First obs-service-install_packages package
