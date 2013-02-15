Summary:        macros for emulator build
Name:           emulator-macros
Version:        1
Release:        1
Group:          System/Base
License:        GPLv2+
BuildArch:      noarch
Source0:        macros.emulator

%description
Macros for emulator build

%prep

%build

%install
mkdir -p %{buildroot}/etc/rpm
install -m 644 %{SOURCE0} %{buildroot}/etc/rpm

%post

%postun

%files
%config /etc/rpm/macros.emulator
