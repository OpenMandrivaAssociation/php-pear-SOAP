%define		_class		SOAP
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	0.12.0
Release:	%mkrel 6
Summary:	Client/Server for PHP
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/SOAP/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-bcmath
Requires:	php-pear-HTTP_Request
Requires:	php-pear-Net_URL
Requires:	php-pear-Net_DIME
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Implementation of SOAP protocol and services.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/example
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.12.0-6mdv2011.0
+ Revision: 667639
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.12.0-5mdv2011.0
+ Revision: 607142
- rebuild

* Tue Nov 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.12.0-4mdv2010.1
+ Revision: 467084
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.12.0-3mdv2010.0
+ Revision: 426667
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.12.0-2mdv2009.1
+ Revision: 321897
- rebuild

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 0.12.0-1mdv2009.0
+ Revision: 272596
- 0.12.0

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.10.1-3mdv2009.0
+ Revision: 224881
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.10.1-2mdv2008.1
+ Revision: 178536
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.10.1-1mdv2008.0
+ Revision: 15746
- 0.10.1


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.4-1mdv2007.0
+ Revision: 82529
- Import php-pear-SOAP

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.4-1mdk
- 0.9.4

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.3-1mdk
- 0.9.3
- new group (Development/PHP)

* Sat Sep 03 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-8mdk
- fix #17668

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-5mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-4mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-3mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-2mdk
- fix spec file to conform with the others

* Thu Jan 20 2005 Pascal Terjan <pterjan@mandrake.org> 0.8.1-1mdk
- First mdk package

