%define	_class	SOAP
%define	modname	%{_class}

Summary:	Client/Server for PHP
Name:		php-pear-%{modname}
Version:	0.13.0
Release:	4
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/SOAP/
Source0:	http://download.pear.php.net/package/SOAP-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear
Requires:	php-bcmath
Requires:	php-pear-HTTP_Request
Requires:	php-pear-Net_URL
Requires:	php-pear-Net_DIME

%description
Implementation of SOAP protocol and services.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/example
%{_datadir}/pear/%{_class}
%{_datadir}/pear/tools/genproxy.php
%{_datadir}/pear/packages/%{modname}.xml

